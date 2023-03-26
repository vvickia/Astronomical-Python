'''                             Conway's Game of Life
Правила:
○ Место действия — размеченная на клетки поверхность (здесь ограниченная плоскость).
○ Каждая клетка имеет два состояния: «живая» или «мёртвая». Клетка имеет восемь соседей.
○ Распределение «живых» клеток в начале игры называется первым поколением. Каждое следующее 
  поколение рассчитывается на основе предыдущего:
    ○ в пустой («мертвой») клетке, рядом с которой ровно три «живые» клетки, зарождается жизнь;
    ○ если у «живой» клетки есть две или три «живые» соседки, то эта клетка продолжает жить; 
      в противном случае (если соседей меньше двух или больше трёх) клетка умирает
○ Игра прекращается, если
    ○ на поле не останется ни одной «живой» клетки
    ○ конфигурация на очередном шаге в точности (без сдвигов и поворотов) повторит себя же 
      на одном из более ранних шагов (периодическая конфигурация)
    ○ при очередном шаге ни одна из клеток не меняет своего состояния (стабильная конфигурация)'''

import numpy as np

n = 10
# 0 means dead (False), 1 means alive (True)
grid = np.array([[np.random.choice(2, p=[0.7, 0.3]) for i in range(n)] for j in range(n)], dtype=np.int32)
configuration = []
configuration.append(grid)
print('1 generation:\n', grid)

sys = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
# соседями крайних клеток являются клетки с противоположной стороны
def get_num_of_alive_neighbors(pos: list, sys=sys):
    num = 0
    for i in sys:
        if grid[(pos[0] + i[0]) % len(grid)][(pos[1] + i[1]) % len(grid[0])]:
            num += 1
    return num

lattice = np.zeros((n, n), dtype=np.int32)
flag1, flag2 = False, False
count = 1
while True:
    for i in range(n):
        for j in range(n):
            if not(grid[i][j]) and (get_num_of_alive_neighbors([i, j]) == 3):
                lattice[i][j] = 1
            if grid[i][j]:
                if get_num_of_alive_neighbors([i, j]) not in (2, 3):
                    lattice[i][j] = 0
                else:
                    continue
    grid = lattice
    count += 1
    print('%i generation:\n' % count, grid)
    for config in configuration:
        if np.array_equal(grid, config):
            flag1 = True
            break
    if flag1:
        print('break1')
        break
    configuration.append(grid)

    s = 0
    for i in range(n):
        for j in range(n):
            s += grid[i][j]
        if s == 0:
            flag2 = True
            break
    if flag2:
        print('break2')
        break    
