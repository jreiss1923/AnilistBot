import json
import discord
import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()

client = discord.Client()

url = 'https://graphql.anilist.co'

query = '''
query ($userId: Int, $createdAt_greater: Int) {
  Activity (userId: $userId, createdAt_greater: $createdAt_greater) {
    ... on ListActivity {
        createdAt
        status
        progress
        media {
            title {
                romaji
            }
        }
        user {
            name
        }
    }
  }
}
'''


@client.event
async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(458644594905710595)
    while not client.is_closed():
        curr_time = int(time.time()-3)
        variables_pat = {
            'userId': 121769,
            'createdAt_greater': curr_time
        }

        variables_hani = {
            'userId': 320308,
            'createdAt_greater': curr_time

        }

        variables_phil = {
            'userId': 163795,
            'createdAt_greater': curr_time
        }

        variables_alan = {
            'userId': 121839,
            'createdAt_greater': curr_time
        }

        variables_ben = {
            'userId': 122953,
            'createdAt_greater': curr_time
        }

        variables_zen = {
            'userId': 382311,
            'createdAt_greater': curr_time
        }

        variables_me = {
            'userId': 323865,
            'createdAt_greater': curr_time
        }

        variables_min = {
            'userId': 169966,
            'createdAt_greater': curr_time
        }
        arr_vars = [variables_alan, variables_ben, variables_hani, variables_pat, variables_phil, variables_zen,
                    variables_me, variables_min]
        for variables in arr_vars:
            response = requests.post(url, json={'query': query, 'variables': variables})
            my_json = json.loads(response.content)
            if my_json is not None and my_json["data"]["Activity"] is not None:
                activity = my_json["data"]["Activity"]
                print(activity)
                if activity["progress"] is not None:
                    result_string = activity["user"]["name"] + " " + activity["status"] + " " + activity["progress"] + " of " + activity["media"]["title"]["romaji"]
                    result_embed = discord.Embed(
                        title="New Anilist Post",
                        color=discord.Color(0x039AFF),
                        description=result_string
                    )
                    await channel.send(embed=result_embed)
                else:
                    result_string = activity["user"]["name"] + " " + activity["status"] + " " + activity["media"]["title"]["romaji"]
                    result_embed = discord.Embed(
                        title="New Anilist Post",
                        color=discord.Color(0x039AFF),
                        description=result_string
                    )
                    await channel.send(embed=result_embed)

client.loop.create_task(my_background_task())
client.run(os.getenv("DISCORD_TOKEN"))
