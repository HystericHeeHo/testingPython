#

x = int(input('Please choose a number: '))

if x <= 10: 
    print('Huh. I thought you\'d choose something bigger')
elif x > 10 and x < 25:
    print('I knew you would choose that')
elif x > 25:
    print('That\'s larger than I imagined.')