"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | GPT | HTTP | ASYNC
                          Title : Initialization of Discord Bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
import asyncio as aio
import random
from bardapi import BardAsync , Bard
import discord
from discord.ext import commands
from inspect import getmembers , isfunction
import aiohttp
import requests
#------------------------------------------------------------------------------------------------------------------------------------------#
#USER MODULES
from keys import bardAPI_KEY

#------------------------------------------------------------------------------------------------------------------------------------------#

def init_bard_session () :
	# session = requests.Session()
	# session.headers = {
   #          "Host": "bard.google.com",
   #          "X-Same-Domain": "1",
   #          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
   #          "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
   #          "Origin": "https://bard.google.com",
   #          "Referer": "https://bard.google.com/",
   #      }
	# session.cookies.set("__Secure-1PSID", bardAPI_KEY) 
	# bard = Bard(token=bardAPI_KEY , session=session, timeout=30)
	bard = BardAsync(token=bardAPI_KEY) #add -> language= 'ar' to respond in arabic only (experimental)

	return bard
bard = init_bard_session()

wizard_bot_id = 1117540489365827594
wizard_channel_id = 1118953370510696498
bot = commands.Bot(command_prefix= ("~" , '' , ' '), case_insensitive= True , strip_after_prefix= True , intents=discord.Intents.all() ,description= f""" 
                   GPTEOUS HELP MESSAGE```
                   **I'M MIGHTY GPTEOUS !** the first GPT-Spirit in Narol's island volcan gurdian , Island Master right hand  and the begining of Island's new ERA  , etc... I mean you get it am very special here  :man_mage:

 						:inbox_tray:   Ask me any where in the Island and  I shall INDEED answer you 

						:inbox_tray:   The question must start start with mentioning me e.g.( <@{wizard_bot_id}> )
      
						:inbox_tray:   if you want to speak with me more freely with no mentionrs/ commands just type anything in my channel <#{wizard_channel_id}> and I shall respond !

						:inbox_tray:   Aditional Functionalities and SPELLS coming soon...

                   
                   __COMANDS LIST__
                   ```fix
                   1. <@{wizard_bot_id}> "your_question"
                   3. wiz "your_question"
                   5. bard "your_question"
                   2. wizard "your_question"
                   4. wizardspirit "your_question"
                   6. ~ <any_of_prev_CMDs> "your_question"
                   ```
                   
                   ```fix
                   *note : Due to connectivity + billing issues between my country 'Egypt' and GPT API We temporarily moved to using bard via a coockie key
                   ```
                   """)

pagHelp = commands.Paginator(suffix="")
# minHelp = commands.MinimalHelpCommand()
# help = commands.HelpCommand()
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.event
async def on_ready():
   print ("RAW DATA ON HELP: PAGES DATA THEN HELP THE MINIMAL HELP:")
   # print (pagHelp.pages)
   print ("RAW DATA ON HELP: MINIMAL HELP:")
   # print(minHelp.get_ending_note())
   # print(minHelp.get_opening_note())
   # print(minHelp.get_command_signature("~wizard"))
   # print(minHelp.get_command_signature("wizard"))
   # print(minHelp.get_command_signature("~"))
   print ("RAW DATA ON HELP: HELP:")
   # print(help.get_bot_mapping())
   # print(help.get_command_signature("~wizard"))
   # print(help.get_command_signature("wizard"))
   # print(help.get_command_signature("~"))
   print ("RAW DATA ON bot: ")
   print(f"Bot '{bot.user}' Sucessfully connected to Discord!\n\n")
   print(f"Bot info: \n (magic and dunder attrs. excluded) ")
   for attr in dir(bot.user):
      if  not (attr.startswith('__') or  attr.startswith('_')) :
         value = getattr(bot.user, attr)
         print(f'{attr}: {value}')


