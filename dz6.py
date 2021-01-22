def int_func(my_text):
    my_text = my_text.split()
    new_list = []
    for el in my_text:
        len_text = len(el)
        first_letter = el[:1]
        other_letters = el[1:len_text]
        up_lt = ord(first_letter) - 32
        first_letter = chr(up_lt)
        result = first_letter + other_letters
        new_list.append(result)
    return (' '.join(new_list))

print(int_func('function is working great'))
