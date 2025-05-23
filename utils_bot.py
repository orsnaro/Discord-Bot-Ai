"""
                          Coder : Omar
                          Version : v2.5.6B
                          version Date :  26 / 04 / 2025
                          Code Type : python | Discrod | GEMINI | HTTP | ASYNC
                          Title : Utility code for Discord Bot
                          Interpreter : cPython  v3.11.8 [Compiler : MSC v.1937 64 bit (AMD64)]
"""
import init_bot as ini
import discord.message
import youtube_dl
import asyncio as aio
import aiohttp

#------------------------------------------------------------------------------------------------------------------------------------------#
def get_last_conv_id()  : ...  #TODO
#------------------------------------------------------------------------------------------------------------------------------------------#
def cd_to_main_dir(main_file: str):
   abspath = ini.os.path.abspath(main_file)
   dname = ini.os.path.dirname(abspath)
   ini.os.chdir(dname)
#------------------------------------------------------------------------------------------------------------------------------------------#
async def await_me_maybe(value):
    if callable(value):
        value = value()
    if aio.iscoroutine(value):
        value = await value
    return value
#------------------------------------------------------------------------------------------------------------------------------------------#
def get_all_files(dir: str) -> list[str]:
   """_summary_
      get all tracks for local 

   Args:
       dir (str): the root path of all local tracks

   Returns:
       list[str]: all paths for local tracks
       
   """
   all_paths = []
   for root, dirs, files in ini.os.walk(dir):
      for file in files:
         rel_path = ini.os.path.join(root, file)
         all_paths += [rel_path]
   return all_paths
#------------------------------------------------------------------------------------------------------------------------------------------#
def find_VC_matching_guild(invoker: discord.Member, bot: ini.commands.Bot) -> discord.VoiceClient:
   """_summary_
      get bots voice client in same server as the invoker
   Args:
       invoker (discord.Member)
       bot (ini.commands.Bot)
   Returns:
       discord.VoiceClient: bots voice client that in same guild as the bot command invoker
   """
   for VC in bot.voice_clients :
      if VC.guild == invoker.guild : 
         return VC
   
#------------------------------------------------------------------------------------------------------------------------------------------#
async def play_chill_track(server: discord.Guild):
   tracks_dir: str = "./tracks"
   local_tracks: list[str] = get_all_files(dir= tracks_dir)
   print("\n\n\n####TESTING\n\n\n ",local_tracks)#TESTING
   track_path = ini.random.choice(local_tracks)
   await await_me_maybe(server.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=track_path)))
#------------------------------------------------------------------------------------------------------------------------------------------#
async def sub_sections_msg_sending_ctrl (message : discord.Message , final_links_msg : str , lnk1_len : int , final_imgs_msg : str , lnks_flag = False , imgs_flag = True) :
   if  lnks_flag and imgs_flag : # meaning I will supress first link also cuz there is imgs already
      #SUPRESS FIRST LINK  (first parse the message)
      fst_char_1st_link = 33 #29 chars for header [0~28] then 3 chars  bullet point [29~31]
      seg_before_1st_link = final_links_msg[0 : fst_char_1st_link] #end is excluded
      lnk1 = final_links_msg[fst_char_1st_link : fst_char_1st_link + lnk1_len] #end is excluded
      lnk1 = '<' + lnk1 + '>'
      seg_aft_1st_link = final_links_msg[fst_char_1st_link + lnk1_len : ]
      final_links_msg = seg_before_1st_link + lnk1 + seg_aft_1st_link #now 1st link and all links are supressed !
      await message.reply(content= final_links_msg , mention_author= False)
      await message.reply(content= final_imgs_msg  , mention_author= False)

   elif lnks_flag and not imgs_flag : # means I will not supress first link embed (prepare funcs done this already)
      await message.reply(content= final_links_msg , mention_author= False)
   elif imgs_flag and not lnks_flag : #send only imgs
      await message.reply(content= final_imgs_msg  , mention_author= False)
   else: #no imgs or links sections is present
      pass
      
#------------------------------------------------------------------------------------------------------------------------------------------#
def supress_msg_body_url_embeds ( text : str ) -> str :
  url_regex = r"(https?://\S+)(\s|\n|$)"
  matches = ini.re.finditer(url_regex, text)
  for match in matches:
    text = text.replace(match.group(0), f"<{match.group(0).strip()}> \n")
  return text
