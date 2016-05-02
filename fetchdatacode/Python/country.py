from bs4 import BeautifulSoup
import requests
import json
import math
import time
import calendar


# Initialize variables

listCountries = []
listSpeciesByCountry = []

listTotalSpecies = []

listCategory = {}

# Retrieve Countries

url = 'http://apiv3.iucnredlist.org/api/v3/country/list?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
response = requests.get(url)
j = response.json()

for x in (j['results']):
    listCountries.append(x['isocode'])


# Retrieve Species by country

for x in listCountries:
    url = 'http://apiv3.iucnredlist.org/api/v3/country/getspecies/'+ str(x) +'?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
    response = requests.get(url)
    j = response.json()

    listSpecies = []
    for s in (j['result']):
        if((s['category'] == 'CR') | (s['category'] == 'EN') | (s['category'] == 'VU')):
            listSpecies.append(s)

            # Add species id to list with all species
            if (s['taxonid']) not in listTotalSpecies:
                listTotalSpecies.append(s['taxonid'])
                listCategory[s['taxonid']] = s['category']


    country = {}
    country['result'] = listSpecies
    country['count'] = len(listSpecies)
    country['country'] = x

    print(country)

    listSpeciesByCountry.append(country)

#file = open('countries.json', 'w')
#json.dump(listSpeciesByCountry, file)

#file = open('totalSpecies.json', 'w')
#json.dump(listTotalSpecies, file)

file = open('speciesCategories.json', 'w')
json.dump(listCategory, file)





