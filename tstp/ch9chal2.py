import os

useranswer = input('Say Something: ')
with open("hello.txt", "w+") as f:
    f.write(useranswer)