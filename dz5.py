sum_results = 0
my_str = None
while my_str != 'q':
    my_str = input("Enter number: ")
    separate_str = my_str.split()
    result = 0
    for el in separate_str:
        if el.isdigit():
            result = result + int(el)
        else:
            break
    sum_results = sum_results + result
    print(sum_results)