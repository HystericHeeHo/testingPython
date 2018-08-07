import os 
import csv

favmovies = [['Top Gun', 'Risky Business', 'Minority Report'], ['Titanic', 'Revenant', 'Inception'], ['Training Day', 'Man on Fire', 'Flight']]
with open("hello.csv", "w") as f:
    w = csv.writer(f, delimiter=',')
    for movie_list in favmovies:
        w.writerow(movie_list)