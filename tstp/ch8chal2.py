import cubed

x = input('Please Choose a number: ')

try:
    cubed.cubing(x)
except ValueError:
    print('Please Choose a number.')
