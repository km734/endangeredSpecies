import json

file = open('speciesHabitat.json', 'r')
listHabitatOld = eval(file.read())

file = open('speciesThreatsCount.json', 'r')
listThreatOld = eval(file.read())


listHabitat = {}
listThreat = {}

i = 0

# Parsing Habitats

    # for key, value in listHabitatOld.items():
    #     for habitat in value:
    #         if(habitat in listHabitat):
    #             listHabitat[habitat].append(key)
    #         else:
    #             ids = []
    #             ids.append(key)
    #             listHabitat[habitat] = ids
    #
    #     i = i + 1
    #     print(str(i) + "   " + str(listHabitat))
    #
    # file = open('habitatSpecies.json', 'w')
    # json.dump(listHabitat, file)

# Parsing Threats
    #
    # for cat, threats in listThreatOld.items():
    #     if((cat == 'CR') | (cat == 'EN') | (cat == 'VU')):
    #         for key, value in threats.items():
    #             for threat in value:
    #                 if(threat in listThreat):
    #                     listThreat[threat].append(key)
    #                 else:
    #                     ids = []
    #                     ids.append(key)
    #                     listThreat[threat] = ids
    #
    #             i = i + 1
    #             print(str(i) + "   " + str(listThreat))
    #
    # file = open('threatSpecies.json', 'w')
    # json.dump(listThreat, file)

# Parsing IDs

addedCodes = {}
for cat, threats in listThreatOld.items():
    if((cat == 'CR') | (cat == 'EN') | (cat == 'VU')):
        for key, value in threats.items():
            if(key not in addedCodes):
                addedCodes[key] = cat

            i = i + 1

        print(str(i) + "   " + str(addedCodes))

#file = open('totalSpeciesThreat.json', 'w')
#json.dump(addedCodes, file)

file = open('speciesCategoriesThreat.json', 'w')
json.dump(addedCodes, file)