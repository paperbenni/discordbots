#!/usr/bin/env python

import discord
import os
import re
import hidad
import creeper


def getvar(string, defaultstr='none'):
    sstring = str(string)
    if os.path.exists('.' + sstring.lower()):
        outstring = open('.' + sstring, 'r').read()
        return outstring
    else:
        if sstring.upper() in os.environ.keys():
            return os.environ[sstring.upper()]
        else:
            return defaultstr


discordtoken = getvar('discord')
print(discordtoken)
client = discord.Client()

parserlist = []
parserlist.append(hidad.replydad)
parserlist.append(creeper.creeper)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for i in parserlist:
        response = i(message.content, message.channel.id)
        if response:
            await message.channel.send(response)

client.run(discordtoken)
