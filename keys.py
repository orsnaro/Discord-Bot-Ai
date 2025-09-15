"""
                          Coder : Omar
                          Version : v2.5.9B
                          version Date :  15 / 09 / 2025
                          Code Type : python | Discrod | GEMINI | HTTP | ASYNC
                          Title : #
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]

"""
import os
import json

keysFileOk : bool = os.path.isfile("../wizy_keys.json")

if( keysFileOk ):
   with open('../wizy_keys.json', 'r') as keysFile:

      keys_dict: str = json.load(keysFile)

      openaiAPI_KEY    = keys_dict['OPENAI_API_KEY']
      openaiAPI_ORG_ID = keys_dict['OPENAI_ORG_ID']
      deepseekAPI_KEY    = keys_dict['DEEPSEEK_API_KEY']
      Token_gpteousBot = keys_dict['DISCORDBOTTOKEN_GPTEOUS']
      geminiAPI_KEY      = keys_dict['GEMINI_APIKEY']
      geminiGmail        = keys_dict['GEMINI_GMAIL']
      geminiGmail_KEY    = keys_dict['GEMINI_GMAILPASS']

else : #if json file is not there (the ones with default None val are not super necessary)
   openaiAPI_KEY    = os.environ['OPENAI_API_KEY']
   openaiAPI_ORG_ID = os.environ['OPENAI_ORG_ID']
   deepseekAPI_KEY    = os.environ['DEEPSEEK_API_KEY']
   Token_gpteousBot = os.environ['DISCORDBOTTOKEN_GPTEOUS']
   geminiAPI_KEY      = os.environ['GEMINI_APIKEY']
   geminiGmail        = os.environ.get('GEMINI_GMAIL', None) 
   geminiGmailK_KEY   = os.environ.get('GEMINI_GMAILPASS', None) 