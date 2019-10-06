def decor(fun):
    def inner(n):
        res = fun(n)
        return res, "How are you"
    return inner

@decor
def hello(name):
    return "hello "+name

print(hello("Deepak"))