#TODO: APIs
import requests

# response = requests.get('https://oim.108122.xyz/words/random')
# print(response.json())   # a random word!

response = requests.get('https://oim.108122.xyz/mass', 
                        headers={"X-Token": "wahwah"})
data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

# print(len(data))
# print(data.keys())
# print(type(data["data"])) #Do these three lines to explore the data

towns = data["data"]

#I want to sort towns by population, but how do I do that? (Hint: sorted() only works on keys, but we want to sort by values)
towns = data["data"]
print(towns[1]) #This is a dictionary, so we can use .items()
#I need to sort by population, so I need to check the population value in the dictionary, but how do I do that? (Hint: Use a function that checks the population value in the dictionary)
def sort_by_population(t):
    return t["population"]

for town in towns:
    print(sorted(town.items(), key=sort_by_population))


