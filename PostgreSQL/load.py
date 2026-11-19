"""Когда мы пробовали открыть и читать csv файл, мы просто смотрели на данные в терминале. Теперь наша задача сохранить эти данные в виде списка словарей. Вот наш код изначальной версии:"""

#Давайте откроем и прочитаем csv файл
# import csv
# with open('extract.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(f"{row['userId']}, {row['id']}, {row['title']}, {row['body']}")

"""Теперь, чтобы загрузить данные нам необходимо каждый row сохранять в список"""

import csv
with open('extract.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    columns = reader.fieldnames
    rows = []
    for row in reader:
        rows.append(row)
print(len(rows))
print(rows[0])
print(rows[0].keys())
