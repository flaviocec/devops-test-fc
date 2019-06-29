# -*- coding: utf-8 -*-
"""
@author: fcecca
"""

import requests
import json

abvFilter = input("Filter beers by ABV greater than - Please enter an ABV value e.g. 5.6 \n")

response = requests.get("https://api.punkapi.com/v2/beers")

if response.ok :
    beerData = json.loads(response.content)
    
    #output dictionary containing Name as key and ABV as value needed for filtering and sorting
    beerDict ={}
    
    for key in beerData:
        #Filter by ABV input
        if key ['abv'] > float(abvFilter):
            #Add Name and ABV to filtered dictionary, safe because name is unique.
            beerDict.update({key['name']:key ['abv']})
  
    #sort the dictonary by abv x[1]
    sortedBeerData = sorted(beerDict.items(), key=lambda x :x[1])
    for sortedKey in sortedBeerData:
        print (sortedKey[0]+",{}".format(sortedKey[1]))
   
else:
   print("Error calling API " + response.status_code)
   