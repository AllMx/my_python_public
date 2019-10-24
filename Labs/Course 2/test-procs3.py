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
#-------------------------NE OK---------------------
import urllib.request
import re
from multiprocessing import Process, Pool


pisk = re.compile(r'Django 2[.]0')

def get_urls(url):
	#urls=[]
	# i = 1
	# while 1:
	# 	urlx = url + '?page={}'.format(i)
	# 	try:
	# 		print(urlx)
	# 		if urllib.request.urlopen(urlx):
	# 			#print(html)
	# 			urls.append(urlx)
	# 			i += 1
	# 	except:
	# 		break
	# 	#urls = 
	urls=[url+'?page={}'.format(i) for i in range(1,56)]
	print(urls)
	return urls
def get_res(url):
	global pisk
	django = 0
	try:
	    html = urllib.request.urlopen(url).read().decode()
	    django = len(pisk.findall(html))
	    print(url, django)
	    return django
	except:
	    return 0
def main(urls, proc):
	with Pool(processes=proc) as p:
		numbers=p.map(get_res, urls)
	print(sum(numbers))
if __name__=='__main__':
	url_proc= input().split()
	url=str(url_proc[0])
	proc=int(url_proc[1])
	urls=get_urls(url)
	numbers=0
	main(urls,proc)