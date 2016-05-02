import requests
import json

listTotalSpecies = []

file = open('speciesThreatsCount.json', 'r')
listThreat = eval(file.read())

file = open('totalSpeciesThreat.json', 'r')
listTotalSpecies = eval(file.read())

file = open('speciesCategoriesThreat.json', 'r')
listCategories = json.loads(file.read())

listSpecies = {}

#Retrieve Species by Habitat

i = 0

for x in listTotalSpecies:
    category = listCategories[x]

    threats = listThreat[category][x]
    for s in threats:
        code = s
        if(code in listSpecies):
            if(category in listSpecies[code]):
                listSpecies[code][category] = listSpecies[code][category] + 1
            else:
                listSpecies[code][category] = 1
        else:
            cat = {category: 1}
            listSpecies[code] = cat

    i = i+1
    print(str(i) + " " + str(listSpecies))

#print(listHabitat)

file = open('threat.json', 'w')
json.dump(listSpecies, file)