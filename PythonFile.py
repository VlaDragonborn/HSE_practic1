print('Python code')
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
operation = input("Введите оператор: ")
if operation == '+':
    print(number1, '+', number2, '=',  number1 + number2)
elif operation == '-':
    print(number1, '-', number2, '=',  number1 - number2)
elif operation == '*':
    print(number1, '*', number2, '=',  number1 * number2)
elif operation == '/':
    print(number1, '/', number2, '=',  number1 / number2)

