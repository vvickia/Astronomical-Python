''' Скачать файл GalaxyZoo1_DR_table2.csv, написать скрипт, который парсит этот файл и находит 
там галактики необходимых типов (выбрать себе тип: эллиптические, спиральные или с ребра),
ориентируясь на эти голоса. То есть, программа читает файл строчку за строчкой и смотрит 
соотношение голосов: если у P_EL большие голоса, а у спиральной маленькие, то это эллиптическая
галактика. То же с P_EDGE.
Скрипт лезет на сайт SDSS и скачивает оттуда картинки. Нужна страница (url), в которую если мы 
подставим вместо ra восхождение, вместо dec -- склонение, то она вернет ??? с такой картинкой.
Нужно написать такой скрипт, который скачивает картинки галактик нужного типа. Распараллелить. 
Использовать threading (5 потоков) или multiprocessing. Должен быть интерфейс. '''

import math
import urllib.request
import threading
import numpy as np
from tqdm import tqdm

table = open('GalaxyZoo1_DR_table2.csv', 'r').readlines()[1:]

def foo(table):
    for line in tqdm(table):
        args = line.split(',')
        OBJID = int(args[0])
        RA = args[1].split(':')
        RA = 15 * float(RA[0]) + 15.0 * float(RA[1]) /60.0 + 15 * float(RA[2]) / 3600.0
        DEC = args[2].split(':')
        DEC = math.copysign(abs(float(DEC[0])) + float(DEC[1]) / 60.0 + float(DEC[2]) / 3600.0, float(DEC[0]))
        # пусть тип -- spiral & ClockWise
        P_EL = float(args[4])
        P_CW = float(args[5])
        P_ACW = float(args[6])
        P_EDGE = float(args[7])
        # SPIRAL = int(args[13])
        # ELLIPTICAL = int(args[14])
        # UNCERTAIN = int(args[15])
        if (P_EDGE == 0) and ((P_CW > 0.3) and (P_ACW == 0)):
            pic = 'http://skyservice.pha.jhu.edu/DR13/ImgCutout/getjpeg.aspx?'
            pic += 'ra=%s&dec=%s&scale=0.2&width=600&height=600&opt=G' % (str(RA), str(DEC))
            urllib.request.urlretrieve(pic, './pictures/%i.jpg' % (OBJID))
            with open('./pictures/info.dat', 'a') as inf:
                inf.write('%i    %20.10f    %20.10f\n' % (OBJID, RA, DEC))

n_part = 5
parts = np.linspace(0, len(table), 5, dtype=np.int32)
threads = []
for i in range(n_part - 1):
    start = parts[i]
    finish = parts[i + 1]
    t = threading.Thread(target=foo, args=(table[start:finish], ))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
# print(t)
