# bot.py
import os
import discord
import random
import tkinter as tk
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
window = tk.Tk()

with open('nameList.txt', 'r') as n:
    nameList = [line.strip() for line in n]


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    thing = message.content.lower()
    if message.channel.id == '502943665480531972':
        return
    if 'nigger' in thing:
        await message.channel.send('NO NO WORD')
        await message.delete()
    if 'nigga' in thing:
        await message.channel.send('NO NO WORD')
        await message.delete()
    if message.author == client.user:
        return
    if "#" in thing:
        if 'c#' in thing:
            await message.channel.send("<@196490316881068032>")
        if '#harass' in thing:
            await message.author.create_dm()
            await message.author.dm_channel.send(file=discord.File('bruh.png'))
            await message.author.dm_channel.send('Time to suffer')
        if '#dice' in thing:
            rollPerm = message.content[message.content.find('(') + 1:message.content.find(')')]
            print(rollPerm)
            sideNum = int(rollPerm[:rollPerm.find(',')])
            diceNum = int(rollPerm[rollPerm.find(',') + 1:])
            print(sideNum)
            print(diceNum)
            rolls = []
            y = 1
            output = ''
            for x in range(diceNum):
                rolls.append(random.randint(1, sideNum))
            for x in rolls:
                output += f'Roll {y}: {x}\n'
                y += 1
            await message.channel.send(output)
        if '#syntax' in thing:
            await message.channel.send('DICE: #dice([numOfSides],[numOfDice])'
                                       '\nADD:  #add([name],[response])'
                                       '\nLIST: #list {[name]}')
        if '#add' in thing:  # god this is fucking disgusting
            string = message.content[message.content.find('(') + 1:message.content.find(')')]
            name = string[:string.find(',')]
            response = string[string.find(',') + 1:string.find(')')].strip()
            file = open(f'{name}.txt', 'a')
            file.write(f'{response}\n')
            file.close()
            nameFile = open('nameList.txt', 'a+')
            if name not in nameList:
                nameFile.write(f'{name}\n')
                nameList.append(name)
            nameFile.close()
            await message.channel.send(f'Done. \nName: {name}\nMessage: {response}')
        if '#list' in thing:
            name = message.content[message.content.find('{') + 1:message.content.find('}')]
            try:
                file = open(f'{name}.txt', 'r')
            except FileNotFoundError:
                await message.channel.send('file not found cuck')
                return
            with file as f:
                output = [line.strip() for line in f]
            await message.channel.send(output)
    else:
        for x in nameList:
            if x in thing:
                await message.channel.send(name_function(x))
    if 'nerd' in thing:
        await message.channel.send('Bruh ima fuck your dad')
    if message.author.id == 379598678920527874:
        await message.channel.send('no u')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(file=discord.File('bruh.png'))
    await member.dm_channel.send('Time to suffer')


def name_function(name):
    file = open(f'{name}.txt', 'r')

    with file as f:
        responses = [line.strip() for line in f]

    return random.choice(responses)


client.run(TOKEN)
