import random
import time

class Lock:
    def __init__(self, real_pass):
        # Constructor
        self.__real_pass = real_pass # сделаем переменную приватной, чтобы нельзя было обратиться 
                                     # к ней вне объекта
    def unlock(self, inp):
        # принимает строку с паролем на вход и возвращает: строку "sucess", если пароль верный; 
        # строку "wrong length", если пароль неверной длины; список, содержащий позиции, на которых 
        # в заданном пароле стоят верные цифры (если верный пароль 14256, а заданный -- 15209, 
        # то метод должен вернуть список [0, 2])
        if self.__real_pass == inp:
            return 'success'
        elif len(self.__real_pass) != len(inp):
            return 'wrong length'
        else:
            min_len = min(len(self.__real_pass), len(inp))
            k = []
            for i in range(min_len):
                if self.__real_pass[i] == inp[i]:
                    k.append(i)
            return k

''' Написать функцию, которая пытается подобрать пароль, вызывая метод unlock объекта-замка и используя 
его подсказки. Изначально функция не знает ни длины пароля, ни его значения. Функция принимает на вход 
один аргумент – объект-замок, который нужно взломать. Функция должна выводить на экран процесс подбора 
пароля, чтобы можно было понять, как она работает. '''

def get_pw(lockobj):
    guess = ''
    is_right_lenght = False
    while True:
        time.sleep(.3)
        if not is_right_lenght:
            guess += str(random.randint(0, 9))
            print(guess)
            hint = lockobj.unlock(guess)
            if hint == 'wrong length':
                continue
            elif isinstance(hint, list):
                is_right_lenght = True
        else:
            hint = lockobj.unlock(guess)
            if hint == 'success' : break
            length = len(guess) # длина пароля
            new_guess = [None for i in range(length)]
            for k in hint:
                new_guess[k] = guess[k]
            for i, symbol in enumerate(new_guess):
                if symbol == None:
                    new_guess[i] = str(random.randint(0, 9))
            guess = ''.join(new_guess)
            print(guess)
    return guess

pw = input('Веведите пароль: ')
lock = Lock(pw)
hacked_pass = get_pw(lock)
print('Ура! Пароль:', hacked_pass)
