"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : main code for Discord Bot (with generative AI)
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
#TODO : OOP IT more and handle errors!
#TODO : make bot see prev messages (use session)
#TODO : talk to bot by mention him or reply to his message (take the content of replayed message and respond accordingly to it + new message)
#TODO : wizard bot sqlite DB : design and connect the db with bot code
#TODO : use google translator API
#TODO : use SESSION with ASYNC BARD ( contact BardAPI maker or raise issue in theire repo)
#TODO : show embedded images in bard answer 
#TODO : show embedded links in bard answer 
#TODO : rest of tasks is on mod's channel (todo) in my narol's server + (to find all TODO s search via global vs code search )

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
