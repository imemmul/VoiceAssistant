from ntpath import join
import os
from types import coroutine
import discord
from discord.ext import commands
from discord.ext.commands.core import command
import asyncio
import time
from threading import Thread

TOKEN = "ODY2MTcyNDY2ODUzMTgzNDg4.YPOr-A.EjpQDPhmn0lkds4rwpaT4bZYSCM"
GUILD = "Dungeonesis"
ID = "317630542407270401"

class My_Discord_Bot():
    def __init__(self):
        self.client = commands.Bot(command_prefix = "!")
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)
    def run(self, TOKEN):
        self.client.run(TOKEN)
    async def on_ready(self):
        print("Logged on as {} to {} as guild!".format(self.client.user, self.client.guilds[0]))
        channel = self.client.get_channel(id=483622519304355850)
        #await channel.send("I am back.")
    async def on_message(self, message):
        await self.client.process_commands(message)
        text_channels = ["bot"]
        if str(message.channel) in text_channels:
            if message.content.find("!wakeup") != -1:
                await message.channel.send("I am alive.")
    async def join_channel(self):
        print("I AM INSIDE OF THE JOIN")
        channel = self.client.get_channel(id=484044934924599306)
        await channel.connect()
    async def exit_channel(self):
        channel = self.client.get_channel(id=484044934924599306)
        await channel.disconnect()





