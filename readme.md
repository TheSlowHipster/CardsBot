# Quickstart

## I don't want to host this myself

Click [HERE](https://discord.com/api/oauth2/authorize?client_id=872969311172579379&permissions=51539668032&scope=bot%20applications.commands) to add this bot to your server!

## I want to host this myself

Clone the repository and run the following commands:

To install `discord.py` run:

```bash
python3 -m pip install -U discord.py
```

To install the slash commands run:

```bash
pip install -U discord-py-slash-command
```
Then use your favorite editor to set up the `secrets.json` file. Required fields are:

```json
{
  "TOKEN": "TOKEN_ID_FROM_DISCORD_GOES_HERE",
  "Guilds":[]
}
```

To get your bot token follow [these instructions](https://discordpy.readthedocs.io/en/latest/discord.html) from [Discord.py](https://discordpy.readthedocs.io/en/latest/index.html).