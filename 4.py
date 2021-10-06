l = list(map(int, input().split()))
def even(x):
    k = 0
    for i in l:
        if i % 2 == 0:
            k += 1
    return k 
def decorator(foo):
    def wrapper(x):
        if even(x) == 0:
            return 'нет'
        elif even(x) > 10:
            return 'очень много'
        else:
            return even(x)
    return wrapper
print(decorator(even)(l))
