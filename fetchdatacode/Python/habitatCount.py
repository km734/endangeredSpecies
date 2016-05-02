import requests
import json

listTotalSpecies = []

file = open('totalSpecies.json', 'r')
listTotalSpecies = file.read().split(', ')

file = open('speciesCategories.json', 'r')
listCategories = json.loads(file.read())

print(len(listTotalSpecies))

listHabitat = {}

#Retrieve Species by Habitat

i = 0

for x in listTotalSpecies:
    url = 'http://apiv3.iucnredlist.org/api/v3/habitats/species/id/'+ str(x) +'?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
    response = requests.get(url)
    j = response.json()

    category = listCategories[x]

    addedCodes = []
    if(len(j['result']) > 0):
        for s in (j['result']):
            code = s['code'].split(".")
            code = code[0]
            if(code not in addedCodes):
                addedCodes.append(code)
                if(code in listHabitat):
                    if(category in listHabitat[code]):
                        listHabitat[code][category] = listHabitat[code][category] + 1
                    else:
                        listHabitat[code][category] = 1
                else:
                    cat = {category: 1}
                    listHabitat[code] = cat

    i = i+1
    print(str(i) + " " + str(listHabitat))

#print(listHabitat)

file = open('habitat.json', 'w')
json.dump(listHabitat, file)