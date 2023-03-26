''' При помощи автоматизированного доступа к базе данных HyperLEDA построить диаграмму 
Талли-Фишера. Адрес базы: http://leda.univ-lyon1.fr/fullsql.html, по нему нужно отправлять 
SQL-запрос.
Скрипт получает на вход ограничение по bt, формирует SQL запрос, отправляет его на сайт HyperLEDA,
получает список галактик с таким bt у которых есть Vrot и модуль расстояния (modbest) и строит 
по ним диаграмму Талли---Фишера (более яркие галактики быстрее вращаются, т.к. они более тяжелые).
bt -- видимая звездная величина, надо перейти к абсолютной, для этого есть скорость (Vrot). 
Нужно построить светимость против логарифма скорости с учетом расстояния (т.е. по горизонтали 
bt-modbest, по вертикали log10(Vrot). '''

import requests as req
from numpy import loadtxt, ndarray
from math import log10
import matplotlib.pyplot as plt

m = input('Введите максимальную звездную величину: ')
if int(m) <= 0:
    print('Таких галактик нет.')
else:
    url = 'http://leda.univ-lyon1.fr/fG.cgi?n=meandata&c=o&of=1,leda,simbad&nra=l&nakd=1&d=objname\
        %2C%20bt%2C%20vrot%2C%20modbest&sql=bt%3C'+m+'%20and%20vrot%20IS%20NOT%20NULL%20and%20\
            modbest%20IS%20NOT%20NULL&ob=&a=t'
    with open('galaxies.txt', 'w') as ouf:
        ouf.write(str(req.get(url).text))
    galaxies = loadtxt('galaxies.txt', comments='#', usecols=(1,2,3))
    V_rot = []
    M = []
    if isinstance(galaxies[0], ndarray):
        for i in range(len(galaxies)):
            V_rot.append(log10(galaxies[i][1]))
            M.append(galaxies[i][0] - galaxies[i][2])
    else: # если в galaxies только одна галактика удовлетворяет запросу (например, когда m < 1)
        V_rot.append(log10(galaxies[1]))
        M.append(galaxies[0] - galaxies[2])

    plt.title('Диаграмма Талли—Фишера')
    plt.xlabel('$M = m - \mu$')
    plt.ylabel('$\log_{10}{(V_{rot})}$')
    plt.plot(M, V_rot, 'o', markersize=0.5, color='#eaf7fb')
    plt.axes().set_facecolor('#0c0d29')
    plt.legend(['galaxies'], loc='best')
    plt.show()
