#!/usr/bin/python3

favoriteFruit = ["cherry","banana","apple","watermelom","lemon","passiflora"]

searchFruit = input("Try one fruit: ")

parseSearchFruit = searchFruit.lower()

for i in favoriteFruit:
    if parseSearchFruit == i:
        print((f'{i} is already for you eat.').capitalize())
        break
else:
        print((f'{parseSearchFruit} out of this list').capitalize())