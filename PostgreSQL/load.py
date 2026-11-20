"""Когда мы пробовали открыть и читать csv файл, мы просто смотрели на данные в терминале. Теперь наша задача сохранить эти данные в виде списка словарей. Вот наш код изначальной версии:"""

#Давайте откроем и прочитаем csv файл
# import csv
# with open('extract.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(f"{row['userId']}, {row['id']}, {row['title']}, {row['body']}")

"""Теперь, чтобы загрузить данные нам необходимо каждый row сохранять в список"""

# import csv
# with open('extract.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     rows = []
#     for row in reader:
#         rows.append(row)
# print(len(rows))
# print(rows[0])
# print(rows[0].keys())
# print(columns)

"""
Далее нам необходимо загрузить данные в PostgreSQL. Для этого необходимо установить сам PostgreSQL на пк.""" 

# Далее мы будем работать с библотекой psycopg2. Перед установкой нужно активировать виртуальное окружение, чтобы в данном проекте была именно одна версия библиотеки. Для этого в терминале пишем команду: python -m venv venv. Мы создали окружение с названием venv. Теперь его необходимо активировать: venv\Scripts\activate


"""
Далее устанавливаем библиотеку: pip install psycopg2

Для подключения к бд пишем функцию:

import psycopg2

conn = psycopg2.connect(
    dbname="app_db",
    user="app_user",
    password="strong_password",
    host="localhost",
    port=5432
)

Когда соединение установится, создайте объект курсора: 

cursor = conn.cursor()

Можно создать несколько курсоров, но достаточно и одного. Он будет выступать интерфейсом для отправки SQL-запросов и получения результатов. 
"""

import psycopg2
import os
from dotenv import load_dotenv
import csv

load_dotenv()

DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")


with open('extract.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = []
    for row in reader:
        rows.append(row)
values = [(row["userId"], row["id"], row["title"], row["body"]) for row in rows]

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_data(
    "userId" INTEGER,
    id INTEGER PRIMARY KEY,
    title TEXT,
    body TEXT
);
""")
conn.commit()

cursor.executemany(
    'INSERT INTO raw_data ("userId", id, title, body) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING', values
)

conn.commit()
cursor.execute("SELECT * FROM raw_data")
print(cursor.fetchall())
