import openpyxl
import requests
import json
# make one api cal to retrieve the list of pokemon

####### get first pokemon from the api call
# first_pokemon = json_data['results'][0]

pokemon_list = []

def populate_pokemon(url):
  response  = requests.get(url)
  json_data = json.loads(response.text)
  for each in json_data['results']:
    pokemon_list.append(each)
  if json_data['next'] != None:
    populate_pokemon(json_data['next'])



wb = openpyxl.Workbook()
sheet = wb.active

def make_header():
  sheet['A1'] = "Name"
  sheet['B1'] = "Abilities"

def write_rows(row_num, name, abilities):
  sheet["A" + str(row_num)] = name
  sheet['B' + str(row_num)] = abilities

def stringify_abilities(abilities_list):
  result_string = ''
  for ability in abilities_list:
    result_string += ability['ability']['name'] + " "
  return result_string

def retrieve_abilities(url):
  abil_resp = requests.get(url)
  abil_json_data = json.loads(abil_resp.text)
  return abil_json_data['abilities']

def populate_data(pokemons):
  for (row_num, each_pokemon) in enumerate(pokemons, start=2):
    just_abil_list = retrieve_abilities(each_pokemon['url'])
    abil_string = stringify_abilities(just_abil_list)
    write_rows(row_num, each_pokemon['name'], abil_string)


make_header()
all_pokemon = populate_pokemon('https://pokeapi.co/api/v2/pokemon')
populate_data(pokemon_list)
wb.save('/mnt/c/Users/Jeffe/source/codefellows/vetsInTech/itp_week_4/day_2/output.xlsx')



# sheet['A1'] = first_pokemon['name']
# sheet['B1'] = abil_string

# append to a list thats going to hold all of the pokemon dictionaries with name and urls

#  iterate through eh list of pokemons
#  make subsequent api calls to retrieve abilities list

#### get the abilities for the first_pokemon

# abilities_response = requests.get(first_pokemon['url'])
# abilities_json_data = json.loads(abilities_response.text)
# just_abilities_of_first_pokemon = abilities_json_data['abilities']



#  tranform abilities list in an excel compatible format

######### transform or stringify the abilities together
# abilities_string = ""
# for each_ability in just_abilities_of_first_pokemon:
#   abilities_string += each_ability['ability']['name'] + ' '

# print(abilities_string)
# write to excel

