"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Events code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from init_bot import *
from utils_bot import ask_bard , check_msg
#------------------------------------------------------------------------------------------------------------------------------------------#
# @bot.event
# async def on_any_event_update_DB_buffer():... #TODO if bot does any action or any thing trigger it save needed info in your own DB for later....
# #if buffer surpasses certain size | bot is acitve for certain time  flush all to db 
#------------------------------------------------------------------------------------------------------------------------------------------#


# on_message_in_wizard_channel = discord.on_message  #TODO if alias work use instead to diffrentiate between many > on message events
@bot.event #if used @client.event bot could reply to him self i.e.(trigger him self ) which could cause recursion and replay loop issue
async def on_message(message):
	wizardChannelId = 1118953370510696498 #🧙ask-the-wizard 
	wizard_ch_msg = message 
 
	if await check_msg(wizard_ch_msg , targetChannelId= wizardChannelId): 
    #NOTE : if want to disable talk to all bots in also check if author.bot != True
		# print (wizard_ch_msg.content)
		ask_bard_task =  bot.loop.create_task( ask_bard(user_query= wizard_ch_msg.content , user_name= wizard_ch_msg.author.display_name) ) #if error replace display_name with name
		task_response : tuple = await ask_bard_task
		bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** \n"
		full_response = bot_msg_header + task_response[0]
		await message.reply(content= full_response  , mention_author= True)
		#TODO : ADD REPLY MESSAGES WITh LINKS IF THERE IS AND IMAGES IF THERE IS 
  
	await bot.process_commands(message) #add this to prevent on_message() from blocking bot.command
#------------------------------------------------------------------------------------------------------------------------------------------#

