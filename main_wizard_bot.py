"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : main code for Discord Bot (with generative AI)
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
#TODO : Documentaion for functions / classes and repo readme.md
#(DONE)TODO : make bot see prev messages (use session)
#(DONE)TODO : talk to bot by mention him  
#(DONE)TODO : talk to bot in specific channel no need to mention or trigger him by command just send the question as plain message
#(DONE)TODO :  reply to his message (take the content of replayed message and respond accordingly to it + new message)
#(DONE)TODO : use SESSION with ASYNC BARD ( contact BardAPI maker or raise issue in their repo)(I was  kinda  wrong)
#(DONE)TODO : show embedded images in bard answer 
#(DONE)TODO : show embedded links in bard answer 
#TODO : save last conversation id (load it in init_bot.py) in text file and add command to start new conv or  default is to continue old 
#       the issue is that bard.get_answer() itself doesnt take any args put the query prompt (can easly add new param but prefer search more on this first)
#TODO : wizard bot sqlite DB : design and connect the db with bot code
#TODO : use google translator API
#TODO : OOP it more and handle errors!
#TODO : connect to cdn that has memes / quotes  and set on_time() event to send to chat chill and ask-wizard-channel (duplicated in todo discord channel)
#TODO : the rest of tasks is on mod's channel 'todo' in my narol's server + (to find all TODO s search via global vs code search )

#NOTE : embed field size is limited to 1024 words
#NOTE : #Heartbeating handled automatically (modify from gateway class) 
#NOTE : BARD API is the one used now due to connection and belling issue beteen GPT API and my country (egypt)

import init_bot
import keys
import utils_bot
import events_bot
import commands_bot
import help_bot
#------------------------------------------------------------------------------------------------------------------------------------------#

init_bot.bot.run(keys.Token_gpteousBot)
