import discord
import os
from keep_alive import keep_alive

client = discord.Client()
version = discord.__version__
print(version)
intents = discord.Intents.default()
intents.members = True
rules = "1. No NSFW or Offensive Content - Self explanatory, it is not wanted. \n 2. Keep Swearing To A Minimum - not everyone wants to see that \n 3. Respect All Staff - We all work very hard, and if we can't get to you at the moment, we'll try to get back with you soon! \n 4. Keep Arguments Out - Use DMs to settle problems, please. \n 5. No Advertising - Advertising is not allowed unless you have been given special permission by an HR to do so. \n 6. Don't Spam - It is annoying, and could get you muted for a certain period of time. \n 7. Keep Politics Out - Please use DMs to talk about politics, as it may create arguments here. \n 8. Do Not Threaten Yourself Or Others - We want everyone to feel safe here! Threatening may lead to consequences. \n 9. Have fun! - We're doing our best to accommodate everyone's needs, so don't forget to relax and have fun! :smile:"
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(834185160919875677) #I did define channel Id in my code
    await channel.send("Everyone welcome " + member.mention + " to Delta!")
    rules = discord.Embed(title="Rules:", color=1146986)
    rules.add_field(name="1.", value="No NSFW or Offensive Content - Self explanatory, it is not wanted.", inline=True)
    rules.add_field(name="2.", value="Keep Swearing To A Minimum - not everyone wants to see that", inline=True)
    rules.add_field(name="3.", value="Respect All Staff - We all work very hard, and if we can't get to you at the moment, we'll try to get back with you soon!", inline=True)
    rules.add_field(name="4.", value="Keep Arguments Out - Use DMs to settle problems, please.", inline=True)
    rules.add_field(name="5.", value="No Advertising - Advertising is not allowed unless you have been given special permission by an HR to do so.", inline=True)
    rules.add_field(name="6.", value="Don't Spam - It is annoying, and could get you muted for a certain period of time.", inline=True)
    rules.add_field(name="7.", value="Keep Politics Out - Please use DMs to talk about politics, as it may create arguments here.", inline=True)
    rules.add_field(name="8.", value="Do Not Threaten Yourself Or Others - We want everyone to feel safe here! Threatening may lead to consequences.", inline=True)
    rules.add_field(name="9.", value="Have fun! - We're doing our best to accommodate everyone's needs, so don't forget to relax and have fun! :smile:", inline=True)
    await member.send("Welcome to Delta! There are a few rules we would like you to keep in mind whilst chating in our server")
    await member.send(embed=rules)
    
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('?hello'):
            await message.channel.send('Hello!')
        
        if message.content.startswith('?help'):
            embed = discord.Embed(title="Commands:", color=1146986)
            embed.add_field(name="__?help__", value="Displays list of commands", inline=False)
            embed.add_field(name="__?hello__", value="Responds with hello", inline=False)
            embed.add_field(name="__?calendar__", value="Displays a list of the confirmed and planned flights", inline=False)
            embed.add_field(name="__?rules__", value="Displays a list of all the rules", inline=False)
            embed.add_field(name="__?test__", value="Command to test if the bot is functioning properly", inline=False)
            await message.channel.send(embed=embed)


        if message.content.startswith('?calendar'):
            embed = discord.Embed(title="Flight Calendar:", color=1146986)
            embed.add_field(name="**Confirmed Flights:**", value="MM/DD/YY HH:MM EST", inline=False)
            embed.add_field(name="**Planned Flights**", value="MM/DD/YY HH:MM EST", inline=False)
            await message.channel.send(embed=embed)
        
        if message.content.startswith('?test'):
            await message.channel.send("the bot is working properly")
        
        if message.content.startswith('?rules'):
            rules = discord.Embed(title="Rules:", color=1146986)
            rules.add_field(name="1.", value="No NSFW or Offensive Content - Self explanatory, it is not wanted.", inline=True)
            rules.add_field(name="2.", value="Keep Swearing To A Minimum - not everyone wants to see that", inline=True)
            rules.add_field(name="3.", value="Respect All Staff - We all work very hard, and if we can't get to you at the moment, we'll try to get back with you soon!", inline=True)
            rules.add_field(name="4.", value="Keep Arguments Out - Use DMs to settle problems, please.", inline=True)
            rules.add_field(name="5.", value="No Advertising - Advertising is not allowed unless you have been given special permission by an HR to do so.", inline=True)
            rules.add_field(name="6.", value="Don't Spam - It is annoying, and could get you muted for a certain period of time.", inline=True)
            rules.add_field(name="7.", value="Keep Politics Out - Please use DMs to talk about politics, as it may create arguments here.", inline=True)
            rules.add_field(name="8.", value="Do Not Threaten Yourself Or Others - We want everyone to feel safe here! Threatening may lead to consequences.", inline=True)
            rules.add_field(name="9.", value="Have fun! - We're doing our best to accommodate everyone's needs, so don't forget to relax and have fun! :smile:", inline=True)
            await message.channel.send(embed=rules)

keep_alive()
token = "ODM0MDkzMzQxMjY0MDUyMjk0.YH739Q.LzXVvSWvRyPs30oIMTBei05U-nw"
client.run(token)
