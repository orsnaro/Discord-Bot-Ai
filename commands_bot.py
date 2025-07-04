"""
                          Coder : Omar
                          Version : v2.5.7B
                          version Date :  6 / 06 / 2025
                          Code Type : python | Discrod | GEMINI | HTTP | ASYNC
                          Title : Commands Code for Discord bot
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]
"""
from init_bot import *
from utils_bot import ask_deepSeek, ask_gemini, ask_gpt, get_rand_greeting, prepare_discord_embed, prepare_quote
from utils_bot import check_msg, get_new_reply_prompt, YTDLSource, await_me_maybe
import keys
from typing import List
#------------------------------------------------------------------------------------------------------------------------------------------#
#disabled default global help message  from bot constructor then override default by this command
slash_cmd_ok_msg = "OK ✅"
@bot.hybrid_command(name="help")
@commands.cooldown(1, 5)
async def help( ctx: commands.Context ):
   """
   Displays the bot's help message with command information.
   
   This command overrides the default help command and displays a custom help message
   split into two parts. It includes a cooldown of 5 seconds between uses.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   async with ctx.typing():
      bot_help_msg_p1: discord.Message = await ctx.reply(content= help_bot.override_help_msgP1)
      await ctx.send(content= help_bot.override_help_msgP2)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="boringwizard", help= "wizy sends a random meme")
@commands.cooldown(1, 5)
async def boring( ctx: commands.Context ):
   """
   Sends a random meme to the channel.
   
   This command fetches and sends a random meme with a wizard-themed title.
   Includes a cooldown of 5 seconds between uses.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   await ctx.send(embed= await pyrandmeme2(_title= "Some Wizardy Humor👻"))

   #if used via slash command will not add reaction cuz it raises discord error msg not found
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizyawakened", help= "wizy wakes you up to the truth!")
@commands.cooldown(1, 5)
async def awake( ctx: commands.Context ):
   """
   Posts content from r/Palestine subreddit.
   
   This command fetches and posts content from the Palestine subreddit,
   including handling video content if present. Includes a cooldown of 5 seconds.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   ps_post_get_task = await bot.loop.create_task(palestina_free(_title= ":flag_ps: *r/Palestine* :flag_ps:"))
   ps_post_embed_is_video, ps_post_data, ps_post_url = await await_me_maybe(ps_post_get_task)

   await util.final_send_special_ps(ctx, ps_post_embed_is_video, ps_post_data, ps_post_url)

   #if used via slash command will not add reaction cuz it raises discord error msg not found
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wisewiz", help= 'wizy sends a random Quote (quote of type 1 for now glitches slash cmd)')
async def wise( ctx: commands.Context):
   """
   Sends a random inspirational quote.
   
   This command fetches and sends a random quote. Note that type 1 quote API
   is not async and may timeout with slash commands. Includes retry logic
   with a limit of 10 attempts.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   quote_api = 1 if ctx.interaction else 0 #type 1 quote api is not async and timesout with slash commands
   prepare_quote_task =  bot.loop.create_task(prepare_quote(invoker= quote_api, retrylimit= 10)) #invoker == 0 cuases error if used by a slash command (probably cuz its not async)
   quotes = await prepare_quote_task
   await ctx.reply( embed= quotes ) if quote_api == 1 else await ctx.reply( quotes )
#------------------------------------------------------------------------------------------------------------------------------------------#
allowed_roles_togglerandom = {
                              "ULT! SAQF": 889532272989053019,
                              "ULT! ADMIN": 889931295365414993,
                              "ULT! CODER": 1014300476814147656,
                              "Spirits Overlord": 1118266805006389289
                              } #check by id not the names cuz they're missing emojies
allowed_roles_quotesz = {"ULT! SAQF": 889532272989053019,
                         "ULT! ADMIN": 889931295365414993,
                         "ULT! CODER": 1014300476814147656,
                         "Spirits Overlord": 1118266805006389289
                         } #check by id not the names cuz they're missing emojies
allowed_roles_change_ai = {"ULT! SAQF": 889532272989053019,
                         "ULT! ADMIN": 889931295365414993,
                         "ULT! CODER": 1014300476814147656,
                         "Land MASTERS": 890586687623798834,
                         "ISLE! Booster": 1013995284470169761,
                         "Spirits Overlord": 1118266805006389289
                         } #check by id not the names cuz they're missing emojies
