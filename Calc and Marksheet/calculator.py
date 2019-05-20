print('\n\t\t***********************************************************************************')
print('\t\t*\t\t\t\tCALCULATOR ASSIGNMENT\t\t\t\t  *')
print('\t\t***********************************************************************************')

num1 = int(input('\t\t\tEnter first number: '))
num2 = int(input('\t\t\tEnter second number: '))
operation = input('\t\t\tEnter desired operation (+, -, *, /, %): ')

if operation == '+':
    result = '\n\t\t\tThe Sum of ' + str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2) + '\n'
    print(result)
elif operation == '-':
    result = '\n\t\t\tThe Substraction of ' + str(num1) + ' - ' + str(num2) + ' = ' + str(num1 - num2) + '\n'
    print(result)
elif operation == '*':
    result = '\n\t\t\tThe Multiplication of ' + str(num1) + ' * ' + str(num2) + ' = ' + str(num1 * num2) + '\n'
    print(result)
elif operation == '/':
    result = '\n\t\t\tThe Division of ' + str(num1) + ' / ' + str(num2) + ' = ' + str(num1 / num2) + '\n'
    print(result)
elif operation == '%':
    result = '\n\t\t\tThe Remainder of ' + str(num1) + ' % ' + str(num2) + ' = ' + str(num1 % num2) + '\n'
    print(result)
else:
    print('\n\t\t\tInvalid operation. Please select any of the following (+, -, *, /, %)') + '\n'