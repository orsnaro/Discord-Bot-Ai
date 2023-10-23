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
@commands.cooldown(1, 5)
@bot.command (name="help")
async def help( ctx : commands.Context ):
	await ctx.send(content= override_help_msgP1)
	await ctx.send(content= override_help_msgP2)
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="boringwizard" )
@commands.cooldown(1, 5)
async def boring( ctx : commands.Context ):
   await ctx.send(embed= await pyrandmeme2(_title= "Some Wizardy Humor👻"))
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
@bot.command (name="togglerandom")
@commands.cooldown(1, 5)
async def toggle_rand_meme_quote_sender( ctx : commands.Context ):

	global allowed_roles_togglerandom

	user_comanded_roles : list[discord.Role] = ctx.message.author.roles
	is_allowed = [role for role in user_comanded_roles if role.id in tuple(allowed_roles_togglerandom.values()) ]

	if  is_allowed == None or  len(is_allowed) <= 0 :
		allowed_ids = list(allowed_roles_togglerandom.values())
		await ctx.message.delete(delay= 15.0) #delete user message it self ( then in .reply we delete bot msg also)
		await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False) ,
                  delete_after= 15.0 ,
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
	else :
		await bot.stop_auto_memequote_sender() if bot.is_auto_memequote_on else await bot.start_auto_memequote_sender()
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(
                  delete_after= 15.0,
                  content=f"random memes & quotes feature is {'`Enabled`' if bot.is_auto_memequote_on  else '`Disabled`' }"
                  )

#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="wizyleave")
@commands.cooldown(1, 5)
async def leave_voice_wizard( ctx : commands.Context ):
	await ctx.guild.voice_client.disconnect()
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="wizyjoin" )
@commands.cooldown(1, 5)
async def join_voice_wizard( ctx : commands.Context ):

	if ( ctx.author.voice ):
		if ctx.guild.voice_client is not None:
			await ctx.guild.voice_client.disconnect()

		target_voice_channel = ctx.message.author.voice.channel
		await ctx.message.delete(delay= 15.0)
		await  target_voice_channel.connect()
	else :
		user = ctx.message.author.mention
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(
                  delete_after= 15.0,
                  content= f"Ops! {user}  you must be in a voice channel!"
                  )
#------------------------------------------------------------------------------------------------------------------------------------------#
custom_quote_threshhold = 200 #defaulted to 200 but you can change it via quotesz at runtime easily
max_quote_size = 5070
@bot.hybrid_command (name="wisewiz")
async def wise( ctx : commands.Context ):
	prepare_quote_task =  bot.loop.create_task(prepare_quote(invoker= 0)) # invoker == 0 means command wisewiz invoked
	quotes = await prepare_quote_task
	await ctx.reply(content= quotes)
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="quotesz" )#defaulted to 200
@commands.cooldown(1, 5)
@commands.has_any_role(*list(allowed_roles_quotesz.values()))
async def change_quote_mx_sz( ctx : commands.Context , *args ):
	global custom_quote_threshhold
	if args is  None or len(args) <= 0 :
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(delete_after= 15.0 , content=f"Ops! please specify  `Quotes max size` current is `{custom_quote_threshhold}` ")
	elif not args[0].isnumeric() :
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(delete_after= 15.0 , content=f"Ops! Quote size must be a numeric value! current is `{custom_quote_threshhold}` ")
	elif int(args[0]) > max_quote_size :
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(
                  delete_after= 15.0,
                  content=f"Ops! max Quote size is {max_quote_size}! current size is `{custom_quote_threshhold}` "
                  )
	else:
		custom_quote_threshhold = int(args[0])
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(delete_after= 15.0,
                     content=f"Quotes max size are now set to `{custom_quote_threshhold}`"
                     )