#------------------------------------------------------------------------------------------------------------------------------------------#
# TODO : join all prepare funcs in one class or control function
async def prepare_send_wizard_channel_ans_msg( _response : tuple  , message : discord.Message , discord_msg_limit = 2000, is_gemini:bool = True) :

   #Supress i.e.(no embed) any URL inside the msg body and not in links msg section
   if is_gemini :
      _gemini_response = _response
      bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** \n"
      full_response = bot_msg_header + _gemini_response[0]

      print ("TESTING: " , full_response) #TESTING

   #MSG FRAGMENTER SECTION ( TODO : make message fragmenter function for both msg and links msg in utils_bot.py )
      full_resp_len = len(full_response)
      if full_resp_len >= discord_msg_limit : #break gemini response   to smaller messages to fit in discord msg

         bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** `[this msg will be fragmented: exceeds 2000chars]`\n"
         full_response = bot_msg_header + _gemini_response[0]
         full_response = supress_msg_body_url_embeds(full_response)

         full_resp_len = len(full_response) #re-calc

         needed_msgs = full_resp_len // discord_msg_limit
         remain = full_resp_len % discord_msg_limit
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


            elif needed_msgs == 1 and remain == 0 : #send end flag in discord msg to indicate end of full gemini response
               msg_frag = full_response[ : ]
               await message.reply(content= msg_frag  , mention_author= True)
               await message.reply(content= end_flag  , mention_author= True)
               break

            else :
               msg_frag = full_response[ : discord_msg_limit] # from 0 to limit i.e.( 0 -> 1998 = 2000char)  end is not taken ( exclusisve )
               await message.reply(content= msg_frag  , mention_author= True)

            full_response = full_response[discord_msg_limit : ] # skip the sent fragment of message start after it for rest fragments
            needed_msgs -= 1


      else: #all gemini response can fit in one discord msg
         full_response = supress_msg_body_url_embeds(full_response)
         await message.reply(content= full_response  , mention_author= True)
         
         
   elif not is_gemini: #GPT
      _gpt_response = _response
      bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** \n"
      full_response = bot_msg_header + _gpt_response[0]

      print ("TESTING: " , full_response) #TESTING

   #MSG FRAGMENTER SECTION ( TODO : make message fragmenter function for both msg and links msg in utils_bot.py )
      full_resp_len = len(full_response)
      if full_resp_len >= discord_msg_limit : #break gemini response   to smaller messages to fit in discord msg

         bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** `[this msg will be fragmented: exceeds 2000chars]`\n"
         full_response = bot_msg_header + _gpt_response[0]
         full_response = supress_msg_body_url_embeds(full_response)

         full_resp_len = len(full_response) #re-calc

         needed_msgs = full_resp_len // discord_msg_limit
         remain = full_resp_len % discord_msg_limit
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


            elif needed_msgs == 1 and remain == 0 : #send end flag in discord msg to indicate end of full gemini response
               msg_frag = full_response[ : ]
               await message.reply(content= msg_frag  , mention_author= True)
               await message.reply(content= end_flag  , mention_author= True)
               break

            else :
               msg_frag = full_response[ : discord_msg_limit] # from 0 to limit i.e.( 0 -> 1998 = 2000char)  end is not taken ( exclusisve )
               await message.reply(content= msg_frag  , mention_author= True)

            full_response = full_response[discord_msg_limit : ] # skip the sent fragment of message start after it for rest fragments
            needed_msgs -= 1


      else: #all gemini response can fit in one discord msg
         full_response = supress_msg_body_url_embeds(full_response)
         await message.reply(content= full_response  , mention_author= True)
      
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_links_msg( _gemini_response : tuple , _links_limit : int = 5 , discord_msg_limit = 2000, is_gemini:bool = True) -> tuple :


   links_msg_header = f"\n```ini\n [Sources & links]```" #len = 29 [0 -> 28]
   links_list = list( set( _gemini_response[1]) if is_gemini else set(_gemini_response[1]))#TODO: add gpt + #remove duplicate links

   #CHECK if there is images between the links and move them to gemini_images_list(at_end):

   i = 0
   while len(links_list) != 0  and i < len(links_list) :
      link = links_list[i]
      if link.endswith((".jpg",".png",".webp"))  or link.startswith( ("https://lh3.googleusercontent.com" , "https://www.freepik.com") ) or (link.find(".jpg") != -1) :
         links_list.remove(link)
         link = set(link)
         if _gemini_response[2] is not None:
            _gemini_response[2].union(link)

         i = 0 # not to got out of index after removal of a link
         continue #to prevent  inc and skip zeroth element!
      i += 1


   #LINKS MSG FRAGMENTER SECTION (send only first set of links until 'links_length <= 2000char' thats enough)
   tot_lnk_len = 0
   links_list_sz = len(links_list)
   extra_format_chars =  10 #newline and bullet points also is included in length
   links_msg_header_len = len(links_msg_header)
   lnks_no_lmt = 0 # while loop iterator + used later to find last allowed link indx
   lnk_cstm_lmt = 5 #TODO make discord sever admins can change custom links limit
   while  tot_lnk_len < discord_msg_limit - 1  and lnks_no_lmt < links_list_sz  and lnks_no_lmt < lnk_cstm_lmt: # msg_limit set to = actual_limit - 1 for safety
         tot_lnk_len += links_msg_header_len if  lnks_no_lmt == 0 else 0 #include link msg header length in tot len

         tot_lnk_len += len(links_list[lnks_no_lmt]) + extra_format_chars
         lnks_no_lmt += 1

   #if last link exceeds discord msg limit then will leave it else will take it
   lnks_no_lmt -= 1 if tot_lnk_len > discord_msg_limit - 1 else 0
   # (any way we take all links until first link  that its sum with the earlier links exceeds the limit for now we discard the rest of  links from gemini ans)

   #remove embed from all links except the first ( also works in discord chat !)
   lnk1_len = len(links_list[0]) # will be needed later in sub_sections_msg_sending_ctrl()
   for i in range(1 , lnks_no_lmt) :
      links_list[i] = '<' + links_list[i] + '>'


      #FINAL FORMAT FOR LINKS MESSAGE
   links_list[0] = '\n * '+ links_list[0]  # prepend with each link with bullet point
   final_links = links_msg_header  + '\n* '.join(links_list[ : lnks_no_lmt])  #list is zero based and end at limit - 1

   return (final_links , _gemini_response , lnk1_len)

#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_imgs_msg( _gemini_response : tuple , _imgs_limit : int = 5 , discord_msg_limit = 2000, is_gemini:bool = True) -> str :

   imgs_msg_header = f"\n```ini\n [Images]``` \n"
   
   imgs_list = list( set( _gemini_response[2]) if is_gemini else set(_gemini_response[2]) )#TODO: add gpt + #remove duplicate imgs

   #IMAGES MSG FRAGMENTER SECTION (currently discord only allow 5 messages per message and ignores the later ones and we'll stick with 5 images also at max)
   tot_img_len = 0
   imgs_list_sz = len(imgs_list)
   imgs_discord_lmt = 5
   imgs_crnt_lmt = _imgs_limit # while loop iterator + used later to find last allowed img indx

   i = 0
   while  tot_img_len < discord_msg_limit - 1  and i < imgs_crnt_lmt  and i < imgs_list_sz : # make sure i dont send more than 5 images + make sure that  links of images doesnt exceed 2000char + also make sure  dont go passs imgs_list size
         tot_img_len += len(imgs_list[i])
         i += 1

   allowed_imgs : int = i
   #if last imgs link length exceeds discord msg limit then will leave it else will take it
   allowed_imgs -= 1 if tot_img_len > discord_msg_limit - 1 else 0
   # (any way we take all imgs until first img  that its sum with the earlier imgs exceeds the limit of (links chars len or imgs no.)for now we discard the rest of  imgs from gemini ans)


   #FINAL FORMAT FOR imgs MESSAGE
   final_imgs = imgs_msg_header + '\n'.join(imgs_list[ : imgs_crnt_lmt])  #list is zero based and end at limit - 1
   return final_imgs
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
   return greetings[ini.random.randint(0 , last_elmnt_index)]
#------------------------------------------------------------------------------------------------------------------------------------------#

def skip_line(full_ans):
  lines = full_ans.split('\n')
  return '\n'.join(lines[1:])
