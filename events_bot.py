"""
                          Coder : Omar
                          Version : v2.5B
                          version Date :  2 / 7 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Events code for Discord bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from init_bot import *
from utils_bot import ask_bard , check_msg
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
	global trigger_times
	if len(trigger_times) == 0 :
		now = datetime.now() 
		this_year = now.year
		this_month = now.month
		today = now.day
  
		for i in range(6):
			rnd_no = random.randint(0 , 23)
			if rnd_no < 10:
				rnd_no = "0" + str(rnd_no)
		
			wanted_time = datetime.strptime(f"{this_year}"+'-'+f"{this_month}"+'-'+ f"{today} " + f"{rnd_no}"+":00:00", "%Y-%m-%d %H:%M:%S")
			trigger_times.append(wanted_time)
	
		trigger_times.sort(reverse= True)
	
 
	wizard_ch_msg = message 
	
	for i in range (len(trigger_times)):
		if i > len(trigger_times) - 1 :
			break
  
		if datetime.now() > trigger_times[i] :
			trigger_times =trigger_times[0: i - 1 ]
   
			rnd_no = random.randint(1 , 4) #1:quote:wizard channel  2:quote:chat chill 3:meme:wizard Channel 
			if rnd_no <= 2 :
      
				#res : dict =  [{'author': 'J.R.R. Tolkien', 'book': 'The Fellowship of the Ring', 'quote': "I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve."}]
				res = None
				while res is None:
					random_word = RandomWords()
					category = random_word.get_random_word()
					res = quote(category , limit=1)
  
				quotes2 = " "
				for i in range(len(res)): # loop if there is multiple quotes e.g.(limit > 1)
					quotes2 : str = f"> {res[i]['quote']} `-GPTeous A. Wise Spirit;`"
				
				if rnd_no == 1 :# to wiz ch
					channel = bot.get_channel(wizard_channel_id)
					await channel.send(content= quotes2)
     
				else: #to chat&chill ch
					channel = bot.get_channel(chat_chill_ch_id)
					await channel.send(content= quotes2)

			else: #meme
				if rnd_no == 3 : #meme to wiz ch
					channel = bot.get_channel(wizard_channel_id)
					await channel.send(embed= await pyrandmeme())
				else : 
					channel = bot.get_channel(chat_chill_ch_id)
					await channel.send(embed= await pyrandmeme())
			break
 
	if await check_msg(wizard_ch_msg , targetChannelId= wizard_channel_id): 
    #NOTE : if want to disable talk to all bots in also check if author.bot != True
		# print (wizard_ch_msg.content)
		ask_bard_task =  bot.loop.create_task( ask_bard(user_query= wizard_ch_msg.content , user_name= wizard_ch_msg.author.display_name) ) #if error replace display_name with name
		task_response : tuple = await ask_bard_task
		bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** \n"
		links_msg_header = f"\n```ini\n [Sources & links]``` \n"
		full_response = bot_msg_header + task_response[0] 

		full_resp_len = len(full_response)
		if full_resp_len >= 2000 : #break bard response   to smaller messages to fit in discord msg
     
			bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** `[this msg will be fragmented: exceeds 2000chars]`\n"
			full_response = bot_msg_header + task_response[0] 
			full_resp_len = len(full_response) #re-calc
   
			needed_msgs = full_resp_len // 2000
			remain = full_resp_len % 2000
			if remain != 0 :
				needed_msgs += 1
    
			msg_frag : str
			end_flag = "\n```ini\n [END OF MSG]```"
			while needed_msgs != 0 :
				

				if needed_msgs == 1 and remain != 0 :
					if remain > len(end_flag) : #there is place to add in flag in same last msg frag
						msg_frag = full_response[ : ] + "\n```ini\n [END OF MSG]```"
						await message.reply(content= msg_frag  , mention_author= True)
						break
					else :#no place to add end flag send it seperatly in new discord msg
						msg_frag = full_response[ : ] 
						await message.reply(content= msg_frag  , mention_author= True)
						await message.reply(content= end_flag  , mention_author= True)
						break
						
					
				elif needed_msgs == 1 and remain == 0 : #send end flag in discord msg to indicate end of full bard response 
					msg_frag = full_response[ : ] 
					await message.reply(content= msg_frag  , mention_author= True)
					await message.reply(content= end_flag  , mention_author= True)
					break
  
				else :
					msg_frag = full_response[ : 1999]
     
				await message.reply(content= msg_frag  , mention_author= True)
				full_response = full_response[2000 : ]
					

				needed_msgs -= 1
				
			
		else: #all bard response can fit in one discord msg
			await message.reply(content= full_response  , mention_author= True)

		links_list = list( set(task_response[1])) #remove duplicate links
		links_list[0] = '\n * '+ links_list[0]
		final_links = links_msg_header  + '\n * '.join(links_list)
		await message.reply(content= final_links  , mention_author= True)
		#(DONE)TODO : ADD REPLY MESSAGES WITH LINKS IF THERE IS 
  		#TODO : reply with IMAGES IF THERE IS 
  
	await bot.process_commands(message) #add this to prevent on_message() from blocking bot.command
	del message
#------------------------------------------------------------------------------------------------------------------------------------------#

