x = 10
lst = [1, 2]

def f(a, b):
    global x
    x = x + 1
    a = a + 1
    b.append(3)
    b = [99]
    b.append(4)
    return a, b

y = x
result = f(y, lst)
print(x, y, lst, result)