#------------------------------------------------------------------------------------------------------------------------------------------#
class UserAiQuery:
   queries_limit = 100
   command_query_tokken_limit = 300
   chats_ai_dict: dict = {} #key:value => {'userid': UserAiChat_obj}
   
   def __init__(self, userId:str):
      self.userId = userId
      
      if self.userId not in self.chats_ai_dict:
         self.chats_ai_dict[userId] = self
         #each history element(gpt): {'role': system,user,asistant ,'content': str}
         self.history_gpt: list[dict] = []
         self.history_gemini: list[dict] = []
         self.history_deepSeek: list[dict] = []
         
      else: 
         #dont make new/reset history there is already one! (mostly this won't happen we handle this before making new obj. But! just in case...)
         self.history_gpt: list[dict] = self.chats_ai_dict[userId].history_gpt
         self.history_gemini: list[dict] = self.chats_ai_dict[userId].history_gemini
         self.history_deepSeek: list[dict] = self.chats_ai_dict[userId].history_deepSeek
         self.chats_ai_dict[userId].__del__()
         if userId in self.chats_ai_dict: del self.chats_ai_dict[userId]
         self.chats_ai_dict[userId] = self
   
   @classmethod
   async def prepare_chat(cls, _user: discord.User, _AI: str, **kwargs):
      if _AI == "gpt":
         user_name = _user.display_name
         userId: str = str(_user.id)
         character= "GPTeous Wizard whose now living in discord server called Narol's Island"
         series = "Harry Potter"
         sys_prompt = f"""I want you to act like {character} from {series}.
         I want you to respond and answer like {character} using the tone,
         manner and vocabulary {character} would use.
         Do not write any explanations.
         Only answer like {character}.
         You must know all of the knowledge of {character}. 
         Use some emojies just a little bit!.
         My first sentence is \"Hi {character} I'm {user_name}. {kwargs["_query"]} \""
         """
         gpt_user_msg = [{'role': 'user', 'content': kwargs["_query"]}]
         chat_dict = UserAiSpecialChat.chats_ai_dict if kwargs["_is_wizy_ch"] else cls.chats_ai_dict
         
         #TESTING
         print(f"\n\n\n\n\n\n\n TESTING############# \n\n\n gpt payload:  \n\n\n is special channel {kwargs['_is_wizy_ch']}  ############# \n\n\n")
         #TESTING
         
         if userId in chat_dict:
            chat_dict[userId].append_chat_msg(msg= gpt_user_msg, ai_type= 'gpt')
            user_gpt_history = chat_dict[userId].history_gpt
            
         else: #new chat with gpt
            new_chat = UserAiSpecialChat(userId) if kwargs["_is_wizy_ch"] else cls(userId) 
            # tell th AI tokkens limit  to assure him to not send longer messages!
            tokken_limit = new_chat.chat_query_tokken_limit if kwargs['_is_wizy_ch'] else new_chat.command_query_tokken_limit
            sys_prompt += f"\nResponse must not exceed {tokken_limit} tokkens!"
            gpt_starter_prompt =[
               {"role": "system", "content": sys_prompt}
               ]

            new_chat.append_chat_msg(msg= gpt_starter_prompt, ai_type= 'gpt')
            chat_dict[str(userId)] = new_chat
            user_gpt_history = chat_dict[userId].history_gpt

         #TESTING
         print(f"\n\n\n\n\n\n\n TESTING############# \n\n\n gpt payload:  \n\n\n {user_gpt_history}  ############# \n\n\n")
         #TESTING
         
         
         if not kwargs["_is_wizy_ch"]: # set max token limit for query types of requests
            gpt_payload= await ini.gpt.chat.completions.create(
                  model="gpt-3.5-turbo",
                  max_tokens= UserAiQuery.command_query_tokken_limit,
                  messages= user_gpt_history
                  # stream= True
               )
         elif kwargs["_is_wizy_ch"]: # set max token limit for chat types of requests
            gpt_payload= await ini.gpt.chat.completions.create(
                  model="gpt-3.5-turbo",
                  max_tokens= UserAiSpecialChat.chat_query_tokken_limit,
                  messages= user_gpt_history
                  # stream= True
               )
         
         gpt_resp = gpt_payload.choices[0].message.content
         gpt_user_msg_resp = [{"role": "assistant", "content": gpt_resp}]
         chat_dict[userId].append_chat_msg(msg= gpt_user_msg_resp, ai_type= 'gpt')
   
         #TESTING
         print(f"\n\n\n\n\n\n\n TESTING############# \n\n\n gpt payload: {gpt_payload}  \n\n\n ############# \n\n\n")
         #TESTING
         
         return gpt_payload.id, gpt_resp
      
      elif _AI == "deep":
         user_name = _user.display_name
         userId: str = str(_user.id)
         character= "Deep Seeker Wizard whose now living in discord server called Narol's Island"
         series = "Harry Potter"
         sys_prompt = f"""I want you to act like {character} from {series}.
         I want you to respond and answer like {character} using the tone,
         manner and vocabulary {character} would use.
         Do not write any explanations.
         Only answer like {character}.
         You must know all of the knowledge of {character}. 
         Use some emojies just a little bit!.
         My first sentence is \"Hi {character} I'm {user_name}. {kwargs["_query"]} \""
         """
         deepSeek_user_msg = [{'role': 'user', 'content': kwargs["_query"]}]
         chat_dict = UserAiSpecialChat.chats_ai_dict if kwargs["_is_wizy_ch"] else cls.chats_ai_dict
         
         #TESTING
         print(f"\n\n\n\n\n\n\n TESTING############# \n\n\n gpt payload:  \n\n\n is special channel {kwargs['_is_wizy_ch']}  ############# \n\n\n")
         #TESTING
         
         if userId in chat_dict:
            chat_dict[userId].append_chat_msg(msg= deepSeek_user_msg, ai_type= 'deep')
            user_deepSeek_history = chat_dict[userId].history_deepSeek
            
         else: #new chat with gpt
            new_chat = UserAiSpecialChat(userId) if kwargs["_is_wizy_ch"] else cls(userId) 
            # tell th AI tokkens limit  to assure him to not send longer messages!
            tokken_limit = new_chat.chat_query_tokken_limit if kwargs['_is_wizy_ch'] else new_chat.command_query_tokken_limit
            sys_prompt += f"\nResponse must not exceed {tokken_limit} tokkens!"
            deepSeek_starter_prompt =[
               {"role": "system", "content": sys_prompt}
               ]

            new_chat.append_chat_msg(msg= deepSeek_starter_prompt, ai_type= 'deep')
            chat_dict[str(userId)] = new_chat
            user_deepSeek_history = chat_dict[userId].history_deepSeek

         #TESTING
         print(f"\n\n\n\n\n\n\n TESTING############# \n\n\n deepSeek payload:  \n\n\n {user_deepSeek_history}  ############# \n\n\n")
         #TESTING
         
         
         if not kwargs["_is_wizy_ch"]: # set max token to 250 if using gpt outside wizy special chat channel
            deepSeek_payload= await ini.deepSeek.chat.completions.create(
                  model="deepseek-chat",
                  max_tokens= UserAiQuery.command_query_tokken_limit,
                  messages= user_deepSeek_history,
                  temperature= 1.3 #temp. parameter details: https://api-docs.deepseek.com/quick_start/parameter_settings
                  # stream= True
               )
         elif kwargs["_is_wizy_ch"]: 
            deepSeek_payload= await ini.deepSeek.chat.completions.create(
                  model="deepseek-chat",
                  max_tokens= UserAiSpecialChat.chat_query_tokken_limit,
                  messages= user_deepSeek_history,
                  temperature= 1.3 #temp. parameter details: https://api-docs.deepseek.com/quick_start/parameter_settings
                  # stream= True
               )
         
         deepSeek_resp = deepSeek_payload.choices[0].message.content
         deepSeek_user_msg_resp = [{"role": "assistant", "content": deepSeek_resp}]
         chat_dict[userId].append_chat_msg(msg= deepSeek_user_msg_resp, ai_type= 'deep')
   
         #TESTING
         print(f"\n\n\n\n\n\n\n TESTING############# \n\n\n deepSeek payload: {deepSeek_payload}  \n\n\n ############# \n\n\n")
         #TESTING
         
         return deepSeek_payload.id,  deepSeek_resp
         
      elif _AI == "gemini" : #TODO
         ...
         

      
   def append_chat_msg(self, msg, ai_type:str = 'gpt') -> int :
      
      '''
      if return == 0 (fail)
      if return == 1 (done)
      if return == 2 (done + cleared history due to 'queries_limit' exceeding)
      '''
      
      if ai_type == 'gpt':
         #so we want only to clear if user msgs exceeds limit not all chat msgs
         user_msgs_cnt = (len(self.history_gpt) - 1) // 2
         if user_msgs_cnt >= self.queries_limit:
            self.history_gpt.clear()
            self.history_gpt += msg
            return 2#done + done + cleared history due to 'queries_limit' exceeding
         else: #still can append to history
            self.history_gpt += msg
            return 1
      elif ai_type == 'deep':
            #so we want only to clear if user msgs exceeds limit not all chat msgs
            user_msgs_cnt = (len(self.history_deepSeek) - 1) // 2
            if user_msgs_cnt >= self.queries_limit:
               self.history_deepSeek.clear()
               self.history_deepSeek += msg
               return 2#done + done + cleared history due to 'queries_limit' exceeding
            else: #still can append to history
               self.history_deepSeek += msg
               return 1
               
      elif ai_type == 'gemini': 
         #so we want only to clear if user msgs exceeds limit not all chat msgs
         user_msgs_cnt = (len(self.history_gemini) - 1) // 2
         if user_msgs_cnt >= self.queries_limit:
            self.history_gemini.clear()
            self.history_gemini += msg
            return 2 #done + done + cleared history due to 'queries_limit' exceeding
         else: #still can append to history
            self.history_gemini += msg
            return 1 #done
         
      else: 
         return 0 #fail
   
      
   def change_chat_mode(self, user_id, mode:str, ai_type:str = 'gpt'):
      ... #TODO: also add a bot command that invokes it ('mode' is the system role content of GPT e.g.(funny GPT ...))
