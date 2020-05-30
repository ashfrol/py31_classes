allowed_operators = ['+', '-', '*', '/']

def polsky_calc(expression):
    operators = []
    for item in expression.split(' '):
        operators.append(item)
    assert operators[0] in allowed_operators, 'Неизвестная операция'
    assert len(operators) == 3, 'Неправильное количество аргументов'
    if operators[0] == '+':
        try:
            result = int(operators[1]) + int(operators[2])
            print(result)
        except ValueError as e2:
            print(f'Строки складывать нельзя! текст исключения: {e2}')
    elif operators[0] == '-':
        try:
            result = int(operators[1]) - int(operators[2])
            print(result)
        except ValueError as e2:
            print(f'Строки вычитать нельзя! текст исключения: {e2}')
    elif operators[0] == '*':
        try:
            result = int(operators[1]) * int(operators[2])
            print(result)
        except ValueError as e2:
            print(f'Строки умножать нельзя! текст исключения: {e2}')
    elif operators[0] == '/':
        try:
            result = int(operators[1]) / int(operators[2])
            print(result)
        except ZeroDivisionError as e1:
            print(f'На ноль делить нельзя! текст исключения: {e1}')
        except ValueError as e2:
            print(f'Строки делить нельзя! текст исключения: {e2}')
    # else:
    #     print('Неизвестная операция')

expression = input()
polsky_calc(expression)
