qs = [11, 22, 7, 9, 13, 5,]

while True:
    
    a = input('Guess a Number or type q to quit: ')
    if a == 'q':
        break
    try:  
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
    if a in qs: 
        print('You\'ve guessed correctly')
    else: 
        print('You\'ve guessed incorrectly')