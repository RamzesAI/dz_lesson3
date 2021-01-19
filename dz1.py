def num_division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Division by zero')
        return 'Need a positive number'

print('You need positive integer number')

a = int(input('Enter divisible:\n>>>'))
b = int(input('Enter divider:\n>>>'))

result = int(round((num_division(a, b)), 2))
print(f'Result of runing num_division func: {result}')