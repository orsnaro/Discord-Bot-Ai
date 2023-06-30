"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Commands Code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from utils_bot import ask_bard , get_rand_greeting
from init_bot import *	
import keys
#------------------------------------------------------------------------------------------------------------------------------------------#

@bot.command(name=f"<@{wizard_bot_id}>" , aliases= [" " , "\t"]) # command name is defaulted to method name 
async def bardAIfast (ctx : commands.Context , * , full_prompt:str ,  ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
#using BARD API
	print("entered comand name empty string or space")#testing
	send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message.reference ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**" ))#if error replace display_name with name
	ask_bard_task = bot.loop.create_task(ask_bard(full_prompt , user_name= ctx.author.display_name ))
	await send_initMsg_task 
	task_response = await ask_bard_task
	# task_response = ask_bard(full_prompt , user_name= ctx.author.display_name )
	embed = discord.Embed(type='rich' , color= 1 , title="MIGHTY GPTEOUS Wizard Spell Results  has come!! \n" , description=task_response)        
	await ctx.reply(embed=embed)# short cut for ctx.send()   
#------------------------------------------------------------------------------------------------------------------------------------------#
   
@bot.command(name="wizard" , aliases=["wizard ", "wiz" , "wizardspirit" , "bard"]) # command name is defaulted to method name 'bardAI'
async def bardAI (ctx : commands.Context , * , full_prompt:str ,  ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
#using BARD API
   send_initMsg_task = bot.loop.create_task(ctx.send(reference= ctx.message.reference ,  content= "**"+get_rand_greeting(ctx.author.display_name)+"**")) #if error replace display_name with name
   ask_bard_task = bot.loop.create_task(ask_bard(full_prompt , user_name= ctx.author.display_name ))
   await send_initMsg_task 
   task_response = await ask_bard_task
   # task_response = ask_bard(full_prompt , user_name= ctx.author.display_name )
   embed = discord.Embed(type='rich' , color= 1 , title="MIGHTY GPTEOUS Wizard Spell Results  has come!! \n" , description=task_response)        
   await ctx.reply(embed=embed)# short cut for ctx.send()   
#------------------------------------------------------------------------------------------------------------------------------------------#
   
@bot.command(name="wizardgpt" , aliases =["wizardgpt " , "gpt"]) # command name is defaulted to method name 'gpt'
async def gpt (ctx : commands.Context , * , full_prompt:str ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
   async with aiohttp.ClientSession() as session: #with just is for handling errors and session ending
      payload = {
         "model": "text-davinci-003", # this is a GPT text model meaning you cant have series of prompts => only one question one answer at a time . later I may try chat/image.. models with discord
         "prompt": full_prompt,
         "temperature": 0.5, #max = 1 very creative ,min = 0 restrict deterministic, each ans to same question varry if high creativity
         "max_tokens" : 40, #GPT answer max length (let us start with short length not to increase response time and exhoust token balance)
         "presence_penalty": 0, #higher will discourge gpt to repeat tokens in generated text
         "frequency_penalty": 0, #lower value incourage gpt to use the more frequent tokens in training data DB more in generated text
         "best_of": 1,#remove if cause an error (no much docs for it but seems to take only first ans among list of answers)
      }
      headers = {"Authorization": f"Bearer {keys.openaiAPI_KEY}"}
      async with session.post("https://api.openai.com/v1/chat/completions" , json=payload , headers=headers) as respond: #if sucess returns awaitable coroutine value = ClientResponse obj
         response = await respond.json()
         embed = discord.Embed(type='rich' , title="MIGHTY GPTEOUS Wizard!! info-gathering Spell casted! \n" , description=response['choice'][0]['text'])        
         await ctx.reply(embed=embed)       # short cut for ctx.send()   
#------------------------------------------------------------------------------------------------------------------------------------------#
         
         