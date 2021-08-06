import discord
import json
import random
import logging
from discord import embeds
from discord import colour
from discord.ext import commands

"""
    Setting up logging
"""

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='UTF-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

"""
    Setting up dictionaries from JSON files.
"""

with open("secrets.json") as f:
  secrets = json.load(f)

with open("conf.json") as f:
  config = json.load(f)

with open("cards-full.json") as f:
  cards = json.load(f)

decklist = {}

for deck in cards:
  decklist[deck["name"]] = {
                            "white":len(deck["white"]),
                            "black":len(deck["black"]),
                            "official":deck["official"]
                           }

"""
    Setting up discord bot and slash commands
"""

description = '''An unofficial Cards Against Humanity bot for when you and your friends want to lower your expectations.

Written by @TheSlowHipster https://github.com/TheSlowHipster/CardsBot
'''

bot = commands.Bot(command_prefix=config["Prefix"], description=description, intents=discord.Intents.default())


@bot.event
async def on_ready():
  '''
    Update guild lists in secrets on startup
  '''
  for guild in bot.guilds:
    if guild.id not in secrets["Guilds"]:
      secrets["Guilds"].append(guild.id)
  with open("secrets.json", 'w') as f:
    json.dump(secrets, f, indent=4)
  print("Ready!")

'''
  When a guild is joined add it's id to secrets.
'''
@bot.event
async def on_guild_join(guild):
  if guild.id not in secrets["Guilds"]:
    secrets["Guilds"].append(guild.id)
    with open("secrets.json", 'w') as f:
      json.dump(secrets, f, indent=4)

@bot.command()
async def ping(ctx):
  await ctx.send(f"PONG! {round(bot.latency*1000)}ms")

@bot.command(aliases=["list","List","decks","Decks","listdecks","ListDecks","Listdecks","ld"])
async def listDecks(ctx):
  count = 0
  embed = discord.Embed()
  decks = list(decklist.keys())
  while count < len(decks):
    max = 50
    if count + max >= len(decklist):
      max = len(decklist)-count

    embed = discord.Embed(title="Available Decks",
                          description=f'Decks {count+1} to {count+max}',
                          color=0xdedbef)
    for i in range(max):
      if count >= len(decks):
        break
      deck = decks[count]
      embed.add_field(name=deck, value=f'White Cards: {decklist[deck]["white"]}\nBlack Cards: {decklist[deck]["black"]}\nOfficial: {":white_check_mark:" if decklist[deck]["official"] is True else ":no_entry_sign:"}')
      count += 1
    await ctx.author.send(embed=embed)




bot.run(secrets["TOKEN"])