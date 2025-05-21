"""
                          Coder : Omar
                          Version : v2.5.6B
                          version Date :  26 / 04 / 2025
                          Code Type : python | Discrod | GEMINI | HTTP | ASYNC
                          Title : main code for Discord Bot (with generative AI)
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]
"""

#TODO : Documentaion for functions / classes and repo readme.md

#(DONE)TODO : make bot see prev messages (use session) 
#(DONE)TODO : talk to bot by mention him
#(DONE)TODO : talk to bot in specific channel no need to mention or trigger him by command just send the question as plain message
#(DONE)TODO :  reply to his message (take the content of replayed message and respond accordingly to it + new message)
#(DONE)TODO : use SESSION with ASYNC GEMINI ( contact GEMINIAPI maker or raise issue in their repo)(I was  kinda  wrong)
#(DONE)TODO : show embedded links in gemini answer
#(DONE)TODO : show  images in Wizard special channel
#(DONE)TODO : send msg in parts is it exceeds max size in bot special channel
#(DONE)TODO : connect to cdn that has memes / quotes  and set on_time() event to send to chat chill and ask-wizard-channel (duplicated in todo discord channel)
#(DONE)TODO : show embedded images in gemini answer (shows with the links as links :( ))
#(DONE)TODO : make message fragmenter function for msg and links msg  and images msg in utils_bot.py
#(DONE)TODO : replace all your manual auto meme/quote sender queue logic with this (let bot event loop handle it auto!)(no need even for acync event control var): https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html#
#(DONE)TODO : add command to switch between GEMINI mode and poe-GPT mode

#TODO : use https://rapidapi.com/
#TODO : complete tracks queue class and it's two commands look(https://stackoverflow.com/questions/61276362/how-to-play-the-next-song-after-first-finished-discord-bot)
#TODO : complete your quote lib fork and make it fully async.
#TODO : add command : provides the ability for other SERVERS  using wizard bot to add their own '#ask-the-wizard-channel', '#wizy-voice_channel', '#wizy-feed-channel' just by  typing  `add/deleteWizardChannel` command : this command takes channel id and appends it to wizard_channels_ids tuple  ( check if you need any id for the server it self mostly not)
#TODO : implement new gemini feature i.e.( upload image and ask about it ) in your bot since it's now available and GEMINI API wrapper v0.1.27 now also supports it
#TODO : send Embed in parts/pages if it exceeds max size  (6000char) or exceeduts max fields (25 field)
#TODO : wizard bot sqlite DB : design and connect the db with bot code
#TODO : OOP it more and handle errors!
#TODO : save last conversation id (load it in init_bot.py) in text file and add command to start new conv or  default is to continue old
#TODO : add read text in audio feature and ability for bot to join voice chat
#TODO : ADD voice to text feature to enable full voice chat feature between bot and island server's users
#TODO : add and test poe-API (starred at GH)
#TODO : Edit your gemini args and prompt to send full arabic query to gemini (gemini now has arabic lang suuport )
#TODO : complete moving from old un-official bard api to new better gemini(ex-bard) api 
#TODO: for commands & events using deepSeek AI: add attach files/images feature cuz deepseek supports it!
#       the issue is that gemini.get_answer() itself doesnt take any args put the query prompt (can easly add new param but prefer search more on this first)

#NOTE : the rest of tasks is on mod's channel 'todo' in my narol's server + (to find all TODO s search via global vs code search )
#NOTE : #Heartbeating handled automatically (modify from gateway class)

import keys
import configs
import help_bot
import init_bot
import utils_bot
import events_bot
import pyrandmeme2
import commands_bot
import asyncforismatic

init_bot.boot_bot(__file__)















