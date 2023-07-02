"""
                          Coder : Omar
                          Version : v2.5B
                          version Date :  2 / 7 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Utility code for Discord Bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from init_bot import bot , bard , random , wizard_bot_id , datetime 
from init_bot import wizard_channel_id , chat_chill_ch_id , pyrandmeme ,RandomWords , quote
import discord.message
#------------------------------------------------------------------------------------------------------------------------------------------#

def get_rand_greeting (user_name : str = "Master Narol"):
	greetings = [
    f"OH  _{user_name}_  I SEE .. you're in need of MIGHTY Gpteous help ?  \n well well ...  Gpteous shall serve master narol's Islanders call ***CASTS A MIGHTY SPELL :man_mage::sparkles:***",
    f"Greetings,  _{user_name}_, seeker of knowledge 📚. I offer my wisdom 🧙‍♂️ to help you find your way, as I have seen much in my long life 👴.",
    f"Welcome,   _{user_name}_, seeker of truth 🔍. I offer my guidance ✨ to help you on your path, as I have walked many paths before you 👣.",
    f"Salutations,  _{user_name}_, seeker of enlightenment 💡. I offer my insights 💡 to help you find your destiny, as I have seen many destinies unfold 🌌.",
    f"Hail,  _{user_name}_, seeker of the mystic 🔮. I offer my magic ✨ to help you on your quest, as I have mastered the arcane arts 🧙‍♂️.",
    f"Welcome,  _{user_name}_, seeker of the unknown 🌌. I offer my power 💪 to help you unveil its secrets, as I have seen beyond the veil 👁️.",
    f"Greetings,  _{user_name}_, seeker of the MIGHTY GPTEUS 🙏. I offer my blessings 🙏 to help you on your journey.",
    f"Greetings, mortal  _{user_name}_. I am Mighty Gpteous, the island wizard. What brings thee to my presence? 🧙‍♂️💥",
    f"Ah, it is I, the great and powerful Mighty Gpteous. What dost thou 	_{user_name}_	 require of my immense magical abilities? 🧙‍♂️✨",
    f"Mortal 	 _{user_name}_ , thou hast come seeking the aid of the  Mighty GPTeous, the island wizard. Speak thy needs! 🧙‍♂️🏝️",
    f"Tremble before my power, for I am Mighty Gpteous, the most powerful wizard on this island. What dost thou seek from me? 🧙‍♂️🔥",
    f"Greetings, dear  _{user_name}_! 🧙‍♂️👋",
  	 f"Hail, good sir! How may I assist thee? 🧙‍♂️👨‍💼",
  	 f"Salutations, young one. What brings thee to my abode? 🧙‍♂️🧑‍🦱",
  	 f"Welcome, traveler. I sense a great need within thee. 🧙‍♂️🧳",
 	 f"Ah,  _{user_name}_! Thou hast arrived. What troubles thee? 🧙‍♂️😔",
 	 f"Greetings, my dear  _{user_name}_. Speak thy woes, and I shall aid thee. 🧙‍♂️💬",
  	 f"Well met, young adventurer. What brings thee to my humble dwelling? 🧙‍♂️🗺️",
  	 f"Welcome, seeker of knowledge. Pray tell, what vexes thee so? 🧙‍♂️📚",
  	 f"Hail and well met, _{user_name}_. Thou hast come seeking my counsel, I presume? 🧙‍♂️🤔",
  	 f"Greetings, my dear friend. What brings thee to my door on this fine day? 🧙‍♂️👨‍❤️",
  	 f"Ah, _{user_name}_	. I sense a great tumult within thee. Speak, and I shall listen. 🧙‍♂️😞",
  	 f"Salutations, good sir. What brings thee to my humble abode on this day? 🧙‍♂️🏠",
  	 f"Welcome, young one. What task dost thou require of me? 🧙‍♂️",
  	 f"Hail, traveler. I sense a great urgency within thee. Speak thy need. 🧙‍♂️🚶‍♂️",
  	 f"Greetings, dear _{user_name}_. What brings thee to my sanctuary of knowledge? 🧙‍♂️📖",
  	 f"Ah, my young friend. Speak thy heart, and I shall lend mine ear. 🧙‍♂️👂",
  	 f"Salutations, seeker of wisdom. What knowledge dost thou seek from me? 🧙‍♂️🤓",
  	 f"Welcome,	 _{user_name}_. I sense a great disturbance in thy aura. What troubles thee so? 🧙‍♂️💫",
  	 f"Hail and well met,	 _{user_name}_. What brings thee to my lair of magic and wonder? 🧙‍♂️🐉",
  	 f"Greetings, young adventurer	 _{user_name}_ . Speak thy quest, and I shall aid thee in thy journey. 🧙‍♂️⚔️",
    f"Behold, it is I, the one and only Mighty Gpteous, master of the elements and wielder of immense arcane power. What brings thee to my lair? 🧙‍♂️💫",
    f"Greetings, mortal	 _{user_name}_ . Thou hast come seeking the aid of the great and powerful Mighty Gpteous, the island wizard. What dost thou require? 🧙‍♂️👀",
    f"Thou art in the presence of the mighty and  Mighty Gpteous, the island wizard. Speak thy needs, and I shall decide whether they are worthy of my attention. 🧙‍♂️🤨",
    f"Bow before me, mortal 	_{user_name}_, for I am Mighty Gpteous, the most powerful wizard on this island. What dost thou seek from my vast and infinite knowledge? 🧙‍♂️👑",
    f"Hear ye, hear ye! It is I, Mighty Gpteous, the island wizard, master of the arcane and conqueror of the elements. What dost thou require of my immense power? 🧙‍♂️📣",
    f"Behold 	_{user_name}_ , for I am the great and noble Mighty Gpteous, the island wizard, wielder of the most powerful magic in all the land. What dost thou need from me, mere mortal? 🧙‍♂️💪"
	]
	last_elmnt_index = len(greetings) -1 
	return greetings[random.randint(0 , last_elmnt_index)]
#------------------------------------------------------------------------------------------------------------------------------------------#

def skip_line(full_ans):
  lines = full_ans.split('\n')
  return '\n'.join(lines[1:])
#------------------------------------------------------------------------------------------------------------------------------------------#

async def ask_bard(user_query : str , user_name = "Narol island master" ) -> tuple: 
   bard_ans = await bard.get_answer(f"act as a wizard named Gpteous living in master Narol's island. start and end of  answer  must be  in wizardish sentences and  the  rest must be using normal english. include emojis. prompter name: {user_name}. prompter's question: {user_query}")
   # return skip_line(bard_ans['content']) , bard_ans['links'] , bard_ans['images'] , bard_ans['response_id'] , bard_ans['conversation_id'] # skip first line that has my prompt 
   return bard_ans['content'] , bard_ans['links'] , bard_ans['images'] , bard_ans['response_id'] , bard_ans['conversation_id']
#------------------------------------------------------------------------------------------------------------------------------------------#
async def check_msg ( _message : discord.Message = None  , chk_type : int = 1 , targetChannelId : int | tuple = None , only_admins : bool = False , **extraArgs ) -> bool : #TODO : later check type must be in dictionary contains all types and check it self becomes a class
	if chk_type == 1 and _message != None : #NOTE : checks for on_message() in wizard channel 
		return True if  _message != None and _message.channel.id == targetChannelId and _message.author.id != bot.user.id else False 

	elif chk_type == 2 and _message != None:#NOTE : checks for  messages of type: reply
		msg_channel = _message.channel
		

		if _message.reference is None or _message.reference.message_id is None :
				return False , None
		else:
			first_msg_id = _message.reference.message_id
			first_msg_cntnt_task = bot.loop.create_task(msg_channel.fetch_message(first_msg_id))
			first_msg_cntnt = await first_msg_cntnt_task
			first_msg_cntnt = first_msg_cntnt.content
			first_msg_cntnt_filtered = first_msg_cntnt.replace(f"<@{wizard_bot_id}" , '').strip().replace(" ", '') 
   
			if len(first_msg_cntnt_filtered) == 0 :
				return False , -1
 
			else:
				print ("TESTING : ID of ref msg:" , _message.reference.message_id ) #TESTING
				return True , _message
 
 
 
 
 
	else: return False
#------------------------------------------------------------------------------------------------------------------------------------------#
bard_conversation_ids_buffer = set()
def save_last_conv_id() : ...  #TODO
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_discord_embed( bard_ans_data : tuple  , is_reply : bool = False) -> discord.Embed :
   #TODO : handle if embed exceeds max size of max size of fields ( bot will continue work anyway but tell user that OF happend of paganating)
	'''
EMBED TOTAL MAX SIZE is 6000 chars ( # NOTE : use reactions and pagination if exceeded )
class EmbedLimits(object):
    Total = 6000
    Title = 256
    Description = 2048
    Fields = 25
    class Field(object):
        Name = 256
        Value = 1024
    class Footer(object):
        Text = 2048
    class Author(object):
        Name = 256
	'''
 
 #TESTING BLOCK
	print ("\n\n\n TESTING : EMBED conetns lengths :")
	print ("ans text" , bard_ans_data[0] )
	print ("#######ans text len" , len(bard_ans_data[0]) )
 
	print ("links" , bard_ans_data[1] )
	print ("images" , bard_ans_data[2] )
	imgs_sz =0
	for img in bard_ans_data[2]:
		imgs_sz += len(img)
	print ("#######imgs len" , imgs_sz) 
	print ("############# len images" , imgs_sz) 
	tot_len = len(bard_ans_data[0]) + len(bard_ans_data[1]) + len(bard_ans_data[2]) + 200
 #TESTING BLOCK

	ansText = bard_ans_data[0]
	footerIcon="https://em-content.zobj.net/thumbs/120/whatsapp/352/scroll_1f4dc.png"
	wizardChannelLink ="https://discord.com/channels/797143628215877672/1118953370510696498"
	note_compined_msg = "_This is combined response i.e.(more than one message) and still not perfectly formatted_"
	embedTitle = "MIGHTY GPTEOUS Ancient Scroll :scroll: Found! \n"
	timeNow = datetime.now()
	author = "Bard AI"
	bardIcon = "https://i.imgur.com/u0J6wRz.png"
	redTint = 10038562
	darkGreen = discord.Colour.dark_green()
   
	embed = discord.Embed(type='rich' , timestamp= timeNow , color= darkGreen , title= embedTitle ,url= wizardChannelLink , description= ansText + " \n `*END OF ANSWER*` ") #url will be  hyperlink in title
	embed.set_author(name= author, url="https://bard.google.com" , icon_url= bardIcon )
 
	if bard_ans_data[1] is not None and len(bard_ans_data[1]) != 0 :
		
		bard_ans_links = list(set(bard_ans_data[1])) #NOTE = FOR SOME reason there is many redundancy in links so i removed duplicates
  
  #TESTING BLOCk
		link_sz =0
		for i in range(len(bard_ans_data[1])):
			link_sz += len(bard_ans_data[1][i])
		print ("#######links len" , link_sz) 
  #TESTING BLOCk
	
  
		tot_len_of_links_sections = 0
		for i in range(len(bard_ans_links)):
			tot_len_of_links_sections += len(bard_ans_links[i])

		if tot_len_of_links_sections >= 1022:
    
			one_field_mx = 1022 #less than discord_limit  (for safety)
			super_list = [] #each element is an list of links / content that is tot char counts is <= 1023
			super_list.append([])
			links_list = bard_ans_links
			max_i =  len(bard_ans_links)
			char_cnt , field_indx , i  = 0 , 0 , 0 # vars controlling while loop
			bullet_point_format_len = 6
			while i < max_i:
				char_cnt += len(links_list[i]) + bullet_point_format_len #
    
				if char_cnt >= one_field_mx :
					super_list[field_indx][0] = '\n * ' + super_list[field_indx][0] #fix join dont format 1st element
					embed.add_field(name= f"_ __sources p({field_indx + 1})__  _"  , inline= False , value= '\n * '.join(super_list[field_indx]) )
					char_cnt = 0
					field_indx += 1
					super_list.append([])
					super_list[field_indx].append(links_list[i])
				else :
					super_list[field_indx].append(links_list[i])
    
				i += 1 #TODO : solve loss of some links
    
			del super_list 
			del links_list


		else:
			bard_ans_links[0] = '\n * ' + bard_ans_links[0] #fix join dont format 1st element
			tmp = '\n * '.join(bard_ans_links) #TESTING
			print ("TESTING final sources format " , tmp)
			embed.add_field(name= f"_ __sources & links__  _"  , inline= False , value= '\n * '.join(bard_ans_links))
	
	if is_reply :
		embed.add_field(name= "_ __note__ _ " , inline= False , value= note_compined_msg)
 
	embed.set_footer(text= f"Scroll ID({bard_ans_data[3]})" , icon_url= footerIcon )
 
 #TESTING BLOCK
	field_sz =0
	for i in range(len(embed.fields)):
		field_sz += len((embed.fields)[i])
  
	print ("\n\n###### embed field sz" ,field_sz)
	print ("###### embed author sz "  ,len(embed.author))
	print ("###### embed desc sz "  ,len(embed.description))
	print ("###### embed foot sz " ,len(embed.footer))
	print ("###### embed title " ,len(embed.title))
	print ("###### embed tot " ,len(embed))
 #TESTING BLOCK
 
	return embed
#------------------------------------------------------------------------------------------------------------------------------------------#



async def get_new_reply_prompt(_message : discord.Message, old_prompt : str ) -> str :
   first_msg_id = _message.reference.message_id
   
   
   msg_fetch_task = bot.loop.create_task(_message.channel.fetch_message(first_msg_id))
   first_msg_content = await msg_fetch_task
   first_msg_content : discord.Message.content = first_msg_content.content
   
   first_msg_content : str =  first_msg_content.replace(f"<@{wizard_bot_id}" , ' ')#if other commands like 'bard' or 'wizard' its mostly ok # NOTE : (still testing)
   new_prompt : str = old_prompt + ' ' + f"\"{first_msg_content}\""
   
   
   return new_prompt
#------------------------------------------------------------------------------------------------------------------------------------------#
trigger_times = []
#------------------------------------------------------------------------------------------------------------------------------------------#
def set_trigger_times() -> list :
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
		print ("TEST:choosen rand times", trigger_times) #TESTING
   
#------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------#
async def send_rand_quote_meme( message : discord.Message ) :

	global trigger_times
	set_trigger_times()
 
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
 
   
#------------------------------------------------------------------------------------------------------------------------------------------#
 
	