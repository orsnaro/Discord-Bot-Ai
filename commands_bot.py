"""
                          Coder : Omar
                          Version : v2.5.3B
                          version Date :  23 / 10 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Commands Code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from init_bot import *
from utils_bot import ask_bard , get_rand_greeting , prepare_discord_embed , prepare_quote
from utils_bot import check_msg , get_new_reply_prompt, YTDLSource , await_me_maybe
import keys
from typing import List
#------------------------------------------------------------------------------------------------------------------------------------------#
#disabled default global help message  from bot constructor then override default by this command
slash_cmd_ok_msg = "OK ✅"
@bot.hybrid_command(name="help")
@commands.cooldown(1, 5)
async def help( ctx: commands.Context ):
   bot_help_msg_p1: discord.Message = await ctx.reply(content= override_help_msgP1)
   await ctx.send(content= override_help_msgP2)
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="boringwizard", help= "wizy sends a random meme from Reddit")
@commands.cooldown(1, 5)
async def boring( ctx: commands.Context ):
   await ctx.send(embed= await pyrandmeme2(_title= "Some Wizardy Humor👻"))

   #if used via slash command will not add reaction cuz it raises discord error msg not found
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizyawakened", help= "wizy wakes you up to the truth")
@commands.cooldown(1, 5)
async def boring( ctx: commands.Context ):
   ps_post_get_task = await bot.loop.create_task(palestina_free(_title= ":flag_ps: *r/Palestine* :flag_ps:"))
   ps_post_embed_is_video, ps_post_data, ps_post_url = await await_me_maybe(ps_post_get_task)
      
   if ps_post_embed_is_video == False:
      await ctx.send(embed= ps_post_data)
   else:
      await ctx.send(content= ps_post_data + '\n' + ps_post_url)
      
   #if used via slash command will not add reaction cuz it raises discord error msg not found
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
custom_quote_threshhold = 200 #defaulted to 200 but you can change it via quotesz at runtime easily
max_quote_size = 5070
@bot.hybrid_command(name="wisewiz", help= 'wizy sends a random Quote (quote of type 1 for now glitches slash cmd)')
async def wise( ctx: commands.Context):
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
@bot.hybrid_command(name="togglerandom", help= 'toggles the auto meme-quote sender feature of the bot wizy')
@commands.cooldown(1, 5)
async def toggle_rand_meme_quote_sender( ctx: commands.Context, state: int = 1 ):

   global allowed_roles_togglerandom

   user_comanded_roles : list[discord.Role] = ctx.message.author.roles
   is_allowed = [role for role in user_comanded_roles if role.id in tuple(allowed_roles_togglerandom.values()) ]

   if  is_allowed == None or  len(is_allowed) <= 0 :
      allowed_ids = list(allowed_roles_togglerandom.values())
      await ctx.message.delete(delay= 15.0) #delete user message it self ( then in .reply we delete bot msg also)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False) ,
                  delete_after= 15.0 ,
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
   else :
      special_event = state #specially made to switch memes and quotes to post on palestine only (and for any special events later on)
      if state is None  or not state >= 2:
         await bot.toggle_auto_memequote_sender_state(state = 1) if bot.is_auto_memequote_state == 0 else await bot.toggle_auto_memequote_sender_state(state= 0)
         await ctx.reply(
                     delete_after= 15.0,
                     content=f"random memes & quotes feature is {'`Enabled`' if bot.is_auto_memequote_state  else '`Disabled`' }"
                     )
      elif state == special_event:
         await bot.toggle_auto_memequote_sender_state(state = special_event) 
         await ctx.reply(
                     delete_after= 15.0,
                     content=f"random memes & quotes feature is on **special event mode**:  `special event id: {'Free Palestine!' if special_event == 2 else special_event}`"
                     )
         
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'

#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="quotesz" , help= 'modifies quote MAX number of Characters (default is 200)' )#defaulted to 200
@commands.cooldown(1, 5)
@commands.has_any_role(*list(allowed_roles_quotesz.values()))
async def change_quote_mx_sz( ctx: commands.Context, new_quote_sz: str):
   global custom_quote_threshhold
   if new_quote_sz is None or len(new_quote_sz) <= 0 :
      bot_reply_msg: discord.Message = await ctx.reply(delete_after= 15.0,
                                                       content=f"Ops! please specify  `Quotes max size` current is `{custom_quote_threshhold}` "
                                                       )
      await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   elif not new_quote_sz.isnumeric() :
      bot_reply_msg: discord.Message = await ctx.reply(delete_after= 15.0,
                                                       content=f"Ops! Quote size must be a numeric value! current is `{custom_quote_threshhold}` "
                                                       )
      await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   elif int(new_quote_sz) > max_quote_size :
      bot_reply_msg: discord.Message = await ctx.reply(
                  delete_after= 15.0,
                  content=f"Ops! max Quote size is {max_quote_size}! current size is `{custom_quote_threshhold}` "
                  )
      await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   else:
      custom_quote_threshhold = int(new_quote_sz)
      bot_reply_msg: discord.Message = await ctx.reply(delete_after= 15.0,
                     content=f"Quotes max size is now set to `{custom_quote_threshhold}`"
                     )
      await bot_reply_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'

@change_quote_mx_sz.error
async def change_quote_mx_sz_error(error , ctx: commands.Context):
   print (f'\n\n#################{error}')
   if isinstance(error , commands.MissingAnyRole):
      allowed_ids = list(allowed_roles_quotesz.values())
      await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="ping", help= "roughly gets the time bot needed to respond in _ms_ ||__(needs testing)__||")
@commands.cooldown(1, 5)
async def ping(ctx: commands.Context):
   bot_latency  = bot.latency
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
@bot.hybrid_command(name="wiz_ping", help= "gets time of bot heartbeat and discrod ack in _ms_ ||__(needs testing)__||" )
@commands.cooldown(1, 5)
async def wiz_ping(ctx: commands.Context):
   #NOTE : this gets bot latency between discord servers and the bot client
   bot_reply_msg = await ctx.reply(delete_after= 15.0 , content= f'Pong!  Bot Latency is `{round (bot.latency * 1000 , 2)}ms`')
   await bot_reply_msg.add_reaction('\U0001F4F6') #📶 emoji unicide == '\U0001F4F6'
   await ctx.message.delete(delay= 15.0)
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
#NOTE: this left as non-hybrid command cuz if it's name (command name being a bot mention is good for classic commands only anyway)
@bot.command(name=f"<@{wizard_bot_id}>", help= 'wizy answers you questions using GPT/BARD ... etc') # command name is defaulted to method name
@commands.cooldown(1, 5)
#(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
async def bardAIfast (ctx: commands.Context , * ,full_prompt: str = "EMPTY PROMPT. CHECK REPLY: "  ):
#using BARD API

   valid_reply : tuple(bool , discord.Message ) = await check_msg ( _message= ctx.message , chk_type= 2)

   if valid_reply[0] and valid_reply[1] is not  None :
      full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)

   #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
   send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
   ask_bard_task = bot.loop.create_task(ask_bard(full_prompt , user_name= ctx.author.display_name ))
   await send_initMsg_task
   task_response : tuple = await ask_bard_task
   embed = prepare_discord_embed(task_response , is_reply= valid_reply[0])

   send_func_return = bot.loop.create_task(ctx.reply(embed=embed))
   returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
   del embed
   del valid_reply
   del ctx

   # img_embds = list()
   # if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
   # 	for img in task_response[2]:
   # 		img_embds.append(discord.Embed(type='image').set_image(img))

   # 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
   # 	await send_img_msg_task
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.hybrid_command(name="wizard", aliases=["wizy", "wizardspirit", "bard"], help= 'wizy answers you questions using GPT/BARD ... etc')
# command name is defaulted to method name 'bardAI'
@commands.cooldown(1, 5)
#NOTE: (search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
async def bardAI (ctx: commands.Context , * , full_prompt: str = "EMPTY PROMPT. CHECK REPLY: "):
#using BARD API
   valid_reply : tuple(bool , discord.Message ) = await check_msg ( _message= ctx.message , chk_type= 2)

   if valid_reply[0] and valid_reply[1] is not  None :
      full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)
   #NOTE: (next line) if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
   send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))
   try:
      ask_bard_task = bot.loop.create_task(ask_bard(full_prompt , user_name= ctx.author.display_name ))
      await send_initMsg_task
      task_response : tuple = await ask_bard_task
      embed = prepare_discord_embed(task_response , is_reply= valid_reply[0])

      send_func_return = bot.loop.create_task(ctx.reply(embed=embed))
      returned_msg : discord.Message = await send_func_return  # short cut for ctx.send()
      del embed
      del valid_reply
   except: 
      async with ctx.typing():
         bot_reply_msg: discord.Message = await ctx.reply("**Ops! This feature is not working wizy very sorry!**", delete_after= 15)

   # img_embds = list()
   # if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
   # 	for img in task_response[2]:
   # 		img_embds.append(discord.Embed(type='image').set_image(img))

   # 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
   # 	await send_img_msg_task
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name="wizyleave", help= 'wizy leaves voice channel _if_ connected to one')
@commands.cooldown(1, 5)
async def leave_voice_wizard( ctx: commands.Context ):
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

   if ( ctx.author.voice ):
      if ctx.guild.voice_client is not None:
         await ctx.guild.voice_client.disconnect()

      target_voice_channel = ctx.message.author.voice.channel

      if ctx.interaction: #if invoked using slash commmand
         bot_reply_msg = await ctx.reply(slash_cmd_ok_msg)
         await bot_reply_msg.delete(delay= 5)

      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'

      await  target_voice_channel.connect()
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
@bot.hybrid_command(name='wizyplay', help='To play song')
@commands.cooldown(1, 5)
async def play(ctx: commands.Context, url: str= None):
   print(f"TESTING ######### \n\n\n {url} \n\n\n ###########")
   try :
      guild_obj = ctx.message.guild
      voice_channel = guild_obj.voice_client

      if url != None:
         async with ctx.typing():
            #NOTE: if stream arg causes error set to false (download file then play from local pc)
            song_obj , filename = await YTDLSource.from_url(url, loop=bot.loop, stream= True)

            if voice_channel.is_playing():
               voice_channel.stop()

            voice_channel.play(song_obj)

         bot_reply_msg: discord.Message = await ctx.reply(f'**Now playing:** {filename} **-** _islander_ {ctx.message.author.mention}')
         ctx.interaction or await bot_reply_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
         ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
         await ctx.message.delete(delay= 15.0)
      else: #play default chill tracks locally on your pc (infinity loop)
         async with ctx.typing():
            if voice_channel.is_playing():
               voice_channel.stop()

            await util.play_chill_track(guild_obj)
            bot_reply_msg: discord.Message = await ctx.reply(f"**{ctx.message.author.mention} started Wizy's Default MMO Chill Tracks** enjoy! :blue_heart::notes:")
            ctx.interaction or await bot_reply_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
            ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
            await ctx.message.delete(delay= 15.0)

   except Exception as e:
      print(f"######### \n\n\n Exception Raised from 'wizyplay' cmd: {e} \n\n\n ###########")
      bot_reply_msg: discord.Message =await ctx.reply("Ops:kissing: ! either The bot is not connected to a voice channel __OR__ provided link is not a YouTube Music",
                                                      delete_after= 15
                                                      )
      ctx.interaction or await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizypause', help='This command pauses the song')
@commands.cooldown(1, 5)
async def pause(ctx: commands.Context):
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

# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizyresume', help='Resumes the song')
@commands.cooldown(1, 5)
async def resume(ctx: commands.Context):
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
@bot.hybrid_command(name='wizystop', help='Stops the song')
@commands.cooldown(1, 5)
async def stop(ctx: commands.Context):
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
   if do_clear != None and do_clear.strip().capitalize() == 'CLEAR':
      util.tracks_queue.guilds_connected_queues[ctx.guild.id].clear()
      ctx.reply(content="Track Queue is Cleared!", delete_after= 15)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
      await ctx.message.delete(delay= 15.0)

# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.hybrid_command(name='wizyadd', help='Appends track to end of tracks queue **(TODO)**') #TODO
@commands.cooldown(1, 5)
async def addTOqueue(ctx: commands.Context):
   pass  #TODO
# #------------------------------------------------------------------------------------------------------------------------------------------#
#TODO
# @bot.command(name="wizardgpt" , aliases =["wizardgpt " , "gpt"]) # command name is defaulted to method name 'gpt'
# async def gpt (ctx : commands.Context , * , full_prompt:str ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
#    async with aiohttp.ClientSession() as session: #with just is for handling errors and session ending
#       payload = {
#          "model": "text-davinci-003", # this is a GPT text model meaning you cant have series of prompts => only one question one answer at a time . later I may try chat/image.. models with discord
#          "prompt": full_prompt,
#          "temperature": 0.5, #max = 1 very creative ,min = 0 restrict deterministic, each ans to same question varry if high creativity
#          "max_tokens" : 40, #GPT answer max length (let us start with short length not to increase response time and exhoust token balance)
#          "presence_penalty": 0, #higher will discourge gpt to repeat tokens in generated text
#          "frequency_penalty": 0, #lower value incourage gpt to use the more frequent tokens in training data DB more in generated text
#          "best_of": 1,#remove if cause an error (no much docs for it but seems to take only first ans among list of answers)
#       }
#       headers = {"Authorization": f"Bearer {keys.openaiAPI_KEY}"}
#       async with session.post("https://api.openai.com/v1/chat/completions" , json=payload , headers=headers) as respond: #if sucess returns awaitable coroutine value = ClientResponse obj
#          response = await respond.json()
#          embed = discord.Embed(type='rich' , title="MIGHTY GPTEOUS Wizard!! info-gathering Spell casted! \n" , description=response['choice'][0]['text'])
#          await ctx.reply(embed=embed)       # short cut for ctx.send()
# #------------------------------------------------------------------------------------------------------------------------------------------#