@bot.hybrid_command(name="togglerandom", help= 'toggles & controls the auto meme-quote sender feature & feed channel of the bot wizy')
@commands.cooldown(1, 5)
async def toggle_rand_meme_quote_sender( ctx: commands.Context, state: int = None, interval_minutes: int = default_feed_channel_frequency_minutes ):
   """
   Toggles and controls the automatic meme and quote sending feature.
   
   This command allows authorized users to control the bot's automatic content
   sending feature. It can be used to enable/disable the feature and set the
   interval between sends.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       state (int, optional): The state to set (0 for off, 1 for on). Defaults to None.
       interval_minutes (int, optional): The interval between sends in minutes. 
           Defaults to default_feed_channel_frequency_minutes.
           
   Note:
       Only users with specific roles (ULT! SAQF, ULT! ADMIN, ULT! CODER, Spirits Overlord)
       or administrators can use this command.
   """
   global allowed_roles_togglerandom

   user_comanded_roles : list[discord.Role] = ctx.message.author.roles
   is_allowed = [role for role in user_comanded_roles if role.id in tuple(allowed_roles_togglerandom.values()) ]
   is_allowed = [True for role in user_comanded_roles if role.permissions.administrator == True] #if admin override any prev. is_allowed value with True
   
   if  is_allowed == None or  len(is_allowed) <= 0 :
      allowed_ids = list(allowed_roles_togglerandom.values())
      await ctx.message.delete(delay= 15.0) #delete user message it self ( then in .reply we delete bot msg also)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False) ,
                  delete_after= 15.0 ,
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ or ADMINS! are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
   else:
      await util.process_send_togglerandom_cmd(ctx= ctx, _state= state, _interval_minutes = interval_minutes)
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizyaimode", help= "choose between generative AI models used in wizy's chat channel: gpt / gemini / deep")
@commands.cooldown(1, 5)
@commands.check_any(commands.has_any_role(*list(allowed_roles_quotesz.values())), commands.has_permissions(administrator=True))
async def change_wizy_ai_type( ctx: commands.Context, ai_name:str = None ):
   """
   Changes the AI model used in the wizard's chat channel.
   
   This command allows authorized users to switch between different AI models
   (GPT, Gemini, or DeepSeek) used for the bot's responses in the chat channel.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       ai_name (str, optional): The name of the AI model to switch to.
           Must be one of: 'gpt', 'gemini', or 'deep'. Defaults to None.
           
   Note:
       Only users with specific roles or administrators can use this command.
       The command includes a cooldown of 5 seconds between uses.
   """
   await util.process_send_change_wizy_ai_cmd(ctx= ctx, _ai_name= None if ai_name is None else ai_name.strip().lower())


@change_wizy_ai_type.error
async def change_wizy_ai_type_error(ctx: commands.Context , error):
   print (f'\n\nTESTING#################E R R O R: {error}\n\n')
   if isinstance(error , commands.MissingAnyRole):
      allowed_ids = list(allowed_roles_change_ai.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ or ADMINS ! are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
   elif isinstance(error , commands.MissingPermissions):
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! __*only*__ ADMINS ! are allowed to use this command..."
                  )
   
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizymusicgenre", help= "choose between local available music genras: lofi / mmochill / mmoanime / orsmix")
@commands.cooldown(1, 5)
# @commands.check_any(commands.has_any_role(*list(allowed_roles_quotesz.values())), commands.has_permissions(administrator=True))
async def change_wizy_music_genre( ctx: commands.Context, genre_name:str = None ):
   """
   Changes the music genre for the bot's background music.
   
   This command allows users to switch between different music genres available
   in the bot's local collection. Available genres include lofi, mmochill,
   mmoanime, and orsmix.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       genre_name (str, optional): The name of the genre to switch to.
           Must be one of: 'lofi', 'mmochill', 'mmoanime', 'orsmix'.
           Defaults to None.
           
   Note:
       The command includes a cooldown of 5 seconds between uses.
   """
   await util.process_send_change_wizy_music_genre_cmd(ctx= ctx, _genre_name= None if genre_name is None else genre_name.strip().lower())


