my_dict = {
    'height': "5'10\"", 
    'color': 'Black',
    'author': 'George Orwell',
    'game': 'Shin Megami Tensei',
    'band': 'Coheed and Cambria'
}

key = input('What do you want to know? I\'ll tell you all my favorites.(Please choose one of the following: height, color, author, game, or band): ')
print('What is your favorite ' + key +'?')
print(my_dict.get(key))