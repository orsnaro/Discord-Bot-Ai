"""
                          Coder : Omar
                          Version : v2.5.5B
                          version Date :  8 / 11 / 2023
                          Code Type : python | Discrod | BARD | GPT | HTTP | ASYNC
                          Title : Initialization of Discord Bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
import discord
from discord.ext import commands , tasks
import utils_bot as util
import asyncio as aio
import random
import random2
from bardapi import BardAsync , Bard , BardCookies , SESSION_HEADERS
from openai import AsyncOpenAI
import openai
from inspect import getmembers , isfunction
import aiohttp
import requests
from pyrandmeme2 import pyrandmeme2
from pyrandmeme2 import palestina_free
# from quote_async.quote import quote #TODO ( complete your quote lib fork and make it fully async )
from quote import quote
from random_word import RandomWords
from datetime import datetime
import re
import pytz
import asyncforismatic.asyncforismatic as foris
import logging
import contextlib
import os
import help_bot
import keys
import configs
import sys
# from bard_key_refresh import regenerate_cookie #TODO:
#------------------------------------------------------------------------------------------------------------------------------------------#
#USER MODULES
#------------------------------------------------------------------------------------------------------------------------------------------#
def init_gpt_session():
   #by default checks keys in sys. env variables check func docstring
   gpt = AsyncOpenAI(api_key= keys.openaiAPI_KEY, organization= keys.openaiAPI_ORG_ID) 
   return gpt   

gpt = init_gpt_session()
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

   
   bard = BardAsync(token=keys.bardAPI_KEY) #add -> language= 'ar' to respond in arabic only (experimental)
   
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
admin_rooms: list = [889999601350881390,]
wizy_voice_channels = [890209823898107904,]
wizy_feed_channels = [1137242260203909151,]
narols_island_wizard_channel_id = 1118953370510696498
testing_wizard_channel_id = 1133103993942462577
wizy_chat_channels = [narols_island_wizard_channel_id , testing_wizard_channel_id]
wizard_bot_id = 1117540489365827594
default_feed_channel_frequency_minutes: int = 120
#------------------------------------------------------------------------------------------------------------------------------------------#
#NOTE: in order to go  away from on_ready() issues override Bot class and move all on ready to it's setup_hook()
class CustomBot(commands.Bot):

   async def setup_hook(self):
      self.is_auto_memequote_state = 1 if len(sys.argv) <= 1 else int(sys.argv[1]) #0 off | 1 on normal mode | 2 on special mode
      self.default_voice_channel: int = wizy_voice_channels[0] #TODO : later will 1) load all voice channels from json 2)assign each wizy voice channel for each server
      self.wizy_chat_ch_ai_type: str = 'gpt'
      self.guilds_not_playing_timer: dict[discord.guild.id, int] = {}
      self.resume_chill_if_free.start()
      self.auto_memequote_sender_task.start()
      self.play_chill_loop.start()

   async def on_ready(self):
      #next line needed to enable slash commands (slash commands are type of interactions not ctx or message or normal command any more)
      await self.tree.sync()
      print(f"Bot info: \n (magic and dunder attrs. excluded) ")
      for attr in dir(self.user):
         if  not (attr.startswith('__') or attr.startswith('_')):
            value = getattr(self.user, attr)
            print(f'{attr}: {value}')
      print(f"\nJoined servers: count({len(self.guilds)}) \n ")
      for guild in self.guilds :
         print(f"name: {guild.name}")
         print(f"owner: {guild.owner}")
         print(f"owner-ID: {guild.owner_id}")
         print(f"members count: {guild.member_count}")
         print(f"#####################################")
      print(f"\n\n Bot '{self.user}' Sucessfully connected to Discord!\n\n")


   @tasks.loop(seconds= 5)
   async def  resume_chill_if_free(self):
      for guild in self.guilds:
         increment_val_sec = 5 
         if guild.id in self.guilds_not_playing_timer:
            # check happens once every 5 secs so increment every time by 5 secs
            self.guilds_not_playing_timer[guild.id] += increment_val_sec
         else:
            self.guilds_not_playing_timer[guild.id] = increment_val_sec

         if guild.voice_client != None and guild.voice_client.is_connected():
            if not guild.voice_client.is_playing():
               threshold_sec = 180 #3 minutes
               if self.guilds_not_playing_timer[guild.id] >= threshold_sec:
                  #if there is any user in channel besides wizy the bot play chill music else stay silent
                  connected_users_cnt = len( guild.voice_client.channel.members ) - 1
                  if connected_users_cnt >= 1 :
                     await guild.voice_client.channel.send("*3+ minutes of Silence:pleading_face: resuming* **MMO Chill Track** ...")
                     await util.play_chill_track(guild)
                  else:
                     #TESTING
                     print("\n\n\n\n\n\n TESTING########################## \n\n\n\n\n there is only the bot in voice channel: don't start track... \n\n\n\n\n\n######################\n\n\n\n")
                     #TESTING
                     
                  self.guilds_not_playing_timer[guild.id] = 0
            else :
               self.guilds_not_playing_timer[guild.id] = 0
         else:
            self.guilds_not_playing_timer[guild.id] = 0

   @resume_chill_if_free.before_loop
   async def wait_bot_ready(self):
      await self.wait_until_ready()
   

   @tasks.loop(minutes= default_feed_channel_frequency_minutes)#def= 2 hours
   async def auto_memequote_sender_task(self):
      await util.send_rand_quote_meme(is_special= True if self.is_auto_memequote_state >= 2 else False)

   @auto_memequote_sender_task.before_loop
   async def before_start_auto_memequote_sender(self):
      #TESTING
      print(f"\n\n\n\n\n TESTING#####################   \n\n\n you auto_memequote_sender state is : {self.is_auto_memequote_state} \n\n\n\n ######################")
      #TESTING
      await self.wait_until_ready()

   async def set_memequote_sender_frequency(self, _interval_minutes: int = default_feed_channel_frequency_minutes ): 
      self.auto_memequote_sender_task.change_interval(minutes= _interval_minutes)

   async def toggle_auto_memequote_sender_state(self, state:int = None ) -> bool :
      
      if state is None: 
         if self.is_auto_memequote_state > 0 :
            self.auto_memequote_sender_task.cancel()
            self.is_auto_memequote_state = 0
         else:
            self.auto_memequote_sender_task.start()
            self.is_auto_memequote_state = 1
      elif state == 0:
         if self.auto_memequote_sender_task.is_running():
            self.auto_memequote_sender_task.cancel()
            self.is_auto_memequote_state = 0
      elif state == 1:
         if not self.auto_memequote_sender_task.is_running():
            self.auto_memequote_sender_task.start()
            self.is_auto_memequote_state = 1
      elif state == 2: #special eventof type: FREE Palestine!
            self.is_auto_memequote_state = 2
         
         
      return self.is_auto_memequote_state

   @tasks.loop(hours= 3)
   async def play_chill_loop(self, target_ch: discord.VoiceChannel= None):
      #when booting up bot make him join admin room (only for my server wizy home!)
      targetVchannel = self.get_channel(self.default_voice_channel) if target_ch == None else target_ch
      server = targetVchannel.guild

      if server.voice_client is not None :
         server.voice_client.disconnect()

      await targetVchannel.connect()

      if not server.voice_client.is_playing() :
         await util.play_chill_track(server)


   @play_chill_loop.before_loop
   async def before_play_chill(self):
      await self.wait_until_ready()

   async def stop_play_chill_loop(self):
      self.play_chill_loop.cancel()
   async def start_play_chill_loop(self):
      self.play_chill_loop.start()
#------------------------------------------------------------------------------------------------------------------------------------------#
bot = CustomBot(
                  command_prefix= ("~", '', ' '),
                  case_insensitive= True,
                  strip_after_prefix= True,
                  intents=discord.Intents.all(),
                  allowed_mentions= discord.AllowedMentions(everyone= False),
                  description= help_bot.default_help_msg,
                  status= discord.Status.online,
                  activity= discord.Game("/help"),
                  help_command= None,
               )
#------------------------------------------------------------------------------------------------------------------------------------------#
def get_last_conv_id()  : ...  #TODO
#------------------------------------------------------------------------------------------------------------------------------------------#
def boot_bot() :
   log_std = open("std.log" , 'a') #logs all stderr and stdout and discord.py msgs
   log_discord = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')#logs only discord.py msgs
   if 'IS_PRODUTCION' in os.environ and os.environ['IS_PRODUCTION'] == '1' :
      with contextlib.redirect_stdout(log_std):
         with contextlib.redirect_stderr(log_std):
            bot.run(keys.Token_gpteousBot , log_handler= log_discord)#default logging level is info
   else :
      bot.run(keys.Token_gpteousBot , log_level= logging.DEBUG) #default handler is stdout , debug log level is more verbose!
#------------------------------------------------------------------------------------------------------------------------------------------#