# @change_wizy_music_genre.error
# async def change_wizy_music_genre_error(ctx: commands.Context , error):
#    print (f'\n\nTESTING#################E R R O R: {error}\n\n')
#    if isinstance(error , commands.MissingAnyRole):
#       allowed_ids = list(allowed_roles_change_ai.values())
#       await ctx.reply(
#                   allowed_mentions=discord.AllowedMentions(roles=False),
#                   delete_after= 15.0,
#                   content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ or ADMINS ! are allowed to use this command..."
#                   ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
#    elif isinstance(error , commands.MissingPermissions):
#       await ctx.reply(
#                   allowed_mentions=discord.AllowedMentions(roles=False),
#                   delete_after= 15.0,
#                   content=f"Ops! __*only*__ ADMINS ! are allowed to use this command..."
#                   )
# ------------------------------------------------------------------------------------------------------------------------------------------#
custom_quote_threshhold = 200 #defaulted to 200 but you can change it via quotesz at runtime easily
max_quote_size = 5070
@bot.hybrid_command(name="quotesz" , help= 'modifies quote MAX number of Characters (default is 200)' )#defaulted to 200
@commands.cooldown(1, 5)
@commands.check_any(commands.has_any_role(*list(allowed_roles_quotesz.values())), commands.has_permissions(administrator=True))
async def change_quote_mx_sz( ctx: commands.Context, new_quote_sz: str):
   """
   Modifies the maximum number of characters allowed in quotes.
   
   This command allows authorized users to change the maximum length of quotes
   that can be generated by the bot. The default is 200 characters, and there
   is a hard limit of 5070 characters.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       new_quote_sz (str): The new maximum quote size to set.
           
   Note:
       Only users with specific roles or administrators can use this command.
       The command includes a cooldown of 5 seconds between uses.
       The maximum allowed size is 5070 characters.
   """
   global custom_quote_threshhold
   await util.process_send_quotesz_cmd(ctx= ctx, _quote_sz = new_quote_sz, _quote_threshhold= custom_quote_threshhold, _max_sz= max_quote_size)


@change_quote_mx_sz.error
async def change_quote_mx_sz_error(ctx: commands.Context , error):
   print (f'\n\nTESTING#################E R R O R: {error}')
   if isinstance(error , commands.MissingAnyRole):
      allowed_ids = list(allowed_roles_quotesz.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
   elif isinstance(error , commands.MissingPermissions):
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! __*only*__ ADMINS ! are allowed to use this command..."
                  )
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="ping", help= "roughly gets the time bot needed to respond in _ms_ ||__(needs testing)__||")
@commands.cooldown(1, 5)
async def ping(ctx: commands.Context):
   """
   Measures the bot's response time in milliseconds.
   
   This command calculates the time difference between when the user's message
   was sent and when the bot responds. The result is displayed in milliseconds.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       
   Note:
       The command includes a cooldown of 5 seconds between uses.
       The response message is automatically deleted after 15 seconds.
   """
   send_time    = ctx.message.created_at

   # next line is naieve datetime obj (all datime obj must be in same type naieve/aware  in order to do arithmatics on them)
   recieve_time = datetime.now()
   recieve_time = recieve_time.astimezone(pytz.utc) # converte aware time zone  to naieve time zone and set tz to utc

   msg_latency  = (abs(recieve_time - send_time)).total_seconds() * 1000 #mul by 1000 to get in ms #TODO : why  recieve time happends before create time !?
   tot_ping = round(msg_latency , 2)

   #NOTE:next line gets the  time needed to recieve user msg and send the respond (usually what users wnat to know)
   bot_reply_msg = await ctx.reply(delete_after= 15.0 , content= f"Pong! `{tot_ping}ms`" )
   await bot_reply_msg.add_reaction('\U0001F4F6') #📶 emoji unicide == '\U0001F4F6'
   await ctx.message.delete(delay= 15.0)
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wiz_ping", help= "gets time of bot heartbeat and discrod ack in _ms_ ||__(needs testing)__||." )
@commands.cooldown(1, 5)
async def wiz_ping(ctx: commands.Context):
   """
   Measures the bot's heartbeat latency with Discord servers.
   
   This command displays the bot's latency to Discord's servers in milliseconds.
   This is different from the regular ping command as it measures the WebSocket
   heartbeat latency rather than command response time.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       
   Note:
       The command includes a cooldown of 5 seconds between uses.
       The response message is automatically deleted after 15 seconds.
   """
   #NOTE : this gets bot latency between discord servers and the bot client
   bot_reply_msg = await ctx.reply(delete_after= 15.0 , content= f'Pong!  Bot Latency is `{round (bot.latency * 1000 , 2)}ms`')
   await bot_reply_msg.add_reaction('\U0001F4F6') #📶 emoji unicide == '\U0001F4F6'
   await ctx.message.delete(delay= 15.0)
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command( name="wizygpt", help="Wizard finds your answer between old scrolls from the depth of OpenAi GPT dungeons!") # command name is defaulted to method name 'gpt'
@commands.cooldown(1, 5)

