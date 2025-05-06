"""
                          Coder : Omar
                          Version : v2.5.6B
                          version Date :  26 / 04 / 2025
                          Code Type : python | Discrod | GEMINI | GPT | DEEPSEEK | HTTP | ASYNC
                          Title : Initialization of Discord Bot
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]
"""
import discord
from discord.ext import commands , tasks
import utils_bot as util
import asyncio as aio
import random
import random2
import google.generativeai as genai
from openai import AsyncOpenAI
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
from configs import Configs
import sys
import setproctitle
#------------------------------------------------------------------------------------------------------------------------------------------#
#USER MODULES
#------------------------------------------------------------------------------------------------------------------------------------------#
def init_gpt_session():
   #by default checks keys in sys. env variables check func docstring
   gpt = AsyncOpenAI(api_key= keys.openaiAPI_KEY, organization= keys.openaiAPI_ORG_ID) 
   return gpt   

gpt = init_gpt_session()
#------------------------------------------------------------------------------------------------------------------------------------------#
def init_deepSeek_session():
   #by default checks keys in sys. env variables check func docstring
   deepSeek = AsyncOpenAI(api_key= keys.deepseekAPI_KEY, base_url="https://api.deepseek.com") 
   return deepSeek   

deepSeek = init_deepSeek_session()
#------------------------------------------------------------------------------------------------------------------------------------------#
#TODO : complete moving from old un-official bard api to new better gemini(ex-bard) api 
def init_gemini_session () : 
   ... #TODO
#    genai.configure_session(api_key= keys.geminiAPI_KEY)
#    gemini = genai.GenerativeModel(model_name= 'gemini-1.5-flash')
#    return gemini

# gemini = init_gemini_session()

# regarding mentions for all discrod objects : messages , users , rules .. etc : https://discord.com/developers/docs/reference#message-formatting
admin_rooms: list = [889999601350881390,]
wizy_voice_channels = [890209823898107904,]
wizy_feed_channels = [1137242260203909151,]
narols_island_wizard_channel_id = 1118953370510696498
testing_wizard_channel_id = 1133103993942462577
wizy_chat_channels = [narols_island_wizard_channel_id , testing_wizard_channel_id]
wizard_bot_id = 1117540489365827594
default_feed_channel_frequency_minutes: int = 360
#------------------------------------------------------------------------------------------------------------------------------------------#
#NOTE: in order to avoid on_ready() issues override Bot class and move all on ready to it's setup_hook()
class CustomBot(commands.Bot):

   async def setup_hook(self):
      self.is_auto_memequote_state = 1 if len(sys.argv) <= 1 else int(sys.argv[1]) #0 off | 1 on normal mode | 2 on special mode
      self.default_voice_channel: int = wizy_voice_channels[0] #TODO : later will 1) load all voice channels from json 2)assign each wizy voice channel for each server
      self.wizy_chat_ch_ai_type: str = 'deep'
      self.guilds_not_playing_timer: dict[discord.guild.id, int] = {}
      self.resume_chill_if_free.start()
      self.auto_memequote_sender_task.start()
      self.play_chill_loop.start()
      self.load_cfg.start()
      self.init_send_master_dm_msg.start()
      

   async def on_ready(self):
      #next line needed to enable slash commands (slash commands are type of interactions not ctx or message or normal command any more)
      await self.tree.sync()
      print(f"\n\n Bot '{self.user}' Sucessfully connected to Discord!\n\n")


   @tasks.loop(seconds= 10, count= 1) #do once
   async def load_cfg(self):
      # load the configs 
      # (loads default config file if no custom config is found (later either all servers config in one json or each server will have their config class and config json))
      Configs.cfg_load()
      
   @tasks.loop(seconds= 20, count= 1) #do once
   async def init_send_master_dm_msg(self):
      if Configs.config_json_dict :  #if dict not empty
         
         #send any init  dm message to admin (defaults to Narol 'me')
         bot_master: discord.User = self.get_user(Configs.config_json_dict["bot_master_id"])
         master_dm_ch = bot_master.dm_channel or await self.create_dm(bot_master) # if dm channel is none will create new dm (shortcut)
         
         init_master_dm_msg: str = "# Wizy bot Initialized! sending DM init MSG:\n "
         init_master_dm_msg = init_master_dm_msg + f"## Bot info: \n (magic and dunder attrs. excluded)\n\n"
         print(f"Bot info: \n (magic and dunder attrs. excluded) ")
         
         # get and print important bot info
         for attr in dir(self.user):
            if  not (attr.startswith('__') or attr.startswith('_')):
               value = getattr(self.user, attr)
               print(f'{attr}: {value}')
               init_master_dm_msg = init_master_dm_msg + f'{attr}: {value}\n'
         init_master_dm_msg = init_master_dm_msg + f"#####################################\n"
         await master_dm_ch.send(init_master_dm_msg)  #send first portion of the msg
               
         init_master_dm_msg = f"\n\n\n # JOINED SERVERS INFO: \n ## servers count({len(self.guilds)})\n"
         print(f"\n ## Joined servers: count({len(self.guilds)}) \n ")
         for guild in self.guilds :
            print(f"name: {guild.name}")
            print(f"owner: {guild.owner}")
            print(f"owner-ID: {guild.owner_id}")
            print(f"members count: {guild.member_count}")
            print(f"#####################################")
            init_master_dm_msg = init_master_dm_msg + f"Gname: {guild.name}, owner: {guild.owner}, owner-ID: {guild.owner_id}, members count: {guild.member_count}\n"
            init_master_dm_msg = init_master_dm_msg + f"#####################################\n"
            await master_dm_ch.send(init_master_dm_msg)  #send the rest of dm msg to bot master dm
            init_master_dm_msg =""
            
            
   @init_send_master_dm_msg.before_loop
   async def wait_send_until_ready(self):
      await self.wait_until_ready()
   

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
                     
                     await guild.voice_client.resume() if guild.voice_client.is_paused() else await util.play_chill_track(guild)
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
def pre_boot_setup(_main_file: str):
   
   if sys.platform.startswith('linux'): # change process name on linux cuz it's hard on win :(
      setproctitle.setproctitle("bot_wizy_discord.py") 
   
   util.cd_to_main_dir(_main_file) #so log files will be written in the same project dir
   log_std = open("std.log" , 'a') #logs all stderr and stdout and discord.py msgs
   log_discord = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')#logs only discord.py msgs
   return log_std , log_discord
   
#------------------------------------------------------------------------------------------------------------------------------------------#
def boot_bot(main_file: str) :
   log_std, log_discord = pre_boot_setup(main_file)
   if 'IS_PRODUCTION' in os.environ and os.environ['IS_PRODUCTION'] == '1' :
      with contextlib.redirect_stdout(log_std):
         with contextlib.redirect_stderr(log_std):
            bot.run(keys.Token_gpteousBot , log_handler= log_discord, log_level= logging.INFO)#default logging level is info
   else :
      bot.run(keys.Token_gpteousBot , log_level= logging.DEBUG) #default handler is stdout , debug log level is more verbose!
#------------------------------------------------------------------------------------------------------------------------------------------#
