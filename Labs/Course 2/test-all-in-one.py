# Используя библиотеки threading или multiprocessing, осуществить поиск
# с использованием регулярных выражений по новостной ленте сайта
# https://www.djangoproject.com/weblog/ количества словосочетаний
# Django 2.0. На ввод данных подается адрес новостной ленты и число
# потоков или процессов через пробел, например:
# https://www.djangoproject.com/weblog/ 10
# вывод осуществляется числом, например:
# 14

# Пример входных данных:
# https://www.djangoproject.com/weblog/ 10
# Пример выходных данных:
# 14

#--THREADING-1---------------------------------------------------------------------------------------------------------

import urllib.request
import re
import threading

count = 0

def download(url, lock, pisk):
    global count
    lock.acquire()
    django = 0
    try:
        html = urllib.request.urlopen(url).read().decode()
        print(url)
        django = len(pisk.findall(html))
        print(threading.currentThread().getName() + ' django={}'.format(django)) #7
    except:
        print('error read')
    finally:
        count += django
        print(count)
        lock.release()

if __name__=='__main__':
    #a = input().split()
    a = "https://www.djangoproject.com/weblog/ 10".split()
    url = a[0] + '?page='
    potoks = int(a[1])
    pisk = re.compile(r'Django 2[.]0')

    thrs =[]
    lock = threading.Lock()
    
    for i in range(potoks):
        my_thread=threading.Thread(target=download, name='Potok ' + str(i+1), args=(url+str(i+1), lock, pisk))
        thrs.append(my_thread)
        my_thread.start()
        for t in thrs:
            my_thread.join()
    print(count)

#--THREADING-2---------------------------------------------------------------------------------------------------------

import urllib.request
import re
import threading
from multiprocessing.pool import ThreadPool



def download(url, pisk):
    django = 0
    try:
        html = urllib.request.urlopen(url).read().decode()
        print(url)
        django = len(pisk.findall(html))
        return django
    except:
        print('error read')
        return 0
    finally:
        print(django)

if __name__=='__main__':
    #a = input().split()
    a = "https://www.djangoproject.com/weblog/ 10".split()
    url = a[0] + '?page='
    potoks = int(a[1])
    pisk = re.compile(r'Django 2[.]0')
    pool = ThreadPool(processes=potoks)
    urls =[]
    count = 0
    for i in range(potoks):
        urls.append(url+str(i+1))

    for url in urls:
        async_result = pool.apply_async(download, (url, pisk))
        count += async_result.get() 

    print(count)

#--PROCESSING-1--------------------------------------------------------------------------------------------------------

import urllib.request
import re
from multiprocessing import Process, Value, Lock, current_process

def download(url, lock, pisk, count):
    lock.acquire()
    django = 0
    try:
        html = urllib.request.urlopen(url).read().decode()
 #       print(url)
        django = len(pisk.findall(html))
        print(current_process().name + ' django={}'.format(django)) #7
    except:
        print('error read')
    finally:
        count.value += django
        print(count.value)
        lock.release()

if __name__=='__main__':
    #a = input().split()
    a = "https://www.djangoproject.com/weblog/ 10".split()
    url = a[0] + '?page='
    potoks = int(a[1])

    pisk = re.compile(r'Django 2[.]0')
    procs=[]
    lock=Lock()
    counts = Value('d', 0)

    for i in range(potoks):
        my_proc=Process(target=download, name='Process ' + str(i+1), args=(url+str(i+1), lock, pisk, counts))
        procs.append(my_proc)
        my_proc.start()
        my_proc.join()
    print(counts.value)

#--PROCESSING-2--------------------------------------------------------------------------------------------------------

import urllib.request
import re
from multiprocessing import Process, Pool

#result_list = []
count = 0

def download(url, pisk):
    django = 0
    try:
        html = urllib.request.urlopen(url).read().decode()
        django = len(pisk.findall(html))
        return django
    except:
        return 0

def log_result(result):
    global count
    count += result
 #   result_list.append(int(result))
 #   print(count, result)

if __name__=='__main__':
    #a = input().split()
    a = "https://www.djangoproject.com/weblog/ 10".split()
    url = a[0] + '?page='
    potoks = int(a[1])

    pisk = re.compile(r'Django 2[.]0')
    pool = Pool(potoks)
    count = 0
    for i in range(potoks):
        async_result = pool.apply_async(download, args = (url+str(i+1), pisk), callback = log_result)
    pool.close()
    pool.join()

    print(count)