async def gpt (ctx : commands.Context, * , full_prompt:str ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
   """
   Answers user queries using OpenAI GPT.
   
   This command fetches an answer from OpenAI GPT based on the user's prompt, unless the command is invoked in the wizard chat channel (to avoid duplicate answers).
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       full_prompt (str): The user's question or prompt for GPT.
   """
   #since I prefer no classic command 'prefix' ignore chat commands when inside wizy speical chat channel i.e.(avoid duplicated ans)
   if ctx.channel.id not in wizy_chat_channels :
       
      valid_reply : tuple(bool, discord.Message ) = await check_msg ( _message= ctx.message , chk_type= 2)

      if valid_reply[0] and valid_reply[1] is not  None :
         full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)

      #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
      try:
         user_msg = ctx.message

         ask_gpt_task = bot.loop.create_task(ask_gpt(full_prompt, user= ctx.author, is_wizy_ch= False ))

         if str(ctx.author.id) not in util.UserAiQuery.chats_ai_dict:
            send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
            await send_initMsg_task
            
         send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message, content= f"**Ah I see! Searching Ancient Scrolls for you on: ** \n \n `{full_prompt}` ..."))
         await send_initMsg_task

         task_response: tuple(str, str) = await ask_gpt_task
         embed = prepare_discord_embed(task_response, is_reply= valid_reply[0], is_gemini= False)

         send_func_return = bot.loop.create_task(user_msg.reply(embed=embed) if not ctx.interaction else ctx.reply(embed=embed))
         returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
      except:
         async with ctx.typing():
            ctx.message.delete(delay= 15)
            bot_reply_msg: discord.Message = await ctx.reply("**Ops! This feature is not working wizy very sorry!**", delete_after= 15)
@gpt.error
async def gpt(ctx: commands.Context , error):
   print (f'\n\nTESTING#################E R R O R: {error}')
   if isinstance(error , commands.HybridCommandError):
      allowed_ids = list(allowed_roles_quotesz.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! this is not avialble right now🧙‍♂️"
                  ) 
# #------------------------------------------------------------------------------------------------------------------------------------------#
#TODO: for commands & events using deepSeek AI: add attach files/images feature cuz deepseek supports it!
@bot.hybrid_command( name="wizydeep", aliases=["wizy", "wizardspirit"], help="Wizard finds your answer within the old scrolls from the depth of DeepSeek dungeons!") # command name is defaulted to method name 'gpt'
@commands.cooldown(1, 5)
async def deepSeek (ctx : commands.Context, * , full_prompt:str ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
   """
   Answers user queries using DeepSeek AI.
   
   This command fetches an answer from DeepSeek AI based on the user's prompt, unless the command is invoked in the wizard chat channel (to avoid duplicate answers).
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       full_prompt (str): The user's question or prompt for DeepSeek.
   """
   #since I prefer no classic command 'prefix' ignore chat commands when inside wizy speical chat channel i.e.(avoid duplicated ans)
   if ctx.channel.id not in wizy_chat_channels :
       
      valid_reply : tuple(bool, discord.Message ) = await check_msg ( _message= ctx.message , chk_type= 2)

      if valid_reply[0] and valid_reply[1] is not  None :
         full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)

      #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
      try:
         user_msg = ctx.message
         ask_deepSeek_task = bot.loop.create_task(ask_deepSeek(full_prompt, user= ctx.author, is_wizy_ch= False))
         ctx.interaction or await user_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
         
         if str(ctx.author.id) not in  util.UserAiQuery.chats_ai_dict:
            send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
            await send_initMsg_task
            
         send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message, content= f"**Ah I see! Searching Scrolls Labyrinth for  your scroll: ** \n \n `{full_prompt}` ...", delete_after= 15))
         await send_initMsg_task

         task_response: tuple(str, str) = await ask_deepSeek_task
         embed = prepare_discord_embed(task_response, is_reply= valid_reply[0], is_gemini= False)

         send_func_return = bot.loop.create_task(user_msg.reply(embed=embed) if not ctx.interaction else ctx.reply(embed=embed))
         returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
      except:
         async with ctx.typing():
            ctx.message.delete(delay= 15)
            bot_reply_msg: discord.Message = await ctx.reply("**Ops! This feature is not working wizy very sorry!**", delete_after= 15)