#------------------------------------------------------------------------------------------------------------------------------------------#
class UserAiSpecialChat(UserAiQuery):
   #NOTE: must reassign it here. otherwise the parent class 'chats_ai_dict' will be shared here ! ( wnna separate special channel chat history from normal command to talk with wizy in any other channel)
   chat_query_tokken_limit = 600
   chats_ai_dict: dict = {} 
   
#------------------------------------------------------------------------------------------------------------------------------------------#
#TODO GPT
async def ask_gpt(user_query, user: discord.User, is_wizy_ch:bool = False) -> tuple:
   resp_id_gpt, gpt_resp = await await_me_maybe( UserAiQuery.prepare_chat(_user= user, _AI="gpt", _is_wizy_ch= is_wizy_ch, _query= user_query) )
   
   return (gpt_resp, resp_id_gpt)
#------------------------------------------------------------------------------------------------------------------------------------------#
async def ask_deepSeek(user_query, user: discord.User, is_wizy_ch:bool = False) -> tuple:
   resp_id_deepSeek, deepSeek_resp = await await_me_maybe( UserAiQuery.prepare_chat(_user= user, _AI="deep", _is_wizy_ch= is_wizy_ch, _query= user_query) )
   
   return (deepSeek_resp, resp_id_deepSeek)
#------------------------------------------------------------------------------------------------------------------------------------------#

async def ask_gemini(user_query: str, user= discord.user ) -> tuple:
   
   user_name = user.display_name
   character= "GPTeous Wizard whose now living in discord server called Narol's Island "
   series = "Harry Potter"
   classic_prmpt = f"act as a wizard named Gpteous living in master Narol's island. start and end of  answer  must be  in wizardish sentences and  the  rest must be using normal english. include emojis. prompter name: {user_name}. prompter's question: {user_query}"
   new_prompt = f"""I want you to act like {character} from {series}.
   I want you to respond and answer like {character} using the tone,
   manner and vocabulary {character} would use.
   Do not write any explanations.
   Only answer like {character}.
   You must know all of the knowledge of {character}.
   My first sentence is \"Hi {character} I'm {user_name}. {user_query} .\"
   """
   
   gemini_ans = await await_me_maybe(ini.gemini.get_answer(classic_prmpt))
   # return skip_line(gemini_ans['content']) , gemini_ans['links'] , gemini_ans['images'] , gemini_ans['response_id'] , gemini_ans['conversation_id'] # skip first line that has my prompt
   return gemini_ans['content'] , gemini_ans['links'] if 'links' in gemini_ans else None , gemini_ans['images'] , gemini_ans['response_id'] , gemini_ans['conversation_id']
