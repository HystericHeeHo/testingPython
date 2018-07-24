age = int(input('How old are you?: '))
retirement = abs(age - 65)

if retirement < 10:
    print("You get to retire soon.")
else:
    print("You have a long time until you can retire!")