import requests
import json

listTotalSpecies = []

file = open('totalSpecies.json', 'r')
listTotalSpecies = file.read().split(', ')

file = open('speciesCategories.json', 'r')
listCategories = json.loads(file.read())

print(len(listTotalSpecies))

listspecies = {}

#Retrieve Species by Habitat

i = 9600

for x in range(9600, 24409):
    url = 'http://apiv3.iucnredlist.org/api/v3/habitats/species/id/'+ str(listTotalSpecies[x]) +'?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
    response = requests.get(url)
    j = response.json()

    category = listCategories[listTotalSpecies[x]]

    addedCodes = []
    if(len(j['result']) > 0):
        for s in (j['result']):
            code = s['code'].split(".")
            code = code[0]
            if(code not in addedCodes):
                addedCodes.append(code)

        listspecies[listTotalSpecies[x]] = addedCodes


    print(str(i) + " " + str(listspecies))
    i = i+1


file = open('listhabitat.json', 'w')
json.dump(listspecies, file)