@deepSeek.error
async def deepSeek(ctx: commands.Context , error):
   print (f'\n\nTESTING#################E R R O R: {error}')
   if isinstance(error , commands.HybridCommandError):
      allowed_ids = list(allowed_roles_quotesz.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! this is not avialble right now🧙‍♂️"
                  ) 
# #------------------------------------------------------------------------------------------------------------------------------------------#
#NOTE: this left as non-hybrid command cuz if it's name (command name being a bot mention is good for classic commands only anyway)
#TODO: add attach files/images feature cuz deepseek supports it!
@bot.command(name=f"<@{wizard_bot_id}>", help= 'wizy answers you questions using DeepSeekp ... etc') # command name is defaulted to method name
@commands.cooldown(1, 5)
#(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
async def ChatDeepSeekfast (ctx: commands.Context, * ,full_prompt: str = "EMPTY PROMPT. CHECK REPLY: "  ):
   """
   Answers user queries using DeepSeek AI (classic command).
   
   This command fetches an answer from DeepSeek AI based on the user's prompt, unless the command is invoked in the wizard chat channel (to avoid duplicate answers). This is a classic command, not a hybrid one.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       full_prompt (str, optional): The user's question or prompt for DeepSeek. Defaults to a placeholder string.
   """
   #using GEMINI API
   #since I prefer no classic command 'prefix' ignore chat commands when inside wizy speical chat channel i.e.(avoid duplicated ans)
   if ctx.channel.id not in wizy_chat_channels :

      valid_reply : tuple(bool, discord.Message ) = await check_msg ( _message= ctx.message, chk_type= 2)

      if valid_reply[0] and valid_reply[1] is not  None :
         full_prompt = await get_new_reply_prompt(valid_reply[1], full_prompt)

      try:
         #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)

         user_msg = ctx.message
         ask_deepSeek_task = bot.loop.create_task(ask_deepSeek(full_prompt, user= ctx.author, is_wizy_ch= False ))
         ctx.interaction or await user_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'

         if str(ctx.author.id) not in  util.UserAiQuery.chats_ai_dict:
            send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message, content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
            await send_initMsg_task
         else:
            send_initMsg_task = bot.loop.create_task(ctx.send( reference= ctx.message, content= "**Searching Ancient Scrolls for you!...**", delete_after= 15 ))
            await send_initMsg_task
            
         task_response : tuple = await ask_deepSeek_task
         embed = prepare_discord_embed(task_response, is_reply= valid_reply[0], is_gemini= False)

         send_func_return = bot.loop.create_task(user_msg.reply(embed=embed))
         returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
      except:
         async with ctx.typing():
            ctx.message.delete(delay= 15)
            bot_reply_msg: discord.Message = await ctx.reply("**Ops! This feature is not working wizy very sorry!**", delete_after= 15)


      # img_embds = list()
      # if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
      # 	for img in task_response[2]:
      # 		img_embds.append(discord.Embed(type='image').set_image(img))

      # 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
      # 	await send_img_msg_task
