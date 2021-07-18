import os
import discord
from discord.ext import commands

## TOKEN = ODY2MTcyNDY2ODUzMTgzNDg4.YPOr-A.EjpQDPhmn0lkds4rwpaT4bZYSCM

TOKEN = "ODY2MTcyNDY2ODUzMTgzNDg4.YPOr-A.EjpQDPhmn0lkds4rwpaT4bZYSCM"
GUILD = "Dungeonesis"
ID = "317630542407270401"

client = commands.Bot(command_prefix = "!")
# i am not going to run client cause i want to run in voicecontroller.py

@client.event
async def on_ready():
    print("Logged on as {} to {} as guild!".format(client.user, client.guilds[0]))
    channel = client.get_channel(id=483622519304355850)
    #await channel.send("I am back.")
@client.event
async def on_message(message):
    await client.process_commands(message)
    text_channels = ["bot"]
    if str(message.channel) in text_channels:
        if message.content.find("!wakeup") != -1:
            await message.channel.send("I am alive.")
@client.command(pass_context = True)
async def esva(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel.")
@client.command(pass_context = True)
async def exit(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel.")
def get_TOKEN():
    return TOKEN

def get_GUILD():
    return GUILD

client.run(TOKEN)
