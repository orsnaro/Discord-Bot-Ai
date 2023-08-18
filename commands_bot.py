"""
                          Coder : Omar
                          Version : v2.5.2B
                          version Date :  17 / 8 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Commands Code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from utils_bot import ask_bard , get_rand_greeting , prepare_discord_embed , prepare_quote
from utils_bot import check_msg , get_new_reply_prompt , meme_quote_sender_is_on_flag
from init_bot import *	
import keys
from typing import List
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.command (name="boringwizard" )
async def boring( ctx : commands.Context ):
   await ctx.send(embed= await pyrandmeme2(_title= "Some Wizardy Humor👻"))
#------------------------------------------------------------------------------------------------------------------------------------------#
allowed_roles_togglerandom = {"ULT! SAQF" : 889532272989053019 , "ULT! ADMIN" : 889931295365414993 , "ULT! CODER" : 1014300476814147656 , "Spirits Overlord" : 1118266805006389289} #check by id not the names cuz they're missing emojies
allowed_roles_quotesz = {"ULT! SAQF" : 889532272989053019 , "ULT! ADMIN" : 889931295365414993 , "ULT! CODER" : 1014300476814147656 , "Spirits Overlord" : 1118266805006389289} #check by id not the names cuz they're missing emojies
@bot.command (name="togglerandom")
async def toggle_rand_meme_quote_sender( ctx : commands.Context ):
	global allowed_roles_togglerandom
	global meme_quote_sender_is_on_flag 
 
	user_comanded_roles : list[discord.Role] = ctx.message.author.roles
	is_allowed = [role for role in user_comanded_roles if role.id in tuple(allowed_roles_togglerandom.values()) ]
	
	if  is_allowed == None or  len(is_allowed) <= 0 :
		allowed_ids = list(allowed_roles_togglerandom.values())
		await ctx.message.delete(delay= 15.0) #delete user message it self ( then in .reply we delete bot msg also)
		await ctx.reply(allowed_mentions=discord.AllowedMentions(roles=False) , delete_after= 15.0 , 
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command...") #used a join and map and lambda function just as fast fancy way to print all allowed roles
	else :
		meme_quote_sender_is_on_flag = not meme_quote_sender_is_on_flag
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(delete_after= 15.0 , 
                  content=f"random memes & quotes feature is {'`Enabled`' if meme_quote_sender_is_on_flag  else '`Disabled`' }")
   
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="wizyleave" )
async def leave_voice_wizard( ctx : commands.Context ):
	await ctx.guild.voice_client.disconnect()
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="wizyjoin" )
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
		await ctx.reply(delete_after= 15.0 , content= f"Ops! {user}  you must be in a voice channel!")
#------------------------------------------------------------------------------------------------------------------------------------------#
custom_quote_threshhold = 200 #defaulted to 200 but you can change it via quotesz at runtime easily
@bot.command (name="wisewiz" )
async def wise( ctx : commands.Context ):
	prepare_quote_task =  bot.loop.create_task(prepare_quote())
	quotes = await prepare_quote_task
	await ctx.reply(content= quotes)
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="quoteSz" )
@commands.has_any_role(*list(allowed_roles_quotesz.values()))
async def change_quote_mx_sz( ctx : commands.Context  ,  *args ):
	global custom_quote_threshhold
	if args is  None or len(args) <= 0 :
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(delete_after= 15.0 , content=f"please specify  `Quotes max size` current is `{custom_quote_threshhold}` ")
	else:  
		custom_quote_threshhold = args[0]
		await ctx.message.delete(delay= 15.0)
		await ctx.reply(delete_after= 15.0 , content=f"Quotes max size are now set to `{custom_quote_threshhold}`")
  
@change_quote_mx_sz.error #TODO : fix this working in preventing but doesnot send any message!
async def change_quote_mx_sz_error(error , ctx : commands.Context):
	if isinstance(error , commands.BotMissingAnyRole):	
		allowed_ids = list(allowed_roles_quotesz.values())
		await ctx.reply(allowed_mentions=discord.AllowedMentions(roles=False) , delete_after= 15.0 , 
                  content=f"Ops! __*only*__ _{' , '.join(map(lambda id : '<@&' + str(id) + '>' , allowed_ids))}_ are allowed to use this command...") #used a join and map and lambda function just as fast fancy way to print all allowed roles

#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="ping" )
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
@bot.command (name="wiz_ping" )
async def wiz_ping(ctx : commands.Context):
	await ctx.message.delete(delay= 15.0)
	await ctx.reply(delete_after= 15.0 , content= f'Pong!  Bot Latency is `{round (bot.latency * 1000 , 2)}ms`') #NOTE : this gets bot latency between discord servers and the bot client
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(name=f"<@{wizard_bot_id}>" ) # command name is defaulted to method name 
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
         
         