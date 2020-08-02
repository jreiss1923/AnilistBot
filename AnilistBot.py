import discord
import requests
import time

query = '''
query ($name: String) { # Define which variables will be used in the query (id)
  User (name: $name) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    name
  }
}
'''

# Define our query variables and values that will be used in the query request
variables_pat = {
    'id': 121769
}

variables_hani = {
    'id': 320308
}

variables_phil = {
    'id': 163795
}

variables_alan = {
    'id': 121839
}

variables_ben = {
    'id': 122953
}

variables_zen = {
    'id': 382311
}

variables_me = {
    'id': 323865
}

url = 'https://graphql.anilist.co'

arr_vars = [variables_alan, variables_ben, variables_hani, variables_pat, variables_phil, variables_zen, variables_me]

# Make the HTTP Api request
for variables in arr_vars:
    response = requests.post(url, json={'query': query, 'variables': variables})
    print(response.content)

print(int(time.time()))
