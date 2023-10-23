"""
                          Coder : Omar
                          Version : v2.5.3B
                          version Date :  23 / 10 / 2023
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
#(DONE)TODO : show embedded links in bard answer 
#(DONE)TODO : show  images in Wizard special channel
#(DONE)TODO : send msg in parts is it exceeds max size in bot special channel
#(DONE)TODO : connect to cdn that has memes / quotes  and set on_time() event to send to chat chill and ask-wizard-channel (duplicated in todo discord channel)
#(DONE)TODO : show embedded images in bard answer (shows with the links as links :( ))
#(DONE)TODO : make message fragmenter function for msg and links msg  and images msg in utils_bot.py
#(DONE)TODO : replace all your manual auto meme/quote sender queue logic with this (let bot event loop handle it auto!)(no need even for acync event control var): https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html#

#TODO : use https://rapidapi.com/ 
#TODO : complete tracks queue class and it's two commands look(https://stackoverflow.com/questions/61276362/how-to-play-the-next-song-after-first-finished-discord-bot)
#TODO : complete your quote lib fork and make it fully async. 
#TODO : add command : provides the ability for other SERVERS  using wizard bot to add their own '#ask-the-wizard-channel' just by  typing  `add/deleteWizardChannel` command : this command takes channel id and appends it to wizard_channels_ids tuple  ( check if you need any id for the server it self mostly not)
#TODO : implement new bard feature i.e.( upload image and ask about it ) in your bot since it's now available and Bard API wrapper v0.1.27 now also supports it
#TODO : send Embed in parts/pages if it exceeds max size  (6000char) or exceeduts max fields (25 field)
#TODO : wizard bot sqlite DB : design and connect the db with bot code
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

import keys
import init_bot
import utils_bot
import events_bot
import pyrandmeme2
import commands_bot
import asyncforismatic
# import bard_key_refresh #TODO
# import help_bot #TODO

init_bot.boot_bot()