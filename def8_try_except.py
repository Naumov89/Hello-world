
try:
    a = input('Enter first number:')
    b = input('Enter second number:')
    a = int(a)
    b = int(b)
    print (a / b)
except (ZeroDivisionError, ValueError):
    print('Error enter')
    