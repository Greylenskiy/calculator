def calculate(num_1, num_2, oper):
    if oper == '+':
        result = num_1 + num_2
    elif oper == '-':
        result = num_1 - num_2
    elif oper == '*':
        result = num_1 * num_2
    elif oper == '/':
        if num_2 == 0:
            result = 'На 0 делить нельзя!'
        elif num_2 != 0:
            result = num_1 / num_2
    else:
        result = 'Неизвестная операция'

    return result


print(calculate(5, 0, ''))
