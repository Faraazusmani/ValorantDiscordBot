import discord
import os
import requests
import json
from keep_alive import keep_alive
# from replit import db


client = discord.Client()

# pingthem = ['Baquir', 'Naman', 'Isa', 'Kushagra', 'Faraaz']

# def update_pingthem(people):
#   if "pingthem" in db.key():
#     pingthem = db["pingthem"]
#     pingthem.append(people)
#     db["pingthem"] = pingthem
#   else:
#     db["pingthem"] = [people]

# def delete_pingthem(index):
#   pingthem = db["pingthem"]
#   if len(pingthem) > index:
#     del pingthem[index]
#     db["pingthem"] = pingthem


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/hello'):
    await message.channel.send('Hello! I am here to assist you with Valorant and improve your game. \nUse /help to get the list of commands.')
  
  if message.content.startswith('/help' or '/commands'):
    await message.channel.send('This bot will only respond to the commands that are preceded with a forward slash (/)')
  #  await message.channel.send('/pingthem - tag Baquir, Kushagra, Isa, Naman, Faraaz, Harshit, and Ayush to let them know you are online and waiting a game ( exclusively for the members of ping spike, a group of 7 friends who play Valorant together) \n')
    await message.channel.send('/hello - welcome the bot in your server')
    await message.channel.send('/help - get the list of commands')
    await message.channel.send('/gn - when you are going offline this command will let your teammates know\n')
    await message.channel.send('/gg - you know what it means\n')
    await message.channel.send('/mapname - Enter the map name to know the best 5 agents to play on that map\n')
    await message.channel.send('/agentnameguide - Enter agent name followed by guide to get a brief summary about the agent and their abilities\n')
    await message.channel.send('/agentnamelineup - Enter agent name followed by lineup to see the lineups of that agent\n')
    await message.channel.send('/agentsguide - a general guide about all agents\n')
    await message.channel.send('/lineups - lineups of all agents\n')
    await message.channel.send('/mystats - know all your stats from each act for all in-game modes')
    await message.channel.send('/weapons - know all the details about each weapon')
    await message.channel.send('/maps - get information about each map')
    await message.channel.send('/valolive - all the live valorant tournaments and streams\n')
    await message.channel.send('/updates - know all the recent updates about the game\n')


  if message.content.startswith('/pingthem'):
    await message.channel.send('Aao ez derank <@516225596653699083> <@543774686815977483> <@691333144317657164> <@691332492191334411> <@689716989530603652> <@461824206519271424> <@687291362499887124>')

  if message.content.startswith('/gn'):
    await message.channel.send('Good night. See you all tomorrow')

  if message.content.startswith('/bye'):
    await message.channel.send('Jaa rahe ab kal aate hain')

  if message.content.startswith('/gg'):
    await message.channel.send('Good game boys')
    await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
  
  if message.content.startswith('/valolive'):
    await message.channel.send('https://www.youtube.com/results?search_query=valorant+live')

  if message.content.startswith('/updates'):
    await message.channel.send('https://playvalorant.com/en-us/news/game-updates/')  

  if message.content.startswith('/mystats'):
    await message.channel.send('https://tracker.gg/valorant')

  if message.content.startswith('/weapons'):
    await message.channel.send('https://tracker.gg/valorant/weapons')
  
  if message.content.startswith('/maps'):
    await message.channel.send('https://tracker.gg/valorant/maps')

  if message.content.startswith('/ascent'):
    await message.channel.send('https://i.pinimg.com/originals/5f/8e/d3/5f8ed39c40c2127ce26ec10827a4cd25.jpg')
    await message.channel.send('Breach               Killjoy               Sova               Jett               Kay/O')
  if message.content.startswith('/bind'):
    await message.channel.send('https://i.pinimg.com/originals/20/9a/7e/209a7ee164e13e98d27b6fa67e085cd9.jpg')
    await message.channel.send('Astra               Cypher               Viper               Raze               Kay/O')
  if message.content.startswith('/breeze'):
    await message.channel.send('https://i.pinimg.com/originals/5b/c8/fa/5bc8fa9f88ba5e7f5cd58589a87448ed.jpg')
    await message.channel.send('Kay/O               Jett               Viper               Skye               Yoru')
  if message.content.startswith('/haven'):
    await message.channel.send('https://i.pinimg.com/originals/0e/05/80/0e05808ae2adfaa1d559bd2bfae9c6ef.jpg')
    await message.channel.send('Kay/O               Astra               Sova               Jett               Skye')
  if message.content.startswith('/icebox'):
    await message.channel.send('https://i.pinimg.com/originals/2d/e1/cf/2de1cff4816f78282daf54e52b4e2098.jpg')
    await message.channel.send('Sova               Viper               Kay/O               Sage               Jett')
  if message.content.startswith('/split'):
    await message.channel.send('https://i.pinimg.com/originals/9a/b0/c4/9ab0c4a9b31860d07c0fe4417f7e0d32.jpg')
    await message.channel.send('Skye               Cypher               Omen               Sage               Raze')  

  if message.content.startswith('/valo'):
    await message.channel.send('https://img.rankedboost.com/wp-content/uploads/2020/03/Valorant-characters-agents-list.png')
  
  if message.content.startswith('/agentsguide'):
    await message.channel.send('https://tracker.gg/valorant/agents')
  if message.content.startswith('/astraguide'):
    await message.channel.send('ASTRA'+'https://tracker.gg/valorant/agents/astra')
  if message.content.startswith('/breachguide'): 
    await message.channel.send('BREACH' + 'https://tracker.gg/valorant/agents/breach')
  if message.content.startswith('/brimstoneguide'):  
    await message.channel.send('BRIMSTONE' + 'https://tracker.gg/valorant/agents/brimstone')
  if message.content.startswith('/cypherguide'):
    await message.channel.send('CYPHER' + 'https://tracker.gg/valorant/agents/cypher')
  if message.content.startswith('/jettguide'):
    await message.channel.send('JETT' + 'https://tracker.gg/valorant/agents/jett')
  if message.content.startswith('/kayoguide'):
    await message.channel.send('KAY/O' + 'https://tracker.gg/valorant/agents/kayo')
  if message.content.startswith('/killjoyguide'):
    await message.channel.send('KILLJOY' + 'https://tracker.gg/valorant/agents/killjoy')
  if message.content.startswith('/omenguide'):
    await message.channel.send('OMEN' + 'https://tracker.gg/valorant/agents/omen')
  if message.content.startswith('/phoenixguide'):
    await message.channel.send('PHOENIX' + 'https://tracker.gg/valorant/agents/phoenix')
  if message.content.startswith('/razeguide'):
    await message.channel.send('RAZE' + 'https://tracker.gg/valorant/agents/raze')
  if message.content.startswith('/reynaguide'):
    await message.channel.send('REYNA' + 'https://tracker.gg/valorant/agents/reyna')
  if message.content.startswith('/sageguide'):
    await message.channel.send('SAGE' + 'https://tracker.gg/valorant/agents/sage')
  if message.content.startswith('/skyeguide'):
    await message.channel.send('SKYE' + 'https://tracker.gg/valorant/agents/skye')
  if message.content.startswith('/sovaguide'):
    await message.channel.send('SOVA' + 'https://tracker.gg/valorant/agents/sova')
  if message.content.startswith('/viperguide'):
    await message.channel.send('VIPER' + 'https://tracker.gg/valorant/agents/viper')
  if message.content.startswith('/yoruguide'):
    await message.channel.send('YORU' + 'https://tracker.gg/valorant/agents/yoru')

  if message.content.startswith('/lineups'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips')
  if message.content.startswith('/astralineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=astra&map=all&objective=all')
  if message.content.startswith('/breachlineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=breach&map=all&objective=all')
  if message.content.startswith('/brimstonelineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=brimstone&map=all&objective=all')
  if message.content.startswith('/cypherlineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=cypher&map=all&objective=all')
  if message.content.startswith('/jettlineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=jett&map=all&objective=all')
  if message.content.startswith('/kayolineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=kayo&map=all&objective=all')
  if message.content.startswith('/killjoylineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=killjoy&map=all&objective=all')
  if message.content.startswith('/omenlineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=omen&map=all&objective=all')
  if message.content.startswith('/phoenixlineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=phoenix&map=all&objective=all')
  if message.content.startswith('/razelineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=raze&map=all&objective=all')
  if message.content.startswith('/reynalineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=reyna&map=all&objective=all')
  if message.content.startswith('/sagelineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=sage&map=all&objective=all')
  if message.content.startswith('/skyelineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=skye&map=all&objective=all')
  if message.content.startswith('/sovalineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=sova&map=all&objective=all')
  if message.content.startswith('/viperlineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=viper&map=all&objective=all')
  if message.content.startswith('/yorulineup'):
    await message.channel.send('https://tracker.gg/valorant/guides/clips?agent=yoru&map=all&objective=all')

keep_alive()
client.run(os.environ['TOKEN'])