#------------------------------------------------------------------------------------------------------------------------------------------#
async def check_msg ( _message : discord.Message = None  , chk_type : int = 1 , targetChannelId : int | tuple = None , only_admins : bool = False , **extraArgs ) -> bool : 
   #TODO : later check type must be in dictionary contains all types and check it self becomes a class
   if chk_type == 1 and _message != None : #NOTE : checks for on_message() in wizard channel
      return True if  _message != None and _message.channel.id in targetChannelId and _message.author.id != ini.bot.user.id else False

   elif chk_type == 2 and _message != None:#NOTE : checks for  messages of type: reply
      msg_channel = _message.channel


      if _message.reference is None or _message.reference.message_id is None :
            return False , None
      else:
         first_msg_id = _message.reference.message_id
         first_msg_cntnt_task = ini.bot.loop.create_task(msg_channel.fetch_message(first_msg_id))
         first_msg_cntnt = await first_msg_cntnt_task
         first_msg_cntnt = first_msg_cntnt.content
         first_msg_cntnt_filtered = first_msg_cntnt.replace(f"<@{ini.wizard_bot_id}" , '').strip().replace(" ", '')

         if len(first_msg_cntnt_filtered) == 0 :
            return False , -1

         else:
            print ("TESTING : ID of ref msg:" , _message.reference.message_id ) #TESTING
            return True , _message





   else: return False
#------------------------------------------------------------------------------------------------------------------------------------------#
gemini_conversation_ids_buffer = set()
def save_gpt_last_conversation_id() : ...  #TODO
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_discord_embed( _ans_data: tuple, is_reply: bool = False, is_gemini= True) -> discord.Embed :
   #TODO : handle if embed exceeds max size of max size of fields ( ini.bot will continue work anyway but tell user that OF happend of paganating)
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


   #TODO : this is a mess refactor it later you could do it in half codes!  
   if is_gemini :
      gemini_ans_data = _ans_data
      ansText = gemini_ans_data[0]
      footerIcon="https://em-content.zobj.net/thumbs/120/whatsapp/352/scroll_1f4dc.png"
      wizardChannelLink ="https://discord.com/channels/797143628215877672/1118953370510696498"
      note_compined_msg = "_This is combined response i.e.(more than one message) and still not perfectly formatted_"
      embedTitle = "MIGHTY GPTEOUS Ancient Scroll :scroll: Found! \n"
      timeNow = ini.datetime.now()
      author = "GEMINI AI"
      geminiIcon = "https://i.imgur.com/u0J6wRz.png"
      redTint = 10038562
      darkGreen = discord.Colour.dark_green()
      
      
      #TESTING BLOCK
      print ("\n\n\n TESTING : EMBED conetns lengths :")
      print ("ans text" , gemini_ans_data[0] )
      print ("#######ans text len" , len(gemini_ans_data[0]) )

      print ("links" , gemini_ans_data[1] )
      print ("images" , gemini_ans_data[2] )
      imgs_sz =0
      for img in gemini_ans_data[2]:
         imgs_sz += len(img)
      print ("#######imgs len" , imgs_sz)
      print ("############# len images" , imgs_sz)
      tot_len = len(gemini_ans_data[0]) + len(gemini_ans_data[1]) + len(gemini_ans_data[2]) + 200
      #TESTING BLOCK

      embed = discord.Embed(type='rich',
                            timestamp= timeNow,
                            color= darkGreen,
                            title= embedTitle,
                            url= wizardChannelLink,
                            description= ansText + " \n `*END OF ANSWER*` "
                            ) #url will be  hyperlink in title
      
      embed.set_author(name= author, url="https://gemini.google.com" , icon_url= geminiIcon )

      if gemini_ans_data[1] is not None and len(gemini_ans_data[1]) != 0 :

         gemini_ans_links = list(set(gemini_ans_data[1])) #NOTE = FOR SOME reason there is many redundancy in links so I removed duplicates

       #TESTING BLOCk
         link_sz =0
         for i in range(len(gemini_ans_data[1])):
            link_sz += len(gemini_ans_data[1][i])
         print ("#######links len" , link_sz)
      #TESTING BLOCk


         tot_len_of_links_sections = 0
         for i in range(len(gemini_ans_links)):
            tot_len_of_links_sections += len(gemini_ans_links[i])

         if tot_len_of_links_sections >= 1022:

            one_field_mx = 1022 #less than discord_limit  (for safety)
            super_list = [] #each element is an list of links / content that is tot char counts is <= 1023
            super_list.append([])
            links_list = gemini_ans_links
            max_i =  len(gemini_ans_links)
            char_cnt , field_indx , i  = 0 , 0 , 0 # vars controlling while loop
            bullet_point_format_len = 6
            while i < max_i:
               char_cnt += len(links_list[i]) + bullet_point_format_len #

               if char_cnt >= one_field_mx :
                  super_list[field_indx][0] = '\n * ' + super_list[field_indx][0] #fix join dont format 1st element
                  embed.add_field(name= f"_ __sources p({field_indx + 1})__  _",
                                  inline= False,
                                  value= '\n* '.join(super_list[field_indx]) 
                                  )
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
            gemini_ans_links[0] = '\n * ' + gemini_ans_links[0] #fix join dont format 1st element
            tmp = '\n * '.join(gemini_ans_links) #TESTING
            print ("TESTING final sources format " , tmp)
            embed.add_field(name= f"_ __sources & links__  _",
                            inline= False,
                            value= '\n * '.join(gemini_ans_links))

      if is_reply :
         embed.add_field(name= "_ __note__ _ " , inline= False , value= note_compined_msg)

      embed.set_footer(text= f"Scroll ID({gemini_ans_data[3]})" , icon_url= footerIcon )

      #TESTING BLOCK
      field_sz += len((embed.fields)[i])
      print ("\n\n###### embed field sz" ,field_sz)
      print ("###### embed author sz "  ,len(embed.author))
      print ("###### embed desc sz "  ,len(embed.description))
      print ("###### embed foot sz " ,len(embed.footer))
      print ("###### embed title " ,len(embed.title))
      print ("###### embed tot " ,len(embed))
      #TESTING BLOCK
   
   elif not is_gemini:
      gpt_ans_data = _ans_data
      ansText = gpt_ans_data[0]
      ansID = gpt_ans_data[1]
      footerIcon="https://em-content.zobj.net/thumbs/120/whatsapp/352/scroll_1f4dc.png"
      wizardChannelLink ="https://discord.com/channels/797143628215877672/1118953370510696498"
      note_compined_msg = "_This is combined response i.e.(more than one message) and still not perfectly formatted_"
      embedTitle = "MIGHTY GPTEOUS Ancient Scroll :scroll: Found! \n"
      timeNow = ini.datetime.now()
      author = "Found Ancient Scroll!"
      gptIcon = "https://i.imgur.com/UTbxXpc.jpg"
      redTint = 10038562 #a color
      darkGreen = discord.Colour.dark_green()

      embed = discord.Embed(type='rich',
                            timestamp= timeNow,
                            color= redTint,
                           #  title= embedTitle,
                            url= wizardChannelLink, 
                            description= ansText + " \n `E N D` "
                            ) #url will be  hyperlink in title
      
      embed.set_author(name= author, url=wizardChannelLink, icon_url= None )
      if ini.bot.wizy_chat_ch_ai_type == 'gpt' :
         embed.set_footer(text= f"Scroll ID({ansID}) • powered by OpenAI", icon_url= footerIcon )
      elif ini.bot.wizy_chat_ch_ai_type == 'deep' :
         embed.set_footer(text= f"Scroll ID({ansID}) • powered by DeepSeek\U0001F40B", icon_url= footerIcon ) #utf code is for whale emoji 🐋
      if is_reply :
         embed.add_field(name= "_ __note__ _ " , inline= False , value= note_compined_msg)


   return embed
