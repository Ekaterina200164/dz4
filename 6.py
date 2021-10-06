import time
import datetime

def decorator(way):
    def dec(foo):
        def wrapper(*args, **kwargs): 
            now1 = datetime.datetime.now()
            foo(*args, **kwargs)
            now2 = datetime.datetime.now()
            strt  = time.time()
            foo(*args, **kwargs)
            stp  = time.time()         
            t = strt - stp
            ret = foo(*args, **kwargs)
            if ret is None:
                ret = '-'
            with open('answ6.txt', 'w') as file:
                file.write('Время вызова функции: {} \nВходящие аргументы: {} \nОтвет return: {} \nВремя завершения работы функции: {} \nВремя работы функции: {}'.format(now1, args, ret, now2, t) + '\n')

        return wrapper
    return dec

@decorator('answ6.txt')
def foo(x, y, z):
    return max(x, y, z)
foo(1, 2, 3)
