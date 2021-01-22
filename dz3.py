def max_sum(a, b, c):
    sum_numb = 0
    if a > b and b > c:
        sum_numb = a + b
    if a > b and b < c:
        sum_numb = a + c
    if a < b and b < c:
        sum_numb = b + c
    if a < b and b > c:
        if a > c:
            sum_numb = a + b
        else:
            sum_numb = b + c
    return sum_numb

print(f'Sum of two maximum numbers = {max_sum(3, 6, 9)}')