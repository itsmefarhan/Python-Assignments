# Check prime number

number = int(input('Enter a number to check whether it is prime or not: '))

for num in range(2, number):
    if number % num == 0:
        print(number, 'is not a prime number')
        break
else:
    print(number, 'is a prime number')