#------------------------------------------------------------------------------------------------------------------------------------------#



async def get_new_reply_prompt(_message : discord.Message, old_prompt : str ) -> str :
   first_msg_id = _message.reference.message_id


   msg_fetch_task = ini.bot.loop.create_task(_message.channel.fetch_message(first_msg_id))
   first_msg_content = await msg_fetch_task
   first_msg_content : discord.Message.content = first_msg_content.content

   first_msg_content : str =  first_msg_content.replace(f"<@{ini.wizard_bot_id}" , ' ')#if other commands like 'gemini' or 'wizard' its mostly ok # NOTE : (still testing)
   new_prompt : str = old_prompt + ' ' + f"\"{first_msg_content}\""


   return new_prompt
#------------------------------------------------------------------------------------------------------------------------------------------#
async def prepare_quote(invoker : int , retrylimit : int = 10) -> str : #TODO : make it fully async
   """_summary_
   invoker : 0 wisewiz command , 1 send_rand_quote_meme()

   Args:
       invoker (int): _description_

   Returns:
       str: the final quote msg
   """

   res = None
   quotes = " "

   if invoker == 0 : #wisewiz invoked uses old pyrandmeme2 (not async)
      # from commands_bot import custom_quote_threshhold #NOTE: bad way if importing global non-const values
      import commands_bot  as cmd

      #res : dict =  [{'author': 'J.R.R. Tolkien', 'book': 'The Fellowship of the Ring', 'quote': "I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve."}]c
      discord_msg_mx_len = 1965 #actually its 2000char max but we will append 35 chars later to the quote

      print(f"\n\n\n #######TESTING current quote size in char 'custom_quote_threshhold' : {cmd.custom_quote_threshhold} ###\n\n")#TESTING

      requests_limits = retrylimit #times to search proper length quote threshold
      while requests_limits != 0 and ( res is None  or len(res[0]['quote']) > int(cmd.custom_quote_threshhold) ):
         random_word = ini.RandomWords()
         category = random_word.get_random_word()
         res = ini.quote(category , limit=1)
         requests_limits -= 1

      if  res is None  or len(res[0]['quote']) > int(cmd.custom_quote_threshhold) :
         quotes = f"***Ops! No quote For this time***"
      else :
         for i in range(len(res)): # loop if there is multiple quotes e.g.(limit > 1)#TODO: multiple quotes in one command
            quotes : str = f"> {res[i]['quote']} `-GPTeous A. Wise Spirit;`" #TODO: make it list /array of strings if used multiple quotes in one command

   elif invoker == 1: #invoked by send_rand_quote_meme() (use async asyncforistmatic lib)
      async_qoute_task = await ini.bot.loop.create_task(ini.foris.async_quote())  #won't type author to encourage discord server users to search about the quote!
      await aio.sleep(2)
      res , _author =  async_qoute_task
      quotes = discord.Embed(type='rich' , description= res).set_footer()
      quotes.set_footer(text= f" © GPTeous A. Wise Spirit;")

   else :
      pass #TODO

   return quotes
