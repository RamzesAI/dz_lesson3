def my_func(x, y):
    y = abs(y)
    result = 1
    for i in range(1, y +1):
        result = result*(1 / x)
    return round(result, 6)
print(my_func(7, -3))