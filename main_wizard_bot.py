"""
                          Coder : Omar
                          Version : v2.5B
                          version Date :  2 / 7 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : main code for Discord Bot (with generative AI)
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
#TODO TODO TODO : DO THIS BEFORE any other big task -> (FINSIH THOSE & FIX BIG BUGS ) THEN => MIGRATE TO PYCORD 
#TODO : Documentaion for functions / classes and repo readme.md
#(DONE)TODO : make bot see prev messages (use session)
#(DONE)TODO : talk to bot by mention him  
#(DONE)TODO : talk to bot in specific channel no need to mention or trigger him by command just send the question as plain message
#(DONE)TODO :  reply to his message (take the content of replayed message and respond accordingly to it + new message)
#(DONE)TODO : use SESSION with ASYNC BARD ( contact BardAPI maker or raise issue in their repo)(I was  kinda  wrong)
#(DONE)TODO : show embedded links in bard answer 
#(DONE)TODO : show  images in Wizard special channel
#(DONE)TODO : send msg in parts is it exceeds max size in bot special channel
#(DONE)TODO : connect to cdn that has memes / quotes  and set on_time() event to send to chat chill and ask-wizard-channel (duplicated in todo discord channel)


#TODO : send Embed in parts/pages if it exceeds max size  (6000char) or exceeds max fields (25 field)
#TODO : show embedded images in bard answer (shows with the links)
#TODO : wizard bot sqlite DB : design and connect the db with bot code
#TODO : use google translator API
#TODO : OOP it more and handle errors!
#TODO : save last conversation id (load it in init_bot.py) in text file and add command to start new conv or  default is to continue old 
#TODO : complete bard_key_refresh.py
#TODO : add read text in audio feature and ability for bot to join voice chat
#TODO : ADD voice to text feature to enable full voice chat feature between bot and island server's users
#TODO : add and test poe-API (starred at GH)
#TODO : add command to switch between BARD mode and poe-GPT mode 
#TODO : Edit your bard args and prompt to send full arabic query to bard (bard now has arabic lang suuport )

#       the issue is that bard.get_answer() itself doesnt take any args put the query prompt (can easly add new param but prefer search more on this first)

#NOTE : the rest of tasks is on mod's channel 'todo' in my narol's server + (to find all TODO s search via global vs code search )
#NOTE : #Heartbeating handled automatically (modify from gateway class) 
#NOTE : BARD API is the one used now due to connection and belling issue beteen GPT API and my country (egypt)

import init_bot
import keys
import utils_bot
import events_bot
import commands_bot
import help_bot
import pyrandmeme2
#------------------------------------------------------------------------------------------------------------------------------------------#

init_bot.bot.run(keys.Token_gpteousBot)
