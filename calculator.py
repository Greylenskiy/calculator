num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
oper = input('Что хотите сделать? ')
if oper == '+':
    result = num_1 + num_2
elif oper == '-':
    result = num_1 - num_2
elif oper == '*':
    result = num_1 * num_2
elif oper == '/':
    if num_2 == 0:
        result = 'На ноль нельзя делить!'
    if num_2 != 0:
        result = num_1 / num_2
else:
    result = 'Неизвестная операция'
print(result)
