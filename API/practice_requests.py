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

