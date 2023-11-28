"""
                          Coder : Omar
                          Version : v2.5.5B
                          version Date :  8 / 11 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : #
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]

"""
import os
import json

keysFileOk : bool = os.path.isfile("../wizy_keys.json")

if( keysFileOk ):
   with open('../wizy_keys.json', 'r') as keysFile:

      keys_dict: str = json.load(keysFile)

      openaiAPI_KEY    = keys_dict['OPENAI_API_KEY']
      openaiAPI_ORG_ID = keys_dict['OPENAI_ORG_ID']
      Token_gpteousBot = keys_dict['DISCORDBOTTOKEN_GPTEOUS']
      bardAPI_KEY      = keys_dict['BARD_APIKEY']
      bardAPI_KEY2     = keys_dict['BARD_APIKEY2']
      bardAPI_KEY3     = keys_dict['BARD_APIKEY3']
      bardGmail        = keys_dict['BARD_GMAIL']
      bardGmail_KEY    = keys_dict['BARD_GMAILPASS']

else : #if json file is not there
   openaiAPI_KEY    = os.environ['OPENAI_API_KEY']
   openaiAPI_ORG_ID = os.environ['OPENAI_ORG_ID']
   Token_gpteousBot = os.environ['DISCORDBOTTOKEN_GPTEOUS']
   bardAPI_KEY      = os.environ['BARD_APIKEY']
   bardAPI_KEY2     = os.environ['BARD_APIKEY2']
   bardAPI_KEY3     = os.environ['BARD_APIKEY3']
   bardGmail        = os.environ['BARD_GMAIL']
   bardGmailK_KEY   = os.environ['BARD_GMAILPASS']
