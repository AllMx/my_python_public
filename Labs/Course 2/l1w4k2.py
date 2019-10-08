import urllib.request
import re
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Lock


def download(imaga, lock):
    lock.acquire()
    try:
        page=urllib.request.urlopen(imaga) 
        print(str(current_process().name + ' downloaded ' + imaga )) #7
    except:        
        print('error download')
    finally:
        lock.release()

if __name__=='__main__':
    url = "http://ya.ru"
    lock=Lock()
    pisk = re.compile(r'<img.+?src="(\S+)"')
    srcs = []
    procs=[]

    html = urllib.request.urlopen(url).read().decode()
    imag = pisk.findall(html) 
    if not len(imag):
        print('error')
    else:
        imag = list(set(imag)) #3 Удалить дубликаты.
        for i in range(1, len(imag) +1):
            if "http" not in imag[len(imag) - i] or "https" not in imag[len(imag) - i]:
                del imag[len(imag) - i] 
            else:
                srcs.append(imag[len(imag) - i])
        for i in range(len(srcs)): 
            print(str(i + 1) + ' image '+ str(srcs[i])) 
        for i in range(len(srcs)):
            my_proc=Process(target=download, name='Process ' + str(i+1), args=(srcs[i],lock))
            procs.append(my_proc)
            my_proc.start()
        for proc in procs:
            proc.join()


        #ocenka 0