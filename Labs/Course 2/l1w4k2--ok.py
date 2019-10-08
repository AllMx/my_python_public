# Лаборатория
# 1. Осуществить ввод адреса Интернет-страницы.
# 2. Осуществить поиск всех изображений на странице.
# 3. Удалить дубликаты.
# 4. Удалить адреса без http или https.
# 5. Вывести адреса изображений с нумерацией, нумерацию изображений начинать с 1.
# 6. Процессами или пулами (выбрать подходящий вариант самостоятельно) осуществить загрузку изображений и информацию о загрузке вывести на экран отдельными строками.
# 7. В случае невозможности загрузки выводить 'error download'.

# Пример входных данных:
# https://ya.ru/

# Пример выходных данных:
# 1 image https://mc.yandex.ru/watch/723233
# Process 1 downloaded https://mc.yandex.ru/watch/723233
# Вариант

import urllib.request
import re
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Lock

count = 1

def download(imaga, lock):
    global count
    lock.acquire()

    try:
        page=urllib.request.urlopen(imaga) 
        print(str(current_process().name + ' image  ' + imaga )) #7


    except:        
        print('error download')
    finally:
        count = count + 245
        lock.release()

if __name__=='__main__':


    url = input()
    pisk = re.compile(r'<\s*?img.+?src="\s*?(http\S+)\s*?"', re.IGNORECASE)
    srcs = []
    procs=[]
    lock=Lock()

    html = urllib.request.urlopen(url).read().decode()
    imag = pisk.findall(html)

    for i in range(len(imag)):
        if imag[i] not in srcs:
                srcs.append(imag[i])
                print(str(i + 1) + ' izobrazhenie '+ str(srcs[i]))

    for i in range(len(srcs)):    
        my_proc=Process(target=download, name='Process ' + str(i+1), args=(srcs[i], lock))
        procs.append(my_proc)
        my_proc.start()
        for proc in procs:
            proc.join()
