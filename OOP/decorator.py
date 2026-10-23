# Изучаем(повторяем) декораторы функций в Python.

'''
-----------------------------------------------
def func_decorator(func):
    def wrapper():
        print("----- что-то делаем перед вызовом функции -----")
        func()
        print("----- что-то делаем после вызова функции -----")

    return wrapper

def some_func():
    print("Вызов функции some_func")

f = func_decorator(some_func)
f()
-----------------------------------------------

У нас есть переменная f в глобальной области видимости, которая ссылается на внутреннюю функцию wrapper() определённую во внешней функции func_decorator(func), а параметр func ссылается на функцию some_func().

То есть, когда мы вызываем функцию f - на самом деле мы вызываем функцию wrapper(), она в свою очередь вызывает функцию func() - (в конкретном случае some_func()) и дополнительно что-то делает перед её вызовом и после (print("----- что-то ....) её вызова. Благодаря внутренней функции wrapper() мы расширяем функционал сторонней функции some_func()

Чтобы не создавать новые переменные, обычно при декорировании функций создают ссылку на то же самое имя
-----------------------------------------------

def func_decorator(func):

.........

some_func = func_decorator(some_func)
some_func()
-----------------------------------------------

В итоге функция some_func() как бы меняет свою работу. Она теперь не просто будет что-то выводить в консоль, но и дополнительно будут выполняться операции до её вызова и после (print("----- что-то ....)

А теперь попробуем добавить параметры в функцию some_func()

-----------------------------------------------
def func_decorator(func):
    def wrapper():
        print("----- что-то делаем перед вызовом функции -----")
        func()
        print("----- что-то делаем после вызова функции -----")

    return wrapper

def some_func(title):
    print(f"title = {title}")

some_func = func_decorator(some_func)
some_func("Python forever") # нужно прописать аргумент
-----------------------------------------------

Но при запуске программы мы увидим ошибку. Потому что внутренняя функция wrapper() не имеет никаких аргументов. Значит, чтобы в нашей программе не было ошибок в самом простом случае мы можем прописать параметр и в wrapper()

-----------------------------------------------
def func_decorator(func):
    def wrapper(title):
        print("----- что-то делаем перед вызовом функции -----")
        func(title)
        print("----- что-то делаем после вызова функции -----")

    return wrapper

def some_func(title):
    print(f"title = {title}")

some_func = func_decorator(some_func)
some_func("Python forever")
-----------------------------------------------

Но в таком случае, если у функции some_func() появится ещё параметр или вообще не будет параметров, то декоратор работать не будет

Мы можем записать декоратор в универсальном виде. Для этого во внутренней функции нужно принять произвольное число фактических параметров и формальных параметров - def wrapper(*args, **kwargs), а далее при вызове функции передать и распаковать - func(*args, **kwargs). Если они будут отсутствовать, то функции func() ничего передавться не будет

Теперь можете попробовать запустить программу с изменениями и проверить(добавить параметр или вызвать функцию без параметров)

-----------------------------------------------
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("----- что-то делаем перед вызовом функции -----")
        func(*args, **kwargs)
        print("----- что-то делаем после вызова функции -----")

    return wrapper

def some_func(title):
    print(f"title = {title}")

some_func = func_decorator(some_func)
some_func("Python forever")
-----------------------------------------------
----------------------------------
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("----- что-то делаем перед вызовом функции -----")
        func(*args, **kwargs)
        print("----- что-то делаем после вызова функции -----")

    return wrapper

def some_func(title, tag):
    print(f"title = {title}, {tag}")

some_func = func_decorator(some_func)
some_func("Python forever", "h1")

---------------------------
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("----- что-то делаем перед вызовом функции -----")
        func(*args, **kwargs)
        print("----- что-то делаем после вызова функции -----")

    return wrapper

def some_func():
    print(1)

some_func = func_decorator(some_func)
some_func()
-----------------------------------------------

А теперь давайте пропишем во внутренней функции wrapper() возвращение результата выполнения функции func(), чтобы избежать None в случае, если в функции some_func() юудет return

-----------------------------------------------
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("----- что-то делаем перед вызовом функции -----")
        res = func(*args, **kwargs)
        print("----- что-то делаем после вызова функции -----")
        return res

    return wrapper

def some_func(title, tag):
    print(f"title = {title}, {tag}")
    return f"<{tag}>{title}</{tag}>"

some_func = func_decorator(some_func)
res = some_func("Python forever", "h1")
print(res)
-----------------------------------------------
'''



"""
Зачем нужен декоратор?

Продемонстрируем на практическом примере

-----------------------------------------------
import time

def test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        dt = end - start
        print(f"Время работы: {dt} сек")
        return res

    return wrapper

# Алгоритм Евклида
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a

get_nod = test_time(get_nod)
get_fast_nod = test_time(get_fast_nod)
res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)
print(res, res2)
-----------------------------------------------
"""

"""
А теперь давайте декорируем функцию как это делают обычно в практике программирования  
Чтобы продекорировать функцию нужно перед ней написать декоратор с символом собаки @

-----------------------------------------------
import time

def test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        dt = end - start
        print(f"Время работы: {dt} сек")
        return res

    return wrapper

@test_time
# Алгоритм Евклида
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a

#get_nod = test_time(get_nod)
#get_fast_nod = test_time(get_fast_nod)
res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)
print(res, res2)
-----------------------------------------------
"""
