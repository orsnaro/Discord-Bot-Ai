"""
                          Coder : Omar
                          Version : v2.5.11B
                          version Date :  3 / 11 / 2025
                          Code Type : python | Discrod | GEMINI | GPT | DEEPSEEK | HTTP | ASYNC
                          Title : Read Bot config file and Initialize the config variables
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]
"""

import os
import json

class Configs :
   """
   Configuration management class for the Discord bot.
   
   This class handles loading, storing, and saving configuration settings for the bot.
   It maintains a dictionary of configuration values and provides methods to load from
   either a custom config file or default configuration.
   
   Attributes:
       config_json_dict (dict): Dictionary containing all configuration settings.
   """

   config_json_dict: dict = {}
   def __init__(self): pass

   @classmethod
   def cfg_load(cls):
      """
      Loads configuration settings from either config.json or default_cfg.json.
      
      This method attempts to load configuration from config.json first. If that file
      doesn't exist, it falls back to loading from default_cfg.json. The loaded
      configuration is stored in the class's config_json_dict.
      
      Note:
          The configuration file should be in JSON format and located in the root directory.
      """
      cfgFileOk: bool = os.path.isfile(r'./config.json')

      if (cfgFileOk):
         with open(file= r'./config.json' , mode= 'r') as cfgFile:
            cls.config_json_dict: dict = json.load(cfgFile)
      else: #no prev config file load the default
         with open(file= r'./default_cfg.json' , mode= 'r') as cfgFile:
            cls.config_json_dict: dict = json.load(cfgFile)

   @classmethod
   def cfg_save(cls):
      """
      Saves the current configuration settings to config.json.
      
      This method writes the current configuration stored in config_json_dict
      to the config.json file in the root directory. The configuration is saved
      in JSON format.
      
      Note:
          This will overwrite any existing config.json file.
      """
      with open(file= r'./config.json', mode= 'w') as cfgFile:
         json.dump(cls.config_json_dict, cfgFile)
