"""
                          Coder : Omar
                          Version : v2.5.6B
                          version Date :  26 / 04 / 2025
                          Code Type : python | Discrod | GEMINI | GPT | DEEPSEEK | HTTP | ASYNC
                          Title : Read Bot config file and Initialize the config variables
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]
"""

import os
import json

class Configs :
   '''Any configs + almost all global variables are stored here'''

   config_json_dict: dict = {}
   def __init__(self): pass

   @classmethod
   def cfg_load(cls):
      cfgFileOk: bool = os.path.isfile(r'./config.json')

      if (cfgFileOk):
         with open(file= r'./config.json' , mode= 'r') as cfgFile:
            cls.config_json_dict: dict = json.load(cfgFile)
      else: #no prev config file load the default
         with open(file= r'./default_cfg.json' , mode= 'r') as cfgFile:
            cls.config_json_dict: dict = json.load(cfgFile)

   @classmethod
   def cfg_save(cls):
      with open(file= r'./config.json', mode= 'w') as cfgFile:
         json.dump(cls.config_json_dict, cfgFile)