#------------------------------------------------------------------------------------------------------------------------------------------#
# #NOTE: this left as non-hybrid command cuz if it's name (command name being a bot mention is good for classic commands only anyway)
# @bot.command(name=f"<@{wizard_bot_id}>", help= 'wizy answers you questions using GEMINI ... etc') # command name is defaulted to method name
# @commands.cooldown(1, 5)
# #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
# async def geminiAIfast (ctx: commands.Context, * ,full_prompt: str = "EMPTY PROMPT. CHECK REPLY: "  ):
# #using GEMINI API

#    valid_reply : tuple(bool, discord.Message ) = await check_msg ( _message= ctx.message, chk_type= 2)

#    if valid_reply[0] and valid_reply[1] is not  None :
#       full_prompt = await get_new_reply_prompt(valid_reply[1], full_prompt)

#    #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
#    send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
#    ask_gemini_task = bot.loop.create_task(ask_gemini(full_prompt, user_name= ctx.author.display_name ))
#    await send_initMsg_task
#    task_response : tuple = await ask_gemini_task
#    embed = prepare_discord_embed(task_response , is_reply= valid_reply[0])

#    send_func_return = bot.loop.create_task(ctx.reply(embed=embed))
#    returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
#    del embed
#    del valid_reply
#    del ctx

#    # img_embds = list()
#    # if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
#    # 	for img in task_response[2]:
#    # 		img_embds.append(discord.Embed(type='image').set_image(img))

#    # 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
#    # 	await send_img_msg_task
@ChatDeepSeekfast.error
async def ChatDeepSeekfast(ctx: commands.Context , error):
   print (f'\n\nTESTING#################E R R O R: {error}')
   if isinstance(error , commands.CommandError):
      allowed_ids = list(allowed_roles_quotesz.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! this is not avialble right now🧙‍♂️"
                  ) 
# #------------------------------------------------------------------------------------------------------------------------------------------#

@bot.hybrid_command(name="wizygemini", aliases=["gemini"], help= 'wizy answers your questions using GEMINI ... etc')
# command name is defaulted to method name 'geminiAI'
@commands.cooldown(1, 5)
#NOTE: (search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
async def geminiAI (ctx: commands.Context , * , full_prompt: str = "EMPTY PROMPT. CHECK REPLY: "):
   """
   Answers user queries using Gemini AI.
   
   This command fetches an answer from Gemini AI based on the user's prompt, unless the command is invoked in the wizard chat channel (to avoid duplicate answers).
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       full_prompt (str, optional): The user's question or prompt for Gemini. Defaults to a placeholder string.
   """
   #using GEMINI API
    #since I prefer no classic command 'prefix' ignore chat commands when inside wizy speical chat channel i.e.(avoid duplicated ans)
   if ctx.channel.id not in wizy_chat_channels :

      valid_reply : tuple[ bool , discord.Message ] = await check_msg ( _message= ctx.message , chk_type= 2) 

      if valid_reply[0] and valid_reply[1] is not  None :
         full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)
      #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
      try:
         ask_gemini_task = bot.loop.create_task(ask_gemini(full_prompt , user_name= ctx.author.display_name ))
         await send_initMsg_task
         task_response : tuple = await ask_gemini_task
         send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
         embed = prepare_discord_embed(task_response , is_reply= valid_reply[0], is_gemini= True)

         send_func_return = bot.loop.create_task(ctx.reply(embed=embed))
         returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
         del embed
         del valid_reply
      except:
         async with ctx.typing():
            ctx.message.delete(delay= 15)
            bot_reply_msg: discord.Message = await ctx.reply("**Ops! This feature is not working wizy very sorry!**", delete_after= 15)

   # img_embds = list()
   # if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
   # 	for img in task_response[2]:
   # 		img_embds.append(discord.Embed(type='image').set_image(img))

   # 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
   # 	await send_img_msg_task