@change_quote_mx_sz.error
async def change_quote_mx_sz_error(error , ctx : commands.Context):
	print (f'\n\n#################{error}')
	if isinstance(error , commands.MissingAnyRole):
		allowed_ids = list(allowed_roles_quotesz.values())
		await ctx.reply(
                  allowed_mentions=discord.AllowedMentions(roles=False),
                  delete_after= 15.0,
						content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command..."
                  ) #used a join and map and lambda function just as fast fancy way to print all allowed roles
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="ping" )
@commands.cooldown(1, 5)
async def ping(ctx : commands.Context):
	bot_latency  = bot.latency
	send_time    = ctx.message.created_at
	recieve_time = datetime.now() # this is naieve datetime obj (all datime obj must be in same type naieve/aware  in order to do arithmatics on them)
	recieve_time = recieve_time.astimezone(pytz.utc) # converte aware time zone  to naieve time zone and set tz to utc

	msg_latency  = (abs(recieve_time - send_time)).total_seconds() * 1000 #mul by 1000 to get in ms #TODO : why  recieve time happends before create time !?
	tot_ping = round(msg_latency , 2)

	await ctx.message.delete(delay= 15.0)
	await ctx.reply(delete_after= 15.0 , content= f"Pong! `{tot_ping}ms`" ) #NOTE this gets the  time needed to recieve user msg and send the respond (usually what users wnat to know)
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="wiz_ping")
@commands.cooldown(1, 5)
async def wiz_ping(ctx : commands.Context):
	await ctx.message.delete(delay= 15.0)
	await ctx.reply(delete_after= 15.0 , content= f'Pong!  Bot Latency is `{round (bot.latency * 1000 , 2)}ms`') #NOTE : this gets bot latency between discord servers and the bot client
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name=f"<@{wizard_bot_id}>") # command name is defaulted to method name
@commands.cooldown(1, 5)
async def bardAIfast (ctx : commands.Context , * ,full_prompt : str = "EMPTY PROMPT. CHECK REPLY :"  ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
#using BARD API

	valid_reply : tuple(bool , discord.Message ) = await check_msg ( _message= ctx.message , chk_type= 2)

	if valid_reply[0] and valid_reply[1] is not  None :
		full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)

	send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))#if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
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

@bot.command(name="wizard" , aliases=["wizard ", "wizy" , "wizardspirit" , "bard"]) # command name is defaulted to method name 'bardAI'
@commands.cooldown(1, 5)
async def bardAI (ctx : commands.Context , * , full_prompt : str = "EMPTY PROMPT. CHECK REPLY :" ,  ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
#using BARD API
	valid_reply : tuple(bool , discord.Message ) = await check_msg ( _message= ctx.message , chk_type= 2)

	if valid_reply[0] and valid_reply[1] is not  None :
		full_prompt = await get_new_reply_prompt(valid_reply[1] , full_prompt)

	send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))#if you put ctx.message.reference  instead of ctx.message in reference arg this will reply to very first message you replied to (if you have)
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
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name='wizyplay', help='To play song')
@commands.cooldown(1, 5)
async def play(ctx: commands.Context , url: str= None):
   print(f"TESTING ######### \n\n\n {url} \n\n\n ###########")
   try :
      guild_obj = ctx.message.guild
      voice_channel = guild_obj.voice_client

      if url != None:
         async with ctx.typing():
            song_obj , filename = await YTDLSource.from_url(url, loop=bot.loop, stream= True) #NOTE: if stream arg causes error set to false (download file then play from local pc)

            if voice_channel.is_playing():
               voice_channel.stop()

            voice_channel.play(song_obj)

         await ctx.send(f'**Now playing:** {filename}')
      else: #play default chill tracks locally on your pc (infinity loop)
         async with ctx.typing():
            if voice_channel.is_playing():
               voice_channel.stop()
               
            await util.play_chill_track(guild_obj)
            await ctx.send("**Now playing Wizy's Default MMO Chill Tracks** enjoy! :blue_heart::notes:")

   except Exception as e:
      print(f"######### \n\n\n Exception Raised from 'wizyplay' cmd: {e} \n\n\n ###########")
      await ctx.send("Ops:kissing: ! either The bot is not connected to a voice channel __OR__ provided link is not a YouTube Music", delete_after= 15)
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name='wizypause', help='This command pauses the song')
@commands.cooldown(1, 5)
async def pause(ctx: commands.Context):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
       await await_me_maybe( voice_client.pause() )
    else:
        await ctx.send(content="The bot is not playing anything at the moment.", delete_after= 15)

# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name='wizyresume', help='Resumes the song')
@commands.cooldown(1, 5)
async def resume(ctx:  commands.Context):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await await_me_maybe(voice_client.resume())
    else:
        await ctx.send(content="The bot was not playing anything before this. Use wizyplay command", delete_after= 15)

# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name='wizystop', help='Stops the song')
@commands.cooldown(1, 5)
async def stop(ctx: commands.Context):
    voice_client= ctx.message.guild.voice_client
    if voice_client.is_playing():
       await await_me_maybe(voice_client.stop())
    else:
        await ctx.send(content="The bot is not playing anything at the moment.", delete_after= 15)
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name='wizyque', help='show the current track queue or clears it')
@commands.cooldown(1, 5)
async def queue(ctx: commands.Context, do_clear: str= None):
   if do_clear != None and do_clear.strip().capitalize() == 'CLEAR':
      util.tracks_queue.guilds_connected_queues[ctx.guild.id].clear()
      ctx.reply(content="Track Queue is Cleared!", delete_after= 15)
      
# #------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name='wizyadd', help='Stops the song')
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


