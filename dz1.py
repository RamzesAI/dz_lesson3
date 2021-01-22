def num_division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Division by zero')
        return 'Need a positive number'

print('You need enter positive integer number')

a = int(input('Enter divisible:\n>>>'))
b = int(input('Enter divider:\n>>>'))

result = (num_division(a, b))
print(f'Result of runing num_division func: {result}')
