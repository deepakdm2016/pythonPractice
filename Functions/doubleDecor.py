def decor(fun):
    def inner():
        res = fun()
        return res*2
    return inner

@decor
def num():
    return 5

print(num())