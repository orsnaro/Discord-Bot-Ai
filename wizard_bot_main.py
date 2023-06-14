   
import asyncio as aio
from bardapi import BardAsync
import discord
from discord.ext import commands
from inspect import getmembers , isfunction
import aiohttp

#TODO : make bot see prev messages 
#TODO : talk to bot by mention him or reply to his message (take the content of replayed message and respond accordingly to it + new message)
#TODO : rest of tasks is on mods channel (todo) in my narol's server 

#Heartbeating handled automatically (modify from gateway class) 
#NOTE : BARD API is the one used now due to connection and belling issue beteen GPT API and my country (egypt)

with open(r"../openai_apiKey.txt" , 'r') as openaifile :
   openaiAPI_KEY = openaifile.read().strip()
   
with open(r"../discordBotToken_Gpteous.txt" , 'r') as discordfile :
   Token_gpteousBot = discordfile.read().strip()
   
#from cockie name : "__Secure-1PSID"
with open(r"../bard_apiKey.txt" , 'r') as bardfile :
   bardAPI_KEY = bardfile.read().strip() 

def skip_line(full_ans):
  lines = full_ans.split('\n')
  return '\n'.join(lines[1:])

bard = BardAsync(token=bardAPI_KEY)
async def ask_bard(user_query : str , user_name = "Narol him self" ):
   bard_ans = await bard.get_answer(f"act as a wizard named Gpteous living in master Narol's island. start and end of  answer  must be  in wizardish sentences  that also  has emojies like :fog: etc.. . the  rest must be using normal english. {user_name} question: {user_query}")
   return skip_line(bard_ans['content']) # skip first line that has my prompt 



 


bot = commands.Bot(command_prefix="~" , intents=discord.Intents.all() ,description= """
                   GPTEOUS HELP MESSAGE```
                   :fleur_de_lis: MIGHTY GPTEOUS! Am the first GPT-Spirit in Narol's island volcan gurdian , Island Master right hand  and the begining of Island's new ERA  , etc... I mean you get it am very special here  :man_mage:
                   
                   
                   :fleur_de_lis: Ask me and  I shall INDEED answer you 
                   
                   :fleur_de_lis: The question must start with '~WizardSpirit ' 
                   
                   :fleur_de_lis: Aditional Functionalities and SPELLS coming soon...
                   
                   ```fix
                   *note : Due to connectivity + billing issues between my country 'Egypt' and GPT API We temporarily moved to using bard via a coockie key
                   ```
                   """)


@bot.event
async def on_ready():
   print(f"Bot '{bot.user}' Sucessfully connected to Discord!\n\n")
   print(f"Bot info: \n (magic and dunder attrs. excluded) ")
   for attr in dir(bot.user):
      if  not (attr.startswith('__') or  attr.startswith('_')) :
         value = getattr(bot.user, attr)
         print(f'    {attr}: {value}')
   
@bot.command(name="WizardSpirit") # command name is defaulted to method name 'gpt'
async def gpt (ctx : commands.Context , * , full_prompt:str ): #(search keyword-only arguments) astrisk in alone arg is to force the later argument to be  passed by name e.g.( prompt="string1" )
   # async with aiohttp.ClientSession() as session: #with just is for handling errors and session ending
   #    payload = {
   #       "model": "text-davinci-003", # this is a GPT text model meaning you cant have series of prompts => only one question one answer at a time . later I may try chat/image.. models with discord
   #       "prompt": full_prompt,
   #       "temperature": 0.5, #max = 1 very creative ,min = 0 restrict deterministic, each ans to same question varry if high creativity
   #       "max_tokens" : 40, #GPT answer max length (let us start with short length not to increase response time and exhoust token balance)
   #       "presence_penalty": 0, #higher will discourge gpt to repeat tokens in generated text
   #       "frequency_penalty": 0, #lower value incourage gpt to use the more frequent tokens in training data DB more in generated text
   #       "best_of": 1,#remove if cause an error (no much docs for it but seems to take only first ans among list of answers)
   #    }
   #    headers = {"Authorization": f"Bearer {openaiAPI_KEY}"}
   #    async with session.post("https://api.openai.com/v1/chat/completions" , json=payload , headers=headers) as respond: #if sucess returns awaitable coroutine value = ClientResponse obj
   #       response = await respond.json()
   #       embed = discord.Embed(type='rich' , title="MIGHTY GPTEOUS Wizard!! info-gathering Spell casted! \n" , description=response['choice'][0]['text'])        
   #       await ctx.reply(embed=embed)       # short cut for ctx.send()   
#BARD API usage
   send_initMsg_task = bot.loop.create_task(ctx.send(content= f"OH _**{ctx.author.name}**_ I SEE .. you're in need of MIGHTY Gpteous help ?  \n well well ...  Gpteous shall serve master narol's Islanders call ***CASTS A MIGHTY SPELL :man_mage::sparkles:***"))
   ask_bard_task = bot.loop.create_task(ask_bard(full_prompt , user_name= ctx.author.name ))
   await send_initMsg_task 
   task_response = await ask_bard_task
   embed = discord.Embed(type='rich' , color= 1 , title="MIGHTY GPTEOUS Wizard!! Spell casted! \n" , description=task_response)        
   await ctx.reply(embed=embed)# short cut for ctx.send()   
bot.run(Token_gpteousBot)