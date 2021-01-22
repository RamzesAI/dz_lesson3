sum_results = 0
while True:
    my_str = input("Enter number: ")
    a = my_str.split()
    result = 0
    for el in a:
        if ord(el[0]) > 47 and ord(el[0]) < 58:
            result = result + int(el)
        else:
            break
    sum_results = sum_results + result
    print(sum_results)
