"""
                          Coder : Omar
                          Version : v2.5.8B
                          version Date :  14 / 09 / 2025
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
#by default checks keys in sys. env variables check func docstring
def init_gpt_session():
   """
   Initializes and returns an OpenAI API session.
   
   Returns:
       AsyncOpenAI: An initialized OpenAI client configured with API key and organization ID.
       
   Note:
       By default checks for API keys in system environment variables.
   """
   gpt = AsyncOpenAI(api_key= keys.openaiAPI_KEY, organization= keys.openaiAPI_ORG_ID) 
   return gpt   

gpt = init_gpt_session()
#------------------------------------------------------------------------------------------------------------------------------------------#
#by default checks keys in sys. env variables check func docstring
def init_deepSeek_session():
   """
   Initializes and returns a DeepSeek API session.
   
   Returns:
       AsyncOpenAI: An initialized DeepSeek client configured with API key and base URL.
       
   Note:
       By default checks for API keys in system environment variables.
   """
   deepSeek = AsyncOpenAI(api_key= keys.deepseekAPI_KEY, base_url="https://api.deepseek.com") 
   return deepSeek   

deepSeek = init_deepSeek_session()
#------------------------------------------------------------------------------------------------------------------------------------------#
#TODO : complete moving from old un-official bard api to new better gemini(ex-bard) api 
def init_gemini_session():
   """
   Initializes and returns a Gemini API session.
   
   Note:
       This is a placeholder for future implementation. The function will be completed
       to move from the old unofficial Bard API to the new Gemini API.
   """
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
 #TODO: cache wizy states per guild to save the expensive for/while loops in bot tasks that runs periodically to get some wizy timer and state for each guild each x minute || second !!
class CustomBot(commands.Bot):
   """
   Custom Discord bot implementation with extended functionality.
   
   This class extends the base Discord Bot class to add custom features including:
   - Automatic meme and quote sending
   - Voice channel management
   - Multiple AI model support
   - Configuration management
   - Periodic tasks and state tracking
   
   Attributes:
       auto_memequote_state (int): Controls the state of automatic meme/quote sending
       default_voice_channel (int): Default voice channel ID for the bot
       default_wizy_chat_ch_ai_type (str): Default AI model for chat
       wizy_chat_ch_ai_types (list): Available AI model types
       default_auto_played_track_type (str): Default music track type
       auto_played_tracks (dict): Available music track types and their paths
       alone_increment_val_sec (int): Time increment for alone status check
       wizy_alone_threshold_sec (int): Threshold for considering bot alone
       guilds_not_playing_timer (dict): Tracks time for each guild's playing status
       connected_to_wizy_voice_per_guild (dict): Tracks voice connection status per guild
   """
   
   async def setup_hook(self):
      """
      Initializes bot settings and starts periodic tasks.
      
      This method is called when the bot is starting up. It:
      - Sets initial states and configurations
      - Initializes tracking dictionaries
      - Starts periodic tasks for various bot functions
      """
      self.auto_memequote_state = 1 if len(sys.argv) <= 1 else int(sys.argv[1]) #0 off | 1 on normal mode | 2 on special mode
      self.default_voice_channel: int = wizy_voice_channels[0] #TODO : later will 1) load all voice channels from json 2)assign each wizy voice channel for each server
      self.default_wizy_chat_ch_ai_type: str = 'deep'
      self.wizy_chat_ch_ai_types: list = ['gpt','gemini', 'deep'] 
      self.default_auto_played_track_type: str = 'mmochill' #lofi | mmochill | mmo&anime | orsmix #TODO: make type per guild
      self.auto_played_tracks: dict = {'lofi': "/lofi", 'mmochill': '/mmochill', 'mmoanime': '/mmoanime', 'orsmix': '/orsmix', 'holyquran': '/holyquran'}  #lofi | chillmmo | mmo | orsmix #TODO: make type per guild
      self.alone_increment_val_sec =5
      self.wizy_alone_threshold_sec = 300 #5 minutes
      self.guilds_not_playing_timer: dict[discord.guild.id, int] = {}
      self.connected_to_wizy_voice_per_guild: dict[discord.guild.id, int] = {}
      self.resume_chill_if_free.start()
      self.auto_memequote_sender_task.start()
      # self.play_chill_loop.start()
      self.load_cfg.start()
      self.send_master_dm_msg_on_init.start()
      #TODO: 1) each guild wizy joins will have minimum of 3 wizy channels: feed,voice,chat  
      #TODO: 2)after x amount of hours if wizy is idle he will go back to his home i.e.(wizy voice channel) and maybe start some chill music loop

   async def on_ready(self):
      """
      Handles bot's ready event.
      
      This method is called when the bot successfully connects to Discord. It:
      - Syncs slash commands
      - Initializes bot counters and timers
      - Prints connection confirmation
      """
      #next line needed to enable slash commands (slash commands are type of interactions not ctx or message or normal command any more)
      await self.tree.sync()
      await util.fill_bot_counters_n_timers()
      print(f"\n\n Bot '{self.user}' Sucessfully connected to Discord!\n\n")

   @tasks.loop(seconds= 10, count= 1) #do once
   async def load_cfg(self):
      """
      Loads bot configuration settings.
      
      This task runs once on startup to load configuration from either
      a custom config file or the default configuration.
      """
      # load the configs 
      # (loads default config file if no custom config is found #TODO: (later either all servers config in one json or each server will have their config class and config json))
      Configs.cfg_load()
      
   @tasks.loop(seconds= 20, count= 1) #do once
   async def send_master_dm_msg_on_init(self):
      """
      Sends initialization message to the bot master.
      
      This task runs once on startup to send a detailed status message
      to the bot's master user via DM.
      """
      full_dm_msg, target_dm_channel = await util.await_me_maybe(util.prepare_bot_info_dm_on_init())
      await target_dm_channel.send(full_dm_msg[0])  #send first portion of the msg
      await target_dm_channel.send(full_dm_msg[1])  #send the rest of dm msg to bot master
            
   @send_master_dm_msg_on_init.before_loop
   async def wait_send_until_ready(self):
      await self.wait_until_ready()
   

   @tasks.loop(seconds= 5)
   async def  resume_chill_if_free(self):
      """
      Periodically checks and resumes chill music if bot is free.
      
      This task runs every 5 seconds to check if the bot is alone in voice
      channels and should resume playing chill music.
      """
      await util.handle_wizy_free_timer(self.guilds, self.guilds_not_playing_timer, self.alone_increment_val_sec, self.wizy_alone_threshold_sec)

   @resume_chill_if_free.before_loop
   async def wait_bot_ready(self):
      await self.wait_until_ready()
   

   @tasks.loop(minutes= default_feed_channel_frequency_minutes)#def= 2 hours
   async def auto_memequote_sender_task(self):
      """
      Periodically sends random memes and quotes to feed channels.
      
      This task runs at the configured interval to send random content
      to designated feed channels. Can operate in normal or special mode.
      """
      await util.send_rand_quote_meme(is_special= True if self.auto_memequote_state >= 2 else False)

   @auto_memequote_sender_task.before_loop
   async def before_start_auto_memequote_sender(self):
      #TESTING
      print(f"\n\n\n\n\n TESTING#####################   \n\n\n your auto_memequote_sender state is : {self.auto_memequote_state} \n\n\n\n ######################")
      #TESTING
      await self.wait_until_ready()

   async def set_memequote_sender_frequency(self, _interval_minutes: int = default_feed_channel_frequency_minutes ): 
      """
      Updates the frequency of the auto meme/quote sender task.
      
      Args:
          _interval_minutes (int): New interval in minutes between sends
      """
      self.auto_memequote_sender_task.change_interval(minutes= _interval_minutes)

   async def change_auto_memequote_sender_state(self, state:int = None ) -> bool :
      """
      Changes the state of the auto meme/quote sender.
      
      Args:
          state (int, optional): New state to set. If None, toggles current state.
              
      Returns:
          bool: The new state of the auto meme/quote sender
      """
      updated_state = util.control_auto_memequote_task(self.auto_memequote_state, self.auto_memequote_sender_task)
      self.auto_memequote_state = updated_state   
      return self.auto_memequote_state

   # @tasks.loop(seconds= 1)
   # async def play_chill_loop(self, target_ch: discord.VoiceChannel= None):
  
   #    # #when booting up bot make him join admin room (only for my server wizy home!)
   #    # targetVchannel = self.get_channel(self.default_voice_channel) if target_ch == None else target_ch
   #    # server = targetVchannel.guild

   #    # if server.voice_client is not None :
   #    #    server.voice_client.disconnect()

   #    # await targetVchannel.connect()

   #    # if not server.voice_client.is_playing() :
   #    #    await util.play_chill_track(server)


   # @play_chill_loop.before_loop
   # async def before_play_chill(self):
   #    await self.wait_until_ready()

   # async def stop_play_chill_loop(self):
   #    self.play_chill_loop.cancel()
   # async def start_play_chill_loop(self):
   #    self.play_chill_loop.start()
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
   """
   Performs pre-boot setup tasks for the bot.
   
   Args:
       _main_file (str): Path to the main bot file
       
   Returns:
       tuple: (log_std, log_discord) File handlers for standard and Discord logging
   """
   
   if sys.platform.startswith('linux'): # change process name on linux cuz it's hard on win :(
      setproctitle.setproctitle("bot_wizy_discord.py") 
   
   util.cd_to_main_dir(_main_file) #so log files will be written in the same project dir
   log_std = open("std.log" , 'a') #logs all stderr and stdout and discord.py msgs
   log_discord = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')#logs only discord.py msgs
   return log_std , log_discord
   
#------------------------------------------------------------------------------------------------------------------------------------------#
def boot_bot(main_file: str) :
   """
   Initializes and starts the Discord bot.
   
   Args:
       main_file (str): Path to the main bot file
       
   Note:
       Handles different logging configurations based on production status.
   """
   log_std, log_discord = pre_boot_setup(main_file)
   if 'IS_PRODUCTION' in os.environ and os.environ['IS_PRODUCTION'] == '1' :
      with contextlib.redirect_stdout(log_std):
         with contextlib.redirect_stderr(log_std):
            bot.run(keys.Token_gpteousBot , log_handler= log_discord, log_level= logging.INFO)#default logging level is info
   else :
      bot.run(keys.Token_gpteousBot , log_level= logging.DEBUG) #default handler is stdout , debug log level is more verbose!
#------------------------------------------------------------------------------------------------------------------------------------------#
