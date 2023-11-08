"""
                          Coder : Omar
                          Version : v2.5.5B
                          version Date :  8 / 11 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Events code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""

from init_bot import *
from utils_bot import ask_bard, ask_gpt, check_msg, send_rand_quote_meme, supress_msg_body_url_embeds, prepare_imgs_msg, prepare_links_msg, prepare_send_wizard_channel_ans_msg, sub_sections_msg_sending_ctrl
#------------------------------------------------------------------------------------------------------------------------------------------#
# @bot.event
# async def on_any_event_update_DB_buffer():... #TODO if bot does any action or any thing trigger it save needed info in your own DB for later....
# #if buffer surpasses certain size | bot is acitve for certain time  flush all to db
#------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------#
#NOTE: this controls the free chat channel of wizy (TODO:make any server assign their wizy chat channel command)
@bot.event #if used @client.event bot could reply to him self i.e.(trigger him self ) which could cause recursion and replay loop issue
async def on_message(message: discord.Message):
   wizard_ch_msg: discord.Message = message
    
   try: #if bard or gpt not available handle that
      
      if await check_msg(wizard_ch_msg , targetChannelId= wizard_channels):
      #NOTE : if want to disable talk to all bots in also check if author.bot != True in check_msg() func
      
         print(f"\n\n\n\n\n TESTING###################    {bot.wizy_chat_ch_ai_type}       \n\n ################\n\n\n\n\n ")#TESTING
            
         if bot.wizy_chat_ch_ai_type == 'gpt':
            ask_gpt_task =  bot.loop.create_task( ask_gpt(user_query= wizard_ch_msg.content,
                                                            user= wizard_ch_msg.author, is_wizy_ch= True) 
                                                )
            task_response : tuple = await ask_gpt_task
            
         elif bot.wizy_chat_ch_ai_type == 'bard':
            ask_bard_task =  bot.loop.create_task( ask_bard(user_query= wizard_ch_msg.content,
                                                            user= wizard_ch_msg.author) 
                                                ) 
            task_response : tuple = await ask_bard_task
            

         is_bard = True if bot.wizy_chat_ch_ai_type == 'bard' else False
         await prepare_send_wizard_channel_ans_msg( task_response , wizard_ch_msg, is_bard= is_bard)
         
         
         if bot.wizy_chat_ch_ai_type == 'bard': #NOTE: for gpt3.5 he cant send links nor images as I know
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
                  
            await sub_sections_msg_sending_ctrl( wizard_ch_msg,
                                                final_links,
                                                lnk1_len,
                                                final_imgs,
                                                have_imgs,
                                                have_links
                                                )
            
         await aio.sleep(5)
         
   except:
      await message.delete(delay= 15)
      await message.reply(content= "Wizy says He is not Here comeback later :face_with_peeking_eye: ",
                          delete_after= 15
                          )



   await bot.process_commands(message) #add this to prevent on_message() from blocking bot.command
   del message
#------------------------------------------------------------------------------------------------------------------------------------------#

