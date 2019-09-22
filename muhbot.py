import requests
import json
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print ('im in')
    channel = bot.get_channel(624999751674232869)
    await channel.send('Hello')
    while True:
        req = requests.get('https://api.warframestat.us/pc/cetusCycle')
        timeLeft = req.json()['shortString']
        if timeLeft.endswith('Day'):
            timeLeft = timeLeft.replace('Day', '🌞')
        else:
            timeLeft = timeLeft.replace('Night', '🌙')
        await bot.change_presence(activity=discord.Game(name=timeLeft))
        await asyncio.sleep(10)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'arcane acceleration' in message.content.lower():
        embed=discord.Embed(color=0x5ff1f1)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/3/3d/ArcaneAcceleration.png/revision/latest?cb=20181225172053")
        embed.add_field(name='Arcane Acceleration', value='On Critical Hit: 5% / 10% / 15% / 20% chance to give 15% / 30% / 45% / 60% Fire Rate to Primary Weapons for 2 / 3 / 5 / 6 seconds', inline=True)
        await message.channel.send(embed = embed)
    
    if 'arcane aegis' in message.content.lower():
        embed=discord.Embed(color=0x5ff1f1)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/3/3e/ArcaneAegis.png/revision/latest?cb=20181225172055")
        embed.add_field(name='Arcane Aegis', value='On Damaged: 2% / 3% / 5% / 6% chance for 15 / 30 / 45 / 60 Shields Regen/sec for 5 / 10 / 15 / 20 Seconds', inline=True)
        await message.channel.send(embed = embed)

    if 'arcane agility' in message.content.lower():
        embed=discord.Embed(color=0x5ff1f1)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/0/0d/ArcaneAgility.png/revision/latest?cb=20181225172056")
        embed.add_field(name='Arcane Agility', value='On Damaged: 3% / 6% / 9% / 12% chance for 10% / 20% / 30% / 40% Parkour Velocity for 2 / 4 / 6 / 8 Seconds', inline=True)
        await message.channel.send(embed = embed)

    if 'arcane arachne' in message.content.lower():
        embed=discord.Embed(color=0x5ff1f1)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/4/43/ArcaneArachne.png/revision/latest?cb=20181225172057")
        embed.add_field(name='Arcane Arachne', value='On Wall Latch for 2s: 100% chance for 25% / 50% / 75% / 100% Bonus Damage for 5s / 10s / 15s / 20s', inline=True)
        await message.channel.send(embed = embed)

    if 'arcane avenger' in message.content.lower():
        embed=discord.Embed(color=0x5ff1f1)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/a/ab/ArcaneAvenger.png/revision/latest?cb=20181225172059")
        embed.add_field(name='Arcane Avenger', value='On Damaged: 4% / 7% / 11% / 14% chance for 7.5% / 15% / 22.5% / 30% Critical Chance for 2 / 4 / 6 / 8 Seconds', inline=True)
        await message.channel.send(embed = embed)

    if 'arcane awakening' in message.content.lower():
        embed=discord.Embed(color=0x5ff1f1)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/a/ae/ArcaneAwakening.png/revision/latest?cb=20181225172058")
        embed.add_field(name='Arcane Awakening', value='On Reload: 10% / 20% / 30% / 40% chance for 25% / 50% / 75% / 100% Damage to Pistols for 4 / 8 / 12 / 16 Seconds', inline=True)
        await message.channel.send(embed = embed)
    
    if 'fuck' in message.content.lower():
        await message.delete()
        await message.channel.send('{0.author.mention} using profanity is prohibited here.'.format(message))

bot.run('NjI0OTkyMjI2NzI3OTUyMzk1.XYZEhA.xGmxPTpGVaWBxUKZNcDjVDltkPc')