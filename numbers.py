#prints opening statement
print("Python is Cool!" + " " "Watch this!")
#User chooses a number.
userNumber = input("Pick an age between 1 and 25. ")
if int(userNumber) > 25:
    print("Well, You're no longer in your prime.")
elif int(userNumber) == 25:
    print("wow you're 25? You don't look a day over 18")
elif int(userNumber) == 23:
    print("No one's gonna like you when you're 23")
elif int(userNumber) < 25:
    print("You're like almost a real adult")
elif int(userNumber) >= 10:
    print("You've still got a ways to go kid.")
elif int(userNumber) < 10:
    print("Are you even old enough to know how to take this?")
else:
    print("You have entered an invalid response, Please Try Again.")
