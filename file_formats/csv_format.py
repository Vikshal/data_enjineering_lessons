"""
CSV(Comma-Separated Values) - формат, который чаще всего используется для хранения табличных данных

Пример данных в формате csv:

Name, Age, City                  # названия столбцов
Alice, 30, New York              # строки со значениями
Bob, 25, London                  # строки со значениями
Carlos, 28, Moscow               # строки со значениями

CSV используют для экспорта и импорта данных из таблиц, отчетов, систем управления персоналом.
Он очень прост и эффективен для хранения больших объемов данных, особенно, елси вам не нужна сложная структура

Pandas - библиотека Python для работы с таблицами. Сделаем формат json с помощью pd.DataFrame() выводом в виде таблицы и сохраним ее в файл формата csv

----------------------------------------------
import pandas as pd

l_connections = [
    {
        "user_name": "etl_user",
        "password": "123"

    } ,
    {
        "user_name": "test_user",
        "password": "456"
    } 
]

df1 = pd.DataFrame(l_connections)
print(df1)
print(type(df1))

df1.to_csv("pandas_csv_file.csv") # сохраняем таблицу в файл pandas_csv_file.csv
----------------------------------------------

Таблица сохранилась вместе с индексами. Если они нам не нужны, нужно добавить параметр

----------------------------------------------
df1.to_csv("pandas_csv_file.csv", index=False) # сохраняем таблицу в файл pandas_csv_file.csv без индексов
----------------------------------------------

"""

import pandas as pd

l_connections = [
    {
        "user_name": "etl_user",
        "password": "123"

    } ,
    {
        "user_name": "test_user",
        "password": "456"
    } 
]

df1 = pd.DataFrame(l_connections)
print(df1)
print(type(df1))

df1.to_csv("pandas_csv_file.csv", index=False) # сохраняем таблицу в файл pandas_csv_file.csv без индексов

df2 = pd.read_csv("pandas_csv_file.csv")
print(df2)
print(type(df2))