@geminiAI.error
async def geminiAI(ctx: commands.Context , error):
   print (f'\n\nTESTING#################E R R O R: {error}')
   if isinstance(error , commands.HybridCommandError):
      allowed_ids = list(allowed_roles_quotesz.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! this is not avialble right now🧙‍♂️"
                  ) 
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizyleave", help= 'wizy leaves voice channel _if_ connected to one')
@commands.cooldown(1, 5)
async def leave_voice_wizard( ctx: commands.Context ):
   """
   Disconnects the bot from the current voice channel.
   
   This command makes the bot leave the voice channel it is currently connected to, if any.
   The command can be invoked via slash or classic command.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   if ctx.interaction: #if invoked using slash commmand
      bot_reply_msg = await ctx.reply(slash_cmd_ok_msg)
      await bot_reply_msg.delete(delay= 5)

   await ctx.message.delete(delay= 15.0)
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
   await ctx.guild.voice_client.disconnect()
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizyjoin", help= 'wizy joins voice channel you are in' )
@commands.cooldown(1, 5)
async def join_voice_wizard( ctx: commands.Context ):
   """
   Makes the bot join the voice channel the user is currently in.
   
   This command connects the bot to the same voice channel as the user, disconnecting from any other channel if necessary.
   If the user is not in a voice channel, an error message is sent.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   #TESTING
   print(f"######## 'wizyjoin' INVOKER VOICE STATE (TESTING): \n\n\n\n\n{ctx.author.voice}\n\n\n\n {True if ctx.author.voice else False }\n\n\n\n\n {ctx.guild.voice_client} ###########\n\n\n\n")
   #TESTING
   
   if ( ctx.author.voice ):
      if ctx.guild.voice_client is not None:
         await ctx.guild.voice_client.disconnect()

      target_voice_channel = ctx.message.author.voice.channel
      await  target_voice_channel.connect()

      if ctx.interaction: #if invoked using slash commmand
         bot_reply_msg = await ctx.reply(slash_cmd_ok_msg)
         await bot_reply_msg.delete(delay= 5)

      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'

   else :
      user = ctx.message.author.mention
      bot_reply_msg: discord.Message = await ctx.reply(
                  delete_after= 15.0,
                  content= f"Ops! {user}  you must be in a voice channel!"
                  )
      ctx.interaction or await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizyplay', help='To play audio')
@commands.cooldown(1, 5)
async def play(ctx: commands.Context, url: str= None):
   """
   Plays audio in the user's current voice channel.
   
   This command plays a YouTube audio stream or the bot's default tracks in the user's current voice channel.
   If the bot is already in another channel, it will not join unless moved.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       url (str, optional): The YouTube URL to play. If not provided, plays default tracks.
   """
   print(f"TESTING ######### \n\n\n {url} \n\n\n ###########")
   try :
      guild_obj = ctx.message.guild
      bot_vioce_client: discord.voice_client = guild_obj.voice_client
      
      
      #make bot (join + play) in one command! (IF he is already in a VC you must move him first!)
      if ( ctx.author.voice ):
         if bot_vioce_client is not None and (bot_vioce_client.channel != ctx.author.voice.channel):
            raise Exception("Bot is Being Used in another Voice Channel!")
         elif bot_vioce_client is None: #user is in a voice ch and bot is not in any voice channel
            await ctx.author.voice.channel.connect()
            bot_vioce_client: discord.voice_client = guild_obj.voice_client
         
         if url != None:
            async with ctx.typing():
               #NOTE: if stream arg causes error set to false (download file then play from local pc)
               song_obj , filename = await YTDLSource.from_url(url, loop=bot.loop, stream= True)

               if bot_vioce_client.is_playing():
                  bot_vioce_client.stop()

               bot_vioce_client.play(song_obj)

            bot_reply_msg: discord.Message = await ctx.reply(f'**Now playing:** {filename} **-** _islander_ {ctx.message.author.mention}')
            ctx.interaction or await bot_reply_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
            ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
            await ctx.message.delete(delay= 15.0)
         else: #play default chill tracks locally on your pc (infinity loop)
            async with ctx.typing():
               if bot_vioce_client.is_playing():
                  bot_vioce_client.stop()
               
               await util.play_chill_track(guild_obj)
               bot_reply_msg: discord.Message = await ctx.reply(f"**{ctx.message.author.mention} started Wizy's Default Wizy Tracks** enjoy! :blue_heart::notes:")
               ctx.interaction or await bot_reply_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
               ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
               await ctx.message.delete(delay= 15.0)
      else: 
         raise Exception("USER NOT IN VALID VOICE STATE (probably not inside a Voice Channel)!")
      

   except Exception as e:
      print(f"######### \n\n\n Exception Raised from 'wizyplay' cmd: {e} \n\n\n ###########")
      bot_reply_msg: discord.Message = await ctx.reply(f"Ops:kissing: !{e} __OR__ provided link is not a YouTube Music",
                                                       delete_after= 15
                                                      )
      ctx.interaction or await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizypause', help='This command pauses the audio')
