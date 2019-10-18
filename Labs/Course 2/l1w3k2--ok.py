# Лаборатория
# 1. Осуществить ввод адреса Интернет-страницы.
# 2. Осуществить поиск всех изображений на странице.
# 3. Удалить дубликаты.
# 4. Удалить адреса без http или https.
# 5. Вывести адреса изображений с нумерацией, нумерацию изображений начинать с 1.
# 6. Потоками осуществить загрузку изображений и информацию о загрузке вывести на экран отдельными строками
# 7. В случае невозможности загрузки выводить 'error'.

# Пример входных данных:
# https://ya.ru/

# Пример выходных данных:
# 1 izobrazhenie https://mc.yandex.ru/watch/723233
# Potok 1 zakonchil zagruzku https://mc.yandex.ru/watch/723233

import urllib.request
import re
import threading

count = 1
lock = threading.Lock()
def download(imaga):
    global count 
    lock.acquire()

    try:
        page=urllib.request.urlopen(imaga)
        print(str(threading.currentThread().getName()) + ' zakonchil zagruzku ' + imaga)
    except:
        print('error')
    finally:
    	count = count +1
    	lock.release()

if __name__=='__main__':

	url = input()
	pisk = re.compile(r'<\s*?img.+?src="\s*?(http\S+)\s*?"', re.IGNORECASE)
	srcs = []
	thrs=[]

	html = urllib.request.urlopen(url).read().decode()
	imag = pisk.findall(html)

	for i in range(len(imag)):
		if imag[i] not in srcs:
	    		srcs.append(imag[i])
	    		print(str(i + 1) + ' izobrazhenie '+ str(srcs[i]))

	for i in range(len(srcs)):
		my_thread=threading.Thread(target=download, name='Potok ' + str(i+1), args=(srcs[i], ))
		thrs.append(my_thread)
		my_thread.start()
		for t in thrs:
			my_thread.join()

#ok