my_dict = {
    'Coheed' : 'Vic The Butcher',
    'Falloutboy' : '20 Dollar Nose Bleed',
    'Kdot' : 'Sing about me, I\'m dying of thirst.',
    'Nujabes' : 'Imaginary Folklore',
    'Kyle' : 'Ups & Downs'
}
answer = input('Choose one of my favorite artists to learn my favorite song by them: Coheed, Falloutboy, Kdot, Nujabes, or Kyle: ').capitalize()
if answer in my_dict:
    result = my_dict[answer]
    print(result)
else:
    print('That choice is invalid')