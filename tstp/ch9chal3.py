import os 
import csv

favmovies1 = ['Top Gun', 'Risky Business', 'Minority Report']
favmovies2 = [' Titanic', 'Revenant', 'Inception']
favmovies3 = ['Training Day', 'Man on Fire', 'Flight']
with open("hello.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow([favmovies1, favmovies2, favmovies3])