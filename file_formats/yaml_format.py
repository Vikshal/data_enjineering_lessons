"""
2 случая для использования формата yaml: 
1) хранение конфигов
2) возможность сохранить данные и в последующем открывать их в том виде, в каком и сохранили(списки, словари)

Установите пакет pyyaml через терминал с помощью команды - pip install pyyaml

Далее напишем программу которая сохраняет список словарей в папке проекта в файл под названием connections с расширением yaml

-------------------------------------------
import yaml

l_connectional = [
    {
        "user_name": "etl_user",
        "password": "123"

    } ,
    {
        "user_name": "test_user",
        "password": "456"
    } 
]

with open(r'connections.yaml', 'a') as file: # здесь мы не прописали путь сохранения, поэтому файл сохранится в нашу папку
    documents = yaml.dump(l_connectional, file)
-----------------------------------------------

После выполнения программы мы увидим появившийся новый файл внутри которого будет слудующее:

-----------------------------------------------
- password: '123'
  user_name: etl_user
- password: '456'
  user_name: test_user
-----------------------------------------------
  Дефис означает новый элемент списка

"""
import yaml

l_connectional = [
    {
        "user_name": "etl_user",
        "password": "123"

    } ,
    {
        "user_name": "test_user",
        "password": "456"
    } 
]

with open(r'connections.yaml', 'a') as file:
    documents = yaml.dump(l_connectional, file)