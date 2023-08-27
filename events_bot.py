"""
                          Coder : Omar
                          Version : v2.5.2B
                          version Date :  17 / 8 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Events code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""

from init_bot import *
from utils_bot import ask_bard , check_msg ,send_rand_quote_meme , supress_msg_body_url_embeds , prepare_imgs_msg , prepare_links_msg , prepare_send_wizard_channel_ans_msg , sub_sections_msg_sending_ctrl
#------------------------------------------------------------------------------------------------------------------------------------------#
# @bot.event
# async def on_any_event_update_DB_buffer():... #TODO if bot does any action or any thing trigger it save needed info in your own DB for later....
# #if buffer surpasses certain size | bot is acitve for certain time  flush all to db 
#------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------#
# on_message_in_wizard_channel = discord.on_message  #TODO if alias work use instead to diffrentiate between many > on message events
@bot.event #if used @client.event bot could reply to him self i.e.(trigger him self ) which could cause recursion and replay loop issue
async def on_message(message):
	wizard_ch_msg = message 
	if await check_msg(wizard_ch_msg , targetChannelId= wizard_channels):
    #NOTE : if want to disable talk to all bots in also check if author.bot != True in check_msg() func
		ask_bard_task =  bot.loop.create_task( ask_bard(user_query= wizard_ch_msg.content , user_name= wizard_ch_msg.author.display_name) ) #if error replace display_name with name
		task_response : tuple = await ask_bard_task
  
		await prepare_send_wizard_channel_ans_msg( task_response , wizard_ch_msg )

		final_imgs  , final_links , lnk1_len = None , None , -1#lnk1_len will be needed in sub_sections_msg_sending_ctrl()
		have_links = False
		if task_response is not None and len(task_response) >= 2 and len(task_response[1]) > 0 :
			final_links , task_response , lnk1_len = prepare_links_msg(task_response)
			if len(final_links) > 0:
				have_links = True

		have_imgs = False
		if task_response is not None and len(task_response) >= 3 and len(task_response[2]) > 0 :
			final_imgs = prepare_imgs_msg(task_response)
			if len(final_imgs) > 0:
				have_imgs = True
    
		await sub_sections_msg_sending_ctrl( wizard_ch_msg  ,  final_links , lnk1_len , final_imgs ,  have_imgs	 , have_links)
		await aio.sleep(5)
		
		
		
  
	await bot.process_commands(message) #add this to prevent on_message() from blocking bot.command
	del message
#------------------------------------------------------------------------------------------------------------------------------------------#