#------------------------------------------------------------------------------------------------------------------------------------------#
def extract_post_info(res: aiohttp.JsonPayload, sz: int):
   rand_post_no = ini.random2.randint(0,sz - 1)
   
   #TESTING BLOCK
   tst_has_crosspost_parent_list: bool = True if "crosspost_parent_list" in res['data']['children'][rand_post_no]['data']  else False
   print(f"\n\n\n\n\n TESTING########### \n\n\n invoked palestina_free(): reddit palestine list size : {sz} \n\n\n #########\n")
   print(res['data']['children'][rand_post_no]['data'])
   print(f"has_crosspost_parent_list?: {tst_has_crosspost_parent_list}")
   #TESTING BLOCK
   
   
   
   # chosen_post_url: this url var might be later changed to maybe video url not post. and might add discrod markdown foramtting to it 
   chosen_post_url: str = res['data']['children'][rand_post_no]['data']['url']
   # org_post: this will always stay raw reddit post url with maybe only disable embed discord markdown added to it at very end 
   # (json itself might return an image url but it's ok for me)
   org_post: str = res['data']['children'][rand_post_no]['data']['url']
   chosen_post_text: str = res['data']['children'][rand_post_no]['data']['title']
   
   #this key in the json appears when it's a video but marked spoiler (to my knowledge) and outer 'is_video' key will show false which is wrong! there is a video!
   has_crosspost_parent_list: bool = True if "crosspost_parent_list" in res['data']['children'][rand_post_no]['data'] else False
   is_video: bool = res['data']['children'][rand_post_no]['data']['is_video'] 
   
   post_extracted_info: list = [rand_post_no,
                          chosen_post_url,
                          org_post,
                          chosen_post_text,
                          has_crosspost_parent_list,
                          is_video]
   return (*post_extracted_info,) #without the tuple brackets can't unpack in return statement
   
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_ps_event(res: aiohttp.JsonPayload, rand_post_no:int, special_type: str, **kwargs):
   image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".psd", ".raw", ".cr2", ".nef", ".dng", ".arw", ".orf", ".sr2"]
   org_post = kwargs['org_post']
   
   if not kwargs['is_video'] and not kwargs['has_crosspost_parent_list']:
      if res['data']['children'][rand_post_no]['data']['media'] is None:
         if kwargs['chosen_post_url'].endswith(tuple(image_extensions)) :#not video
            kwargs['free_palestina_data'] = discord.Embed(title= kwargs['title'] , description= kwargs['chosen_post_text'] + '\npost: ' + kwargs['chosen_post_url'], color=0xff2a2a)
            kwargs['free_palestina_data'].set_image(url= kwargs['chosen_post_url'] )
         else: #not video
            kwargs['chosen_post_url'] = res['data']['children'][rand_post_no]['data']['url']
            org_post = "" if org_post ==  kwargs['chosen_post_url'] else f"<{org_post}>"
            kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: {org_post}'
      else: #not video
         kwargs['chosen_post_url'] = res['data']['children'][rand_post_no]['data']['url']
         org_post = "" if org_post ==  kwargs['chosen_post_url'] else f"<{org_post}>"
         kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: {org_post}'
         
   elif not kwargs['is_video'] and kwargs['has_crosspost_parent_list']:
      is_crossparent_video = res['data']['children'][rand_post_no]['data']['crosspost_parent_list'][0]['is_video']
      if is_crossparent_video:
         kwargs['is_video'] = is_crossparent_video
         chosen_post_video = None if res['data']['children'][rand_post_no]['data']["crosspost_parent_list"][0]['media']["reddit_video"]["fallback_url"] is None else res['data']['children'][rand_post_no]['data']["crosspost_parent_list"][0]['media']["reddit_video"]["fallback_url"]
         kwargs['chosen_post_url'] = '||' + kwargs['chosen_post_url'] + '||' if chosen_post_video is None else '||'+ chosen_post_video + '||'
         org_post = "" if org_post ==  kwargs['chosen_post_url'] else f"<{org_post}>"
         kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: {org_post}'
      else: # not video
         kwargs['free_palestina_data'] = discord.Embed(title= kwargs['title'], description= kwargs['chosen_post_text']+ '\npost: ' + kwargs['chosen_post_url'], color=0xff2a2a)
         kwargs['free_palestina_data'].set_image(url= kwargs['chosen_post_url'])
   elif kwargs['is_video']: 
      chosen_post_video = None if res['data']['children'][rand_post_no]['data']['media']['reddit_video']['fallback_url'] is None else res['data']['children'][rand_post_no]['data']['media']["reddit_video"]["fallback_url"]
      kwargs['chosen_post_url'] = kwargs['chosen_post_url'] if chosen_post_video is None else chosen_post_video
      org_post = "" if org_post ==  kwargs['chosen_post_url'] else f"<{org_post}>"
      kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: {org_post}'
      
      
   return [kwargs['is_video'], kwargs['free_palestina_data'], kwargs['chosen_post_url']]
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_special( res: aiohttp.JsonPayload, rand_post_no:int, special_type: str, **kwargs ):
   
   special_type = special_type.lower()
   prepared_special: list = []
   
   if special_type == 'ps':
      prepared_special = list(
                              prepare_ps_event(res,
                                 rand_post_no,
                                 special_type= 'ps',
                                 chosen_post_url= kwargs['chosen_post_url'],
                                 org_post= kwargs['org_post'],
                                 chosen_post_text= kwargs['chosen_post_text'],
                                 has_crosspost_parent_list= kwargs['has_crosspost_parent_list'],
                                 is_video= kwargs['is_video'],
                                 title= kwargs['title'])
                             )
      
      
   elif special_type == ...:
      ... #TODO: to add extra events later
      
   return (*prepared_special,) #without the tuple brackets can't unpack in return statement
#------------------------------------------------------------------------------------------------------------------------------------------#
async def  final_send_special_ps(target_channel: discord.TextChannel, ps_post_embed_is_video: bool, ps_post_data: str|discord.Embed, ps_post_url: str ) -> discord.Message | None : 
   is_ok_embed_data: bool = type(ps_post_data) == discord.Embed
   
   if not ps_post_embed_is_video and is_ok_embed_data:
      sent_msg = await target_channel.send(embed= ps_post_data)
   else: #is video and/or data variable is str not discord.Embed
      sent_msg = await target_channel.send(content= ps_post_data + '\n' + ps_post_url )
   
   return sent_msg
#------------------------------------------------------------------------------------------------------------------------------------------#
async def send_rand_quote_meme(target_channel : discord.TextChannel = None, is_special: bool = False) :
   from init_bot import wizy_feed_channels
   target_channel = ini.bot.get_channel(wizy_feed_channels[0]) #TODO: 1) read all channels from jason 2) assign channels for each server 3)cotinue edit the structure to work on multiple servers

   print("\ntime NOW" ,ini.datetime.now() )
   print(f"\n\n")

   print(f"#########################################")#testing
   skip_trig = True if ini.random.randint(1, 3) == 1 else False # 2/3 probability to send and not skip
   print("TRIGGERED! and NOT skipped!") if not skip_trig else print("TRIGGERED! but skipped")#TESTING

   print("\ntime NOW", ini.datetime.now() )
   print(f"\n\n")

   if is_special : #special event (experimental) 
      print(f"\n#####bot CHOICE IS FREE PALESTINE!\n")#TESTING
      ps_post_get_task = await ini.bot.loop.create_task(ini.palestina_free())
      await aio.sleep(3)
      
      ps_post_embed_is_video, ps_post_data , ps_post_url = await await_me_maybe(ps_post_get_task)
      await final_send_special_ps(target_channel, ps_post_embed_is_video, ps_post_data, ps_post_url)
      await aio.sleep(3)
      
      return 2 #special event type: free Palestine!
      

   meme_or_quote  = True if ini.random.randint(1,3) == 1 else False   #1 == quote  else = meme   (~66% to get meme)

   if not skip_trig  and meme_or_quote != True : #meme
      print(f"\n#####bot CHOICE IS MEME!\n")#TESTING
      meme_get_task = await ini.bot.loop.create_task(ini.pyrandmeme2(_title= "Some Wizardy Humor👻"))
      await aio.sleep(3)
      meme_embed : discord.Embed = await await_me_maybe(meme_get_task)
      await target_channel.send(embed= meme_embed)
      await aio.sleep(3)
   elif not skip_trig and meme_or_quote == True : #quote
      quote_proivder = ini.random.randint(0,1)
      print(f"\n#####BOT CHOICE IS Quote! quote privder id: {quote_proivder} \n")#TESTING
      prepare_quote_task = await ini.bot.loop.create_task(prepare_quote(invoker= quote_proivder , retrylimit= 10))
      await aio.sleep(3)
      quote = await await_me_maybe(prepare_quote_task)
      await target_channel.send(embed= quote) if quote_proivder == 1 else await target_channel.send( quote )
      await aio.sleep(3)
   # elif (for jokes and gaming news api) #TODO

