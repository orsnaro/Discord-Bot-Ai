"""
                          Coder : Omar
                          Version : v2.5.2B
                          version Date :  23 / 10 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : #
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
                     
"""
import os

file1ok : bool = os.path.isfile("../discordBotToken_Gpteous.txt")
file2ok : bool = os.path.isfile("../openai_apiKey.txt")
file3ok : bool = os.path.isfile("../bard_apiKey.txt")
file4ok : bool = os.path.isfile("../bard_gmail.txt")
file5ok : bool = os.path.isfile("../bard_gmailPass.txt")

if( file1ok and file2ok and file3ok and file4ok and file5ok ):
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

	Token_gpteousBot = os.environ['DISCORDBOTTOKEN_GPTEOUS']

	bardAPI_KEY = os.environ['BARD_APIKEY'] 

	bardGmail = os.environ['BARD_GMAIL'] 

	bardGmail_KEY = os.environ['BARD_GMAILPASS']