@commands.cooldown(1, 5)
async def pause(ctx: commands.Context):
   """
   Pauses the currently playing audio.
   
   This command pauses the audio that the bot is currently playing in the voice channel.
   If nothing is playing, an error message is sent.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   voice_client = ctx.message.guild.voice_client
   if voice_client.is_playing():
      await await_me_maybe( voice_client.pause() )

      if ctx.interaction: #if invoked using slash commmand
               bot_reply_msg = await ctx.reply(slash_cmd_ok_msg)
               await bot_reply_msg.delete(delay= 5)

      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
      await ctx.message.delete(delay= 15.0)
   else:
      bot_reply_msg: discord.Message = await ctx.reply(content="The bot is not playing anything at the moment.", delete_after= 15)
      ctx.interaction or await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)

@bot.hybrid_command(name='wizyresume', help='Resumes the audio')
@commands.cooldown(1, 5)
async def resume(ctx: commands.Context):
    """
    Resumes paused audio playback.
    
    This command resumes the audio that was previously paused by the bot in the voice channel.
    If nothing is paused, an error message is sent.
    
    Args:
        ctx (commands.Context): The context of the command invocation.
    """
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await await_me_maybe(voice_client.resume())

        if ctx.interaction: #if invoked using slash commmand
            bot_reply_msg = await ctx.reply(slash_cmd_ok_msg)
            await bot_reply_msg.delete(delay= 5)

        ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
        await ctx.message.delete(delay= 15.0)
    else:
        bot_reply_msg: discord.Message = await ctx.reply(content="wizy wasn't pausing any track. maybe try  **wizyplay** command", delete_after= 15)
        ctx.interaction or await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
        ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
        await ctx.message.delete(delay= 15.0)
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizystop', help='Stops the audio')
@commands.cooldown(1, 5)
async def stop(ctx: commands.Context):
    """
    Stops the currently playing or paused audio.
    
    This command stops the audio that the bot is currently playing or has paused in the voice channel.
    If nothing is playing or paused, an error message is sent.
    
    Args:
        ctx (commands.Context): The context of the command invocation.
    """
    voice_client= ctx.message.guild.voice_client
    if voice_client.is_playing() or voice_client.is_paused():
        await await_me_maybe(voice_client.stop())

        if ctx.interaction: #if invoked using slash commmand
            bot_reply_msg = await ctx.reply(slash_cmd_ok_msg)
            await bot_reply_msg.delete(delay= 5)

        ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
        await ctx.message.delete(delay= 15.0)
    else:
        bot_reply_msg: discord.Message = await ctx.reply(content="The bot is not playing anything at the moment.", delete_after= 15)
        ctx.interaction or await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
        ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
        await ctx.message.delete(delay= 15.0)
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizyque', help='Shows the current queue or clears it **(TODO)**') #TODO
@commands.cooldown(1, 5)
async def queue(ctx: commands.Context, do_clear: str= None):
   """
   Shows or clears the current music queue.
   
   This command displays the current queue of tracks or clears it if the 'CLEAR' argument is provided.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
       do_clear (str, optional): If set to 'CLEAR', clears the queue.
   """
   if do_clear != None and do_clear.strip().capitalize() == 'CLEAR':
      util.tracks_queue.guilds_connected_queues[ctx.guild.id].clear()
      ctx.reply(content="Track Queue is Cleared!", delete_after= 15)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
      await ctx.message.delete(delay= 15.0)

# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizyadd', help='Appends track to end of tracks queue **(TODO)**') #TODO
@commands.cooldown(1, 5)
async def addTOqueue(ctx: commands.Context):
   """
   Appends a track to the end of the music queue. (TODO)
   
   This command is a placeholder for future implementation to add tracks to the queue.
   
   Args:
       ctx (commands.Context): The context of the command invocation.
   """
   pass  #TODO
# #------------------------------------------------------------------------------------------------------------------------------------------#