#------------------------------------------------------------------------------------------------------------------------------------------#
class tracks_queue: #TODO
   guilds_connected_queues: dict[ discord.Guild.id, list[str] ] = {}
   #TODO

#------------------------------------------------------------------------------------------------------------------------------------------#
#NOTE: this is voice player/downloder implementation taken from discord.py examples : https://github.com/Rapptz/discord.py/blob/master/examples/basic_voice.py
# Suppress noise about console usage from errors
# youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or aio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        song = data['url'] if stream else ytdl.prepare_filename(data)
        filename = data['title']
        return cls(discord.FFmpegPCMAudio(song, **ffmpeg_options), data=data) , filename

#------------------------------------------------------------------------------------------------------------------------------------------#
async def process_send_togglerandom_cmd(ctx: ini.commands.Context, _state: int, _interval_minutes: int):
   
   #incase we received it as numeric string value 
   _interval_minutes = int(_interval_minutes) 
   
   
   #only change if not same as current frequency
   current_post_freq = int(ini.bot.auto_memequote_sender_task.minutes)
   if _interval_minutes != current_post_freq:
      await ini.bot.set_memequote_sender_frequency(_interval_minutes)
   
   state = None if _state is None else int(_state)
   special_event = 2 #specially made 2 switch memes and quotes to post on palestine only (and for any special events later on)
   start, stop = 1, 0
   if state is None:
      await ini.bot.toggle_auto_memequote_sender_state(state = start) if ini.bot.is_auto_memequote_state == 0 else await ini.bot.toggle_auto_memequote_sender_state(state= stop)
      await ctx.reply(
                  delete_after= 15.0,
                  content=f"random memes & quotes feature is {'`Enabled`' if ini.bot.is_auto_memequote_state != 0  else '`Disabled`' } & frequency is `post/{_interval_minutes / 60.0}hour` "
                  )
   elif state == 0:
      await ini.bot.toggle_auto_memequote_sender_state(state = stop) 
      await ctx.reply(
                  delete_after= 15.0,
                  content=f"random memes & quotes feature is {'`Enabled`' if ini.bot.is_auto_memequote_state != 0  else '`Disabled`' } & frequency is `post/{_interval_minutes / 60.0}hour` "
                  )
      
   elif state == 1:
      await ini.bot.toggle_auto_memequote_sender_state(state = start)
      await ctx.reply(
                  delete_after= 15.0,
                  content=f"random memes & quotes feature is {'`Enabled`' if ini.bot.is_auto_memequote_state != 0 else '`Disabled`' } & frequency is `post/{_interval_minutes / 60.0}hour` "
                  )
      
   elif state >= special_event: #special events has value >= 2
      await ini.bot.toggle_auto_memequote_sender_state(state = special_event) 
      await ctx.reply(
                  delete_after= 15.0,
                  content=f"random memes & quotes feature is on **special event mode**:  `special event id: {'Free Palestine!' if special_event == 2 else special_event}` & `frequency: post/{_interval_minutes / 60.0}hour` "
                  )
      
   await ctx.message.delete(delay= 15.0)
   ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
async def process_send_quotesz_cmd(ctx: ini.commands.context, _quote_sz: str, _quote_threshhold:int, _max_sz:int):
   max_quote_size = _max_sz
   
   if _quote_sz is None or len(_quote_sz) <= 0 :
      bot_reply_msg: discord.Message = await ctx.reply(delete_after= 15.0,
                                                       content=f"Ops! please specify  `Quotes max size` current is `{_quote_threshhold}` "
                                                       )
      await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   elif not _quote_sz.isnumeric() :
      bot_reply_msg: discord.Message = await ctx.reply(delete_after= 15.0,
                                                       content=f"Ops! Quote size must be a numeric value! current is `{_quote_threshhold}` "
                                                       )
      await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   elif int(_quote_sz) > max_quote_size :
      bot_reply_msg: discord.Message = await ctx.reply(
                  delete_after= 15.0,
                  content=f"Ops! max Quote size is {max_quote_size}! current size is `{_quote_threshhold}` "
                  )
      await bot_reply_msg.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   else:
      _quote_threshhold = int(_quote_sz)
      bot_reply_msg: discord.Message = await ctx.reply(delete_after= 15.0,
                     content=f"Quotes max size is now set to `{_quote_threshhold}`"
                     )
      await bot_reply_msg.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
      await ctx.message.delete(delay= 15.0)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
async def process_send_change_wizy_ai_cmd(ctx: ini.commands.context, _ai_name:str):
   ai_models = ['gpt','gemini', 'deep']
   if _ai_name == None or _ai_name not in ai_models :
      await ctx.message.delete(delay= 15)
      await ctx.reply(f"Ops! you must choose a valid AI model: `{' , '.join(ai_models)}`. *current model is `{ini.bot.wizy_chat_ch_ai_type}`*", delete_after= 15)
      ctx.interaction or await ctx.message.add_reaction('\U0000274C') #❌ mark unicode == '\U0000274C'
   else:
      ini.bot.wizy_chat_ch_ai_type = _ai_name
      await ctx.message.delete(delay= 15)
      await ctx.reply(f"Wizard AI Chat Channel model Has been set to:  `{_ai_name}`!", delete_after= 15)
      ctx.interaction or await ctx.message.add_reaction('\U00002705') #✅ mark unicode == '\U00002705'
#------------------------------------------------------------------------------------------------------------------------------------------#
   

      
      
