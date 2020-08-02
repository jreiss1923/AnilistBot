import discord
import requests

query = '''
query ($name: String) { # Define which variables will be used in the query (id)
  User (name: $name) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    name
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'name': "patrui"
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.content)