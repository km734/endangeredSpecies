import requests
import json

file = open('habitatSpecies.json', 'r')
listHabitat = eval(file.read())

file = open('threatSpecies.json', 'r')
listThreat = eval(file.read())

listTotal = {}

totalCount = 0

for habitat, valuesH in listHabitat.items():
    for threat, valuesT in listThreat.items():
        total = len(set(valuesH).intersection(set(valuesT)))

        totalCount = totalCount + total

        if(habitat in listTotal):
            listTotal[habitat][threat] = total
        else:
            listTotal[habitat] = {threat: total}

    print(listTotal)

print(totalCount)

file = open('threatHabitat.json', 'w')
json.dump(listTotal, file)
