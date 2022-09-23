#!/usr/bin/python3

seriesList = ["Dexter", "Ozark", "Better Call Sall","One Piece"]
#for
n = 1
for i in seriesList:
    print(f'{n}.{i}')
    n+=1
#enumerate() method
favoriteFruit = ["cherry","banana","apple","watermelom","lemon","passiflora"]

""" for j in enumerate(favoriteFruit):
    print(j) """

for j,fruit in enumerate(favoriteFruit):
    j+=1
    print(f'{j}.{fruit}')    