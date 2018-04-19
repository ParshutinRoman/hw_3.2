import requests
import os
from pprint import pprint
import chardet

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, lang):

    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def translate_file():
    files = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith('.txt')]
    for file in files:
        with open(file, 'rb') as f:
            data = f.read()
            result = chardet.detect(data)
            text = data.decode(result['encoding'])
        name_file = 'translated-' + file
        with open(name_file, 'w') as f:
           f.write(translate_it(text, 'ru'))


translate_file()

