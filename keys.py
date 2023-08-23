"""
                          Coder : Omar
                          Version : v2.5.2B
                          version Date :  17 / 8 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : #
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
                     
"""
import os

if(os.path.isfile("../discordBotToken_Gpteous.txt")):
	with open(r"../openai_apiKey.txt" , 'r') as openaifile :
		openaiAPI_KEY = openaifile.read().strip()
		
	with open(r"../discordBotToken_Gpteous.txt" , 'r') as discordfile :
		Token_gpteousBot = discordfile.read().strip()
		
	with open(r"../bard_apiKey.txt" , 'r') as bardfile : #actually is  a coockie named : "__Secure-1PSID" from bard website coockies
		bardAPI_KEY = bardfile.read().strip() 
		
	with open(r"../bard_gmail.txt" , 'r') as bardfile : 
		bardGmail = bardfile.read().strip() 
		
	with open(r"../bard_gmailPass.txt" , 'r') as bardfile : 
		bardGmail_KEY = bardfile.read().strip() 
else :
	openaiAPI_KEY = os.environ['OPENAI_APIKEY']

	oken_gpteousBot = os.environ['DISCORDBOTTOKEN_GPTEOUS']

	bardAPI_KEY = os.environ['BARD_APIKEY'] 

	bardGmail = os.environ['BARD_GMAIL'] 

	bardGmail_KEY = os.environ['BARD_GMAILPASS']