''' Написать программу, которая принимает на вход путь до директории и строку и выводит список файлов, 
которые содержат в себе эту строку. Для каждого найденного файла вывод должен содержать имя файла, номер
строки, в которой найдена искомая строка и саму эту строку. Должна корректно отрабатываться возможность 
того, что в файле есть несколько строк, удовлетворяющих поисковому запросу. '''

import os # работа с путями (os.path -- вложенный в os модуль)
from pathlib import Path
import sys

args = sys.argv

route = Path(args[1])
string = ''
for i in range(2, len(args)):
    string += str(args[i]) + ' '
string = string.rstrip()

def find_files(route, string):
    ls = os.listdir(route)
    res = []
    for l in ls:
        path_to_l = route / Path(l)
        with open(path_to_l, 'r') as file:
            content = file.readlines()
            for s, line in enumerate(content):
                # print(string, line)
                if string in line:
                    res.append([os.path.basename(path_to_l), str(s), line.rstrip()])
    return res

res = find_files(route, string)
for r in res:
    print(' '.join(r))
    # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')


