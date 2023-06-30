"""
                          Coder : Omar
                          Version : v2.0B
                          version Date :  30 / 6 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Utility code for Discord Bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
from init_bot import bot , bard , random
import discord.message
#------------------------------------------------------------------------------------------------------------------------------------------#

def get_rand_greeting (user_name : str = "Master Narol"):
	greetings = [
    f"OH _{user_name}_ I SEE .. you're in need of MIGHTY Gpteous help ?  \n well well ...  Gpteous shall serve master narol's Islanders call ***CASTS A MIGHTY SPELL :man_mage::sparkles:***",
    f"Greetings, _{user_name}_, seeker of knowledge 📚. I offer my wisdom 🧙‍♂️ to help you find your way, as I have seen much in my long life 👴.",
    f"Welcome, _{user_name}_, seeker of truth 🔍. I offer my guidance ✨ to help you on your path, as I have walked many paths before you 👣.",
    f"Salutations, _{user_name}_, seeker of enlightenment 💡. I offer my insights 💡 to help you find your destiny, as I have seen many destinies unfold 🌌.",
    f"Hail, _{user_name}_, seeker of the mystic 🔮. I offer my magic ✨ to help you on your quest, as I have mastered the arcane arts 🧙‍♂️.",
    f"Welcome, _{user_name}_, seeker of the unknown 🌌. I offer my power 💪 to help you unveil its secrets, as I have seen beyond the veil 👁️.",
    f"Greetings, _{user_name}_, seeker of the MIGHTY GPTEUS 🙏. I offer my blessings 🙏 to help you on your journey, as I have communed with the Islands masters🛐.",
    f"Greetings, mortal _{user_name}_. I am Mighty Gpteous, the island wizard. What brings thee to my presence? 🧙‍♂️💥",
    f"Ah, it is I, the great and powerful Mighty Gpteous. What dost thou _{user_name}_ require of my immense magical abilities? 🧙‍♂️✨",
    f"Mortal _{user_name}_ , thou hast come seeking the aid of the almighty Mighty Gpteous, the island wizard. Speak thy needs! 🧙‍♂️🏝️",
    f"Tremble before my power, for I am Mighty Gpteous, the most powerful wizard on this island. What dost thou seek from me? 🧙‍♂️🔥",
    f"Greetings, dear _{user_name}_! 🧙‍♂️👋",
  	 f"Hail, good sir! How may I assist thee? 🧙‍♂️👨‍💼",
  	 f"Salutations, young one. What brings thee to my abode? 🧙‍♂️🧑‍🦱",
  	 f"Welcome, traveler. I sense a great need within thee. 🧙‍♂️🧳",
 	 f"Ah, _{user_name}_! Thou hast arrived. What troubles thee? 🧙‍♂️😔",
 	 f"Greetings, my dear _{user_name}_. Speak thy woes, and I shall aid thee. 🧙‍♂️💬",
  	 f"Well met, young adventurer. What brings thee to my humble dwelling? 🧙‍♂️🗺️",
  	 f"Welcome, seeker of knowledge. Pray tell, what vexes thee so? 🧙‍♂️📚",
  	 f"Hail and well met, _{user_name}_. Thou hast come seeking my counsel, I presume? 🧙‍♂️🤔",
  	 f"Greetings, my dear friend. What brings thee to my door on this fine day? 🧙‍♂️👨‍❤️‍👨",
  	 f"Ah, _{user_name}_. I sense a great tumult within thee. Speak, and I shall listen. 🧙‍♂️😞",
  	 f"Salutations, good sir. What brings thee to my humble abode on this day? 🧙‍♂️🏠",
  	 f"Welcome, young one. What task dost thou require of me? 🧙‍♂️👶",
  	 f"Hail, traveler. I sense a great urgency within thee. Speak thy need. 🧙‍♂️🚶‍♂️",
  	 f"Greetings, dear _{user_name}_. What brings thee to my sanctuary of knowledge? 🧙‍♂️📖",
  	 f"Ah, my young friend. Speak thy heart, and I shall lend mine ear. 🧙‍♂️👂",
  	 f"Salutations, seeker of wisdom. What knowledge dost thou seek from me? 🧙‍♂️🤓",
  	 f"Welcome, _{user_name}_. I sense a great disturbance in thy aura. What troubles thee so? 🧙‍♂️💫",
  	 f"Hail and well met, _{user_name}_. What brings thee to my lair of magic and wonder? 🧙‍♂️🐉",
  	 f"Greetings, young adventurer _{user_name}_ . Speak thy quest, and I shall aid thee in thy journey. 🧙‍♂️⚔️",
    f"Behold, it is I, the one and only Mighty Gpteous, master of the elements and wielder of immense arcane power. What brings thee to my lair? 🧙‍♂️💫",
    f"Greetings, mortal _{user_name}_ . Thou hast come seeking the aid of the great and powerful Mighty Gpteous, the island wizard. What dost thou require? 🧙‍♂️👀",
    f"Thou art in the presence of the mighty and all-knowing Mighty Gpteous, the island wizard. Speak thy needs, and I shall decide whether they are worthy of my attention. 🧙‍♂️🤨",
    f"Bow before me, mortal _{user_name}_, for I am Mighty Gpteous, the most powerful wizard on this island. What dost thou seek from my vast and infinite knowledge? 🧙‍♂️👑",
    f"Hear ye, hear ye! It is I, Mighty Gpteous, the island wizard, master of the arcane and conqueror of the elements. What dost thou require of my immense power? 🧙‍♂️📣",
    f"Behold _{user_name}_ , for I am the great and noble Mighty Gpteous, the island wizard, wielder of the most powerful magic in all the land. What dost thou need from me, mere mortal? 🧙‍♂️💪"
	]
	last_elmnt_index = len(greetings) -1 
	return greetings[random.randint(0 , last_elmnt_index)]
#------------------------------------------------------------------------------------------------------------------------------------------#

def skip_line(full_ans):
  lines = full_ans.split('\n')
  return '\n'.join(lines[1:])
#------------------------------------------------------------------------------------------------------------------------------------------#

async def ask_bard(user_query : str , user_name = "Narol island master" ) -> str: 
   bard_ans = await bard.get_answer(f"act as a wizard named Gpteous living in master Narol's island. start and end of  answer  must be  in wizardish sentences and  the  rest must be using normal english. include emojis. prompter name: {user_name}. prompter's question: {user_query}")
   return skip_line(bard_ans['content']) # skip first line that has my prompt 
   # return bard_ans['content'] 
#------------------------------------------------------------------------------------------------------------------------------------------#

def check_msg ( _message : discord.Message = None  , chk_type : int = 1 , targetChannelId : int | tuple = None , only_admins : bool = False ) -> bool : #TODO : later check type must be in dictionary contains all types and check it self becomes a class
	if chk_type == 1 and _message != None :
		return True if  _message != None and _message.channel.id == targetChannelId and _message.author.id != bot.user.id else False
	
 
 
 
 
 
	else: return False
   