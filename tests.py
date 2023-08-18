import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def test_add_pet():
    input_pet = MultipartEncoder(fields={'name': 'Hitch', 'animal_type': 'cat', 'age': '4', 'pet_photo': ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')})
    # inp_pet = {'name': 'Hitch', 'animal_type': 'cat', 'age': '4', 'pet_photo': ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')}
    # Вообще, age в сваггере требует number. Но если не послать его строкой, ругается и не отправляет запрос

    header = {'accept': 'application/json',  'auth_key': '5be340894a8d13758243db49f68e112ee516633ad80b0d67a0ce933c',
              'Content-Type': input_pet.content_type}
    # вообще-то в строке curl в сваггере в значение ключа 'Content-Type' значится multipart/form-data.
    # Но если написать в хедере 'Content-Type': multipart/input_pet, ничего не получается
    # header = {'accept': 'application/json',  'auth_key': '5be340894a8d13758243db49f68e112ee516633ad80b0d67a0ce933c',
    #         'Content-Type': MultipartEncoder/form-data}

    res = requests.post(url='https://petfriends.skillfactory.ru/api/pets', data=input_pet, headers=header)
    status = res.status_code
    result = res.json()
    print('\n*', status, result['name'])