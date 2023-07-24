"""
                          Coder : Omar
                          Version : v2.5.1B
                          version Date :  24 / 7 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Events code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
#TODO :  make message fragmenter function for  msg and links msg and img msg  in utils_bot.py

from init_bot import *
from utils_bot import ask_bard , check_msg ,send_rand_quote_meme , supress_msg_body_url_embeds , prepare_imgs_msg , prepare_links_msg , prepare_send_wizard_channel_ans_msg
#------------------------------------------------------------------------------------------------------------------------------------------#
# @bot.event
# async def on_any_event_update_DB_buffer():... #TODO if bot does any action or any thing trigger it save needed info in your own DB for later....
# #if buffer surpasses certain size | bot is acitve for certain time  flush all to db 
#------------------------------------------------------------------------------------------------------------------------------------------#
trigger_times = []
#------------------------------------------------------------------------------------------------------------------------------------------#
# on_message_in_wizard_channel = discord.on_message  #TODO if alias work use instead to diffrentiate between many > on message events
@bot.event #if used @client.event bot could reply to him self i.e.(trigger him self ) which could cause recursion and replay loop issue
async def on_message(message):
 
	await send_rand_quote_meme( message )
 
	wizard_ch_msg = message 
	if await check_msg(wizard_ch_msg , targetChannelId= wizard_channels):
    #NOTE : if want to disable talk to all bots in also check if author.bot != True in check_msg() func
		ask_bard_task =  bot.loop.create_task( ask_bard(user_query= wizard_ch_msg.content , user_name= wizard_ch_msg.author.display_name) ) #if error replace display_name with name
		task_response : tuple = await ask_bard_task
  
		await prepare_send_wizard_channel_ans_msg( task_response , wizard_ch_msg )

		if task_response is not None and len(task_response) >= 2 and len(task_response[1]) > 0 :
			final_links , task_response = prepare_links_msg(task_response)
			await message.reply(content= final_links  , mention_author= False)

		if task_response is not None and len(task_response) >= 3 and len(task_response[2]) > 0 :
			final_imgs = prepare_imgs_msg(task_response)
			await message.reply(content= final_imgs  , mention_author= False)

	await bot.process_commands(message) #add this to prevent on_message() from blocking bot.command
	del message
#------------------------------------------------------------------------------------------------------------------------------------------#

