# ITP Week 4 Day 2 Exercise

#Today we will pull information from the Pokemon api, put it into a dictionary, and then put that info into a new Excel file.  We will write the pseudocode as a group in class.  Be sure to follow the pseudocode, break your problems down into smaller pieces, and consult the documentation whenever you get stuck: https://pokeapi.co/api/v2/pokemon

#PSEUDO-CODE:

#GET NAME AND ABILITY FROM API
#PUT INFO IN DICTIONARY
#ADD THE DICTIONARY TO A NEW EXCEL WORKBOOK

#imports:
    #json
    #openpyxl
import requests
import json
import openpyxl
# import pandas as pd

#Input
    #json file from pokemon api
    #workbook
#Assign response to variable
response = requests.get('https://pokeapi.co/api/v2/pokemon')

# print(clean_data)

#Create workbook
    #get workbook from openpy
    #load workbook
    #assign workbook to variable
#Create Worksheet
    #assign sheet to variable
    
wb = openpyxl.load_workbook('/mnt/c/Users/Jeffe/source/codefellows/vetsInTech/itp_week_4/day_2/output.xlsx')
sheet = wb['Sheet1']
# sheet2 = wb['Sheet2']

#Create a dictionary, assign to variable
name_dict = {}
ab_dict = {}

#FUNCTION BODY
    #Convert response to json file
        #clean data(response)
            #json.loads(response.text)
clean_data = json.loads(response.text)
result = clean_data["results"]


name_counter = 0
counter1 = 2
counter2 = 2
# ab_counter = 0
# url_counter = 0
    #Iterate over response
            #variable key = pokemon.name
            #variable value = pokemon.abilites
            #append {key/value} pair to dictionary

for char in result:
  # add individul names to xl
  sheet['A' + str(counter1)] = char['name']
  # add individual names to dic
  name_dict[str(name_counter) + " Name"] = char['name']
  # begin cleaning data for ability url
  url_result = clean_data['results']
  pokemon_url = url_result[name_counter]['url']
  response1 = requests.get(pokemon_url)
  clean_url = json.loads(response1.text)
  ab_result = clean_url['abilities']
  # break the scaffolding down far enough that it reduces errors
  single_ab = ab_result[0]["ability"]
  # add individual ability to xl
#   sheet['B' + str(counter1)] = ab_dict[str(name_counter) + " Ability"] = single_ab["name"]
  # add individual ability to dict
  name_dict[str(name_counter) + " Ability"] = single_ab["name"]
  counter1 += 1
  counter2 += 2
  name_counter += 1

print(name_dict)
print(ab_dict)
    #Iterate over dictionary
        #for each item in dictionary
            #assign dictionary values to rows & cols
                #Write Name to Cell
                #Write Abilities to Cell
# df = pd.DataFrame(data=name_dict, index=[1])

# df = (df.T)

# print(df)

sheet['A1'] = 'Name'
sheet['B1'] = 'Ability'

#Output
    #Workbook
wb.save('/mnt/c/Users/Jeffe/source/codefellows/vetsInTech/itp_week_4/day_2/output.xlsx')




# pokemon = {
#     bulbasour : {
#         "name": "pokemon_name",
#         "abilities": ["ability1", "ability2"]
#     },
#     pikachu : {
#         "name": "pokemon_name",
#         "abilities": ["ability1", "ability2"]
#     }
# }