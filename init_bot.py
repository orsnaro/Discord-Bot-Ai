"""
                          Coder : Omar
                          Version : v2.5.2B
                          version Date :  17 / 8 / 2023
                          Code Type : python | Discrod | BARD | GPT | HTTP | ASYNC
                          Title : Initialization of Discord Bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
import discord
from discord.ext import commands
import asyncio as aio
import random
from bardapi import BardAsync , Bard
from inspect import getmembers , isfunction
import aiohttp
import requests
from pyrandmeme2 import pyrandmeme2
from quote import quote
from random_word import RandomWords
from datetime import datetime
import re
import pytz
# from bard_key_refresh import regenerate_cookie #TODO:
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
	bard = BardAsync(token= bardAPI_KEY ) #add -> language= 'ar' to respond in arabic only (experimental)
	# while True:
	# 	try :
	# 		bard = BardAsync(token= bardAPI_KEY ) #add -> language= 'ar' to respond in arabic only (experimental)
	# 		break;

	# 	except Exception as e :
	# 		regenerate_cookie()
	# 		print ( e.__str__() + " TESTING NOTE : this is manual error message from init_bard_session() function")

	return bard

bard = init_bard_session()

# regarding mentions for all discrod objects : messages , users , rules .. etc : https://discord.com/developers/docs/reference#message-formatting
admins_room_id = 889999601350881390
narols_island_wizard_channel_id = 1118953370510696498
testing_wizard_channel_id = 1133103993942462577
wizard_channels = (narols_island_wizard_channel_id , testing_wizard_channel_id )
wizard_bot_id = 1117540489365827594
chat_chill_ch_id = 889535812167938088
proxy_sites = ["https://Proxy.server:3128" ,"https://95.217.167.241:8080"]#first one is the only proxy server available for free in pythonanywhere for more servers: https://hidemyna.me/en/proxy-list/?type=s#list
bot = commands.Bot(command_prefix= ("~" , '' , ' '), case_insensitive= True , strip_after_prefix= True , intents=discord.Intents.all() , allowed_mentions= discord.AllowedMentions(everyone= False) , description= f""" 
                   GPTEOUS HELP MESSAGE```
                   **I'M MIGHTY GPTEOUS !** the first GPT-Spirit in Narol's island Volcan guardian , Island's Master right hand  and the begining of Island's new ERA etcetera etcetera... I mean you get it am very special here  :man_mage:

						** :sparkles: __COMMAND GROUP 1: ASK , I shall Answer! __:sparkles:  **
      
 						:label:    Ask me any where in the Island and  I shall INDEED answer you 

						:label:    The question must start start with mentioning me e.g.( <@{wizard_bot_id}> )
      
						:label:    if you want to speak with me more freely with no mentions/commands 
      							   just type anything in my channel <#{narols_island_wizard_channel_id}> and I shall respond !

      
                 				  ** :sparkles: __COMMAND GROUP 2: Wise Quotes & Deep memes __:sparkles:  **
                      
						:label:    to get random meme at any time use 'BoringWizard' 
						:label:    to get random quote at any time use 'wisewiz' 
      
						      		:inbox_tray: _Aditional Functionalities and SPELLS coming soon ..._:inbox_tray: 
              
                   __COMANDS LIST__
                   ```fix
                   1. @WizardSpirit "your_question" 
                   2. `wiz` "your_question"
                   3. `bard` "your_question"
                   4. `wizard` "your_question"
                   5. `wizardspirit` "your_question"
                   6. `~ <any_of_prev_CMDs>` "your_question"
                   7. `wisewiz`
                   8. `BoringWizard`
                   _(all of them is case INsensitive)_
                   ```
                     
      				```fix
						**WARNING**: sometimes I won't respond this is mainly due to exceeding max embed char limit 
      				i.e.(6000chars)
						```
                   """)
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.event
async def on_ready():
   admin_ch = bot.get_channel(admins_room_id)
   await admin_ch.connect()
   
   playing = discord.Game("Playing help")
   bot.change_presence(status=discord.Status.online , activity=playing)
   
   print(f"Bot info: \n (magic and dunder attrs. excluded) ")
   for attr in dir(bot.user):
      if  not (attr.startswith('__') or  attr.startswith('_')) :
         value = getattr(bot.user, attr)
         print(f'{attr}: {value}')
   print(f"\n\n Bot '{bot.user}' Sucessfully connected to Discord!\n\n")
#------------------------------------------------------------------------------------------------------------------------------------------#
def get_last_conv_id()  : ...  #TODO

