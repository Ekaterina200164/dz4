def swap(foo):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        foo(*args, **kwargs)
    return wrapper

#Примеры работы декоратора
@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res
@swap
def eq(x, y, z, show = False):
    if show:
        print(x, y, z)
    return(x, y, z)

div(2, 4, show=True)
eq(4, 2, 1, show = True)
