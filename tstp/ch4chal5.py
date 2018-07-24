def fltconverter(x):
    try:
        return float(x)    
    except: (ZeroDivisionError, ValueError)
    print('Invalid input')
    
x = fltconverter(input('Please enter a number: ')) 
print(x)