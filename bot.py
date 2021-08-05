import discord
from discord.ext.commands.core import command
from discord.flags import Intents
from discord_slash import SlashCommand
import json
import logging

"""
    Setting up dictionaries from JSON files.
"""

with open("secret.json") as f:
  secrets = json.load(f)

with open("conf.json") as f:
  config = json.load(f)

with open("cards.json") as f:
  cards = json.load(f)
"""
    Setting up discord bot and slash commands
"""

description = '''An unofficial Cards Against Humanity bot for when you and your friends want to lower your expectations.

Written by @TheSlowHipster https://github.com/TheSlowHipster/CardsBot
'''

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
  '''
    Update guild lists in secrets on startup
  '''
  for guild in client.guilds:
    if guild.id not in secrets["Guilds"]:
      secrets["Guilds"].append(guild.id)
  with open("secrets.json", 'w') as f:
    json.dump(secrets, f, indent=4)
  print("Ready!")

'''
  When a guild is joined add it's id to secrets.
'''
@client.event
async def on_guild_join(guild):
  if guild.id not in secrets["Guilds"]:
    secrets["Guilds"].append(guild.id)
    with open("secrets.json", 'w') as f:
      json.dump(secrets, f, indent=4)

client.run(secrets["TOKEN"])