"""
                          Coder : Omar
                          Version : v2.5B
                          version Date :  2 / 7 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Commands Code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from utils_bot import ask_bard , get_rand_greeting , prepare_discord_embed , check_msg , get_new_reply_prompt
from init_bot import *	
import keys
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.command (name="boringwizard" )
async def boring( ctx : commands.Context ):
   await ctx.send(embed= await pyrandmeme2(_title= "Some Wizardy Humor👻"))
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.command (name="wisewiz" )
async def wise( ctx : commands.Context ):
	#res : dict =  [{'author': 'J.R.R. Tolkien', 'book': 'The Fellowship of the Ring', 'quote': "I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve."}]
	res = None
	
	while res is None :
		random_word = RandomWords()
		category = random_word.get_random_word()
		res = quote(category , limit=1)
  
	quotes = " "
	for i in range(len(res)): # loop if there is multiple quotes e.g.(limit > 1)
		quotes : str = f"> {res[i]['quote']} `-GPTeous A. Wise Spirit;` '"
		
	await ctx.reply(content= quotes)
#------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command (name="ping" )
async def ping(ctx : commands.Context):
    await ctx.reply(content= f"Pong! Latency is {bot.latency}ms")
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
	
	# if len(task_response[2]) == 0 :
	# 	print("TESTING : EMPTY images")
    
	# for img in task_response[2] :
	# 	print (img) #TESTING

	# img_embds = list()
	# if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
	# 	for img in task_response[2]:
	# 		img_embds.append(discord.Embed(type='image').set_image(img)) 
   
	# 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
	# 	await send_img_msg_task
#------------------------------------------------------------------------------------------------------------------------------------------#
   
@bot.command(name="wizard" , aliases=["wizard ", "wiz" , "wizardspirit" , "bard"]) # command name is defaulted to method name 'bardAI'
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
	
	# if len(task_response[2]) == 0 :
	# 	print("TESTING : EMPTY images")
    
	# for img in task_response[2] :
	# 	print (img) #TESTING

	# img_embds = list()
	# if task_response[2] is not None and len(task_response[2]) != 0 and send_func_return.done():
	# 	for img in task_response[2]:
	# 		img_embds.append(discord.Embed(type='image').set_image(img)) 
   
	# 	send_img_msg_task = bot.loop.create_task(ctx.send(reference= returned_msg , embeds= img_embds) )#if error replace display_name with name
	# 	await send_img_msg_task
# #------------------------------------------------------------------------------------------------------------------------------------------#
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
         
         