"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : #
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
with open(r"../openai_apiKey.txt" , 'r') as openaifile :
   openaiAPI_KEY = openaifile.read().strip()
   
with open(r"../discordBotToken_Gpteous.txt" , 'r') as discordfile :
   Token_gpteousBot = discordfile.read().strip()
   
with open(r"../bard_apiKey.txt" , 'r') as bardfile : #actually is  a coockie named : "__Secure-1PSID" from bard website coockies
   bardAPI_KEY = bardfile.read().strip() 