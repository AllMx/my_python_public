divmod(5,2)[1]
#1

pow(3,2)
#9

a='hello word python'
b='love'
c=a[0:6]+b+a[10:100]
#'hello love python'

a='hello word python'
c='{0} {2} {1}'.format(*a.split())
#'hello python word'

#------------------
    # Использование * и ** для передачи аргументов в функцию;
    # Использование * и ** для сбора переданных в функцию аргументов;
    # Использование ** для принятия только именованные аргументов;
    # Использование * при распаковке кортежей;
    # Использование * для распаковки итерируемых объектов в список/кортеж;
    # Использование ** для распаковки словарей в другие словари.
#-------------------- 

a='hello word python'
b=list('abc')
c=dict(zip(b,a.split()))
d='{a} {b} {c}'.format(**c) #Функция zip объединяет в кортежи элементы из последовательностей переданных в качестве аргументов.
#'hello python word'

a=list(map(str,list(range(5))))
#['0', '1', '2', '3', '4']

a=list(map(lambda x:x*x,list(range(6))))
#[0, 1, 4, 9, 16, 25]

a=[x*x for x in range(10) if x//2==0]
#[0, 1]

a=list(range(5))
a.append(3)
#[0, 1, 2, 3, 4, 3]

a=list(range(5))
reversed(a)
#[0, 1, 2, 3, 4]

def summa(a,b):
    return a+b
a=summa(4,4)
#8

def summa(a,b):
    return a+b
a=summa((4),(4))
#8

def f1(x):
    return x*x
def f2(*arr):
    return map(f1,arr)######### как вытащить данные
a=list(range(5))
print(f2(a))
#map object

a=[x*x for x in range(5)]
b={str(x):x*x for x in range(5)}
def f1(*a,**kw):
    print('args',a)
    print('kwargs',kw)
f1(a)
#args ([0, 1, 4, 9, 16],) kwargs {}

a=[x*x for x in range(5)]
b={str(x):x*x for x in range(5)}
def f1(*a,**kw):
    print('args',a)
    print('kwargs',kw)
f1(b)
#args ({'2': 4, '0': 0, '4': 16, '1': 1, '3': 9},) kwargs {}

a=[x*x for x in range(5)]
b={str(x):x*x for x in range(5)}
def f1(*a,**kw):
    print('args',a)
    print('kwargs',kw)
f1(**b)
#args () kwargs {'2': 4, '0': 0, '1': 1, '3': 9, '4': 16}

import os
for i in os.listdir():
    print(i)
#список всех файлов и всех папок в корневой папке 

import os
for i in os.listdir('..'):
    if os.path.isfile(i): print(i)
#список всех файлов в папке уровнем выше 

import os
import shutil
os.mkdir('One')
os.mkdir('Two')
file01=open('One\\text01.txt','w+')
file01.close()
shutil.move('One\\text01.txt','One\\text02.txt') #################
#переименуется в text02.txt 

#--------------------------------
# 	shutil.move(src, dst, copy_function=copy2) - рекурсивно перемещает файл или директорию (src) в другое место (dst), и возвращает место назначения.
# 	Если dst - существующая директория, то src перемещается внутрь директории. Если dst существует, но не директория, то оно может быть перезаписано.
#--------------------------------

import hashlib
a=b'привет Питон'
h1=hashlib.md5(a)
print(h1)
#ошибка исполнения 
