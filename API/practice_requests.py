# import requests as r

# try:
#     post_response = r.get("https://jsonplaceholder.typicode.com/posts")
#     post_response.raise_for_status()

#     try:
#         posts = post_response.json()
#     except r.exceptions.JSONDecodeError:
#         print("JSONDecodeError")

#         posts = []


#     try:
#         id = int(input("id: "))
#     except Exception:
#         print("Not integer")
#         id = 1

#     for post in posts:
#         if post['id'] == id:
#             print(post)
#             user_response = r.get("https://jsonplaceholder.typicode.com/users/" + str(post['userId']), timeout=10)
#             post_response.raise_for_status()

#             try:
#                     user = user_response.json()
#             except r.exceptions.JSONDecodeError:
#                 print("JSONDecodeError")
#                 user = None

#             if user is not None:
#                 print(f"{user['name']} {user['email']}")



# except r.exceptions.Timeout:
#     print('timeout')
# except Exception as e:
#     print(e)




# import requests ________  отправка заголовков headers с запросом и как роботу сойти за человека ________ 

# response = requests.get("https://google.com")

# print(response.text[:1000])

# response = requests.get("https://google.com", headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
# })

# print(response.text[:1000])


# import requests ________ сессия для хранения контекста запросов ________ 

# session = requests.session()

# print(session.cookies)

# session.get("https://google.com")

# print(session.cookies)


# import requests ________ скачивание маленьких файлов из интернета ________

# response_images = requests.get("https://httpbin.org/image/jpeg")

# with open("image1.jpeg", "wb") as file:
#     file.write(response_images.content)

# print(response_images.text[:100])
# print(response_images.content[:100])


# import requests ________ скачивание больших файлов из интернета ________

# with requests.get("https://httpbin.org/image/jpeg", stream=True) as r:
#     with open("image2.jpeg", "wb") as file:
#         for chunk in r.iter_content(128):
#             print("128")
#             file.write(chunk)

# import requests
# import pandas as pd

# data = []

# try:
#     response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=10)
#     response.raise_for_status()
#     data = response.json()
# except requests.exceptions.JSONDecodeError:
#     print('JSONDecodeError')
# except requests.exceptions.RequestException as e:
#     print(e)

# df = pd.DataFrame(data[:5])
# print(df)

''' Задание для практики. Посмотреть/прочитать, как работает requests + pandas для получения данных из API. Написать extract.py, который просто печатает первые 5 строк ответа. Использовать get, проработать ошибки и вывести результат в виде таблицы. API: 'https://jsonplaceholder.typicode.com/posts' Сохранить таблицу в файл extract.csv '''

import requests
import pandas as pd


def extract(url: str, timeout: int = 30) -> pd.DataFrame:
    data = []
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print('JSONDecodeError')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка: {e}')

    return pd.DataFrame(data[:5])


def save_to_csv(df: pd.DataFrame, path:str) -> None:
    if df.empty:
        print('no data')
        return
    try:
        df.to_csv(path, index=False, encoding="utf-8")
        print(f'{len(df)} lines saved to {path} successful')
    except PermissionError:
        print("no access to the folder")
    except OSError as e:
        print(f"system error {e}")


if __name__ == '__main__':
    df = extract('https://jsonplaceholder.typicode.com/posts')
    print(df)
    save_to_csv(df, "extract.csv")




