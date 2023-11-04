"""
                          Coder : Omar
                          Version : v2.5.4B
                          version Date :  4 / 11 / 2023
                          Code Type : python | Discrod | BARD | HTTP | ASYNC
                          Title : Utility code for Discord Bot
                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]
"""
import init_bot as ini
import discord.message
import youtube_dl
import asyncio as aio
import aiohttp

#------------------------------------------------------------------------------------------------------------------------------------------#
async def await_me_maybe(value):
    if callable(value):
        value = value()
    if aio.iscoroutine(value):
        value = await value
    return value
#------------------------------------------------------------------------------------------------------------------------------------------#
async def play_chill_track(server: discord.Guild):
   track_path = r"./tracks/mmo_chill_skyrim&wticher3.mp3"
   await await_me_maybe(server.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=track_path)))
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
async def prepare_send_wizard_channel_ans_msg( _bard_response : tuple  , message : discord.Message , discord_msg_limit = 2000) :

   #Supress i.e.(no embed) any URL inside the msg body and not in links msg section
   bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** \n"
   full_response = bot_msg_header + _bard_response[0]

   print ("TESTING: " , full_response) #TESTING

#MSG FRAGMENTER SECTION ( TODO : make message fragmenter function for both msg and links msg in utils_bot.py )
   full_resp_len = len(full_response)
   if full_resp_len >= discord_msg_limit : #break bard response   to smaller messages to fit in discord msg

      bot_msg_header = f"***MIGHTY GPTEOUS Answers :man_mage:! *** `[this msg will be fragmented: exceeds 2000chars]`\n"
      full_response = bot_msg_header + _bard_response[0]
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


         elif needed_msgs == 1 and remain == 0 : #send end flag in discord msg to indicate end of full bard response
            msg_frag = full_response[ : ]
            await message.reply(content= msg_frag  , mention_author= True)
            await message.reply(content= end_flag  , mention_author= True)
            break

         else :
            msg_frag = full_response[ : discord_msg_limit] # from 0 to limit i.e.( 0 -> 1998 = 2000char)  end is not taken ( exclusisve )
            await message.reply(content= msg_frag  , mention_author= True)

         full_response = full_response[discord_msg_limit : ] # skip the sent fragment of message start after it for rest fragments
         needed_msgs -= 1


   else: #all bard response can fit in one discord msg
      full_response = supress_msg_body_url_embeds(full_response)
      await message.reply(content= full_response  , mention_author= True)
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_links_msg( _bard_response : tuple , _links_limit : int = 5 , discord_msg_limit = 2000) -> tuple :


   links_msg_header = f"\n```ini\n [Sources & links]```" #len = 29 [0 -> 28]
   links_list = list( set(_bard_response[1]) ) #remove duplicate links

   #CHECK if there is images between the links and move them to bard_images_list(at_end):

   i = 0
   while len(links_list) != 0  and i < len(links_list) :
      link = links_list[i]
      if link.endswith((".jpg",".png",".webp"))  or link.startswith( ("https://lh3.googleusercontent.com" , "https://www.freepik.com") ) or (link.find(".jpg") != -1) :
         links_list.remove(link)
         link = set(link)
         if _bard_response[2] is not None:
            _bard_response[2].union(link)

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
   # (any way we take all links until first link  that its sum with the earlier links exceeds the limit for now we discard the rest of  links from bard ans)

   #remove embed from all links except the first ( also works in discord chat !)
   lnk1_len = len(links_list[0]) # will be needed later in sub_sections_msg_sending_ctrl()
   for i in range(1 , lnks_no_lmt) :
      links_list[i] = '<' + links_list[i] + '>'


      #FINAL FORMAT FOR LINKS MESSAGE
   links_list[0] = '\n * '+ links_list[0]  # prepend with each link with bullet point
   final_links = links_msg_header  + '\n* '.join(links_list[ : lnks_no_lmt])  #list is zero based and end at limit - 1

   return (final_links , _bard_response , lnk1_len)

#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_imgs_msg( _bard_response : tuple , _imgs_limit : int = 5 , discord_msg_limit = 2000) -> str :

   imgs_msg_header = f"\n```ini\n [Images]``` \n"
   bard_imgs_list = list( set(_bard_response[2]) ) #remove duplicate imgs

   #IMAGES MSG FRAGMENTER SECTION (currently discord only allow 5 messages per message and ignores the later ones and we'll stick with 5 images also at max)
   tot_img_len = 0
   imgs_list_sz = len(bard_imgs_list)
   imgs_discord_lmt = 5
   imgs_crnt_lmt = _imgs_limit # while loop iterator + used later to find last allowed img indx

   i = 0
   while  tot_img_len < discord_msg_limit - 1  and i < imgs_crnt_lmt  and i < imgs_list_sz : # make sure i dont send more than 5 images + make sure that  links of images doesnt exceed 2000char + also make sure  dont go passs bard_imgs_list size
         tot_img_len += len(bard_imgs_list[i])
         i += 1

   allowed_imgs : int = i
   #if last imgs link length exceeds discord msg limit then will leave it else will take it
   allowed_imgs -= 1 if tot_img_len > discord_msg_limit - 1 else 0
   # (any way we take all imgs until first img  that its sum with the earlier imgs exceeds the limit of (links chars len or imgs no.)for now we discard the rest of  imgs from bard ans)


   #FINAL FORMAT FOR imgs MESSAGE
   final_imgs = imgs_msg_header + '\n'.join(bard_imgs_list[ : imgs_crnt_lmt])  #list is zero based and end at limit - 1
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

async def ask_bard(user_query : str , user_name = "Narol island master" ) -> tuple:
   character= "GPTeous Wizard whose now living in discord server called Narol's Island "
   series = "Harry Potter"
   classic_prmpt = f"act as a wizard named Gpteous living in master Narol's island. start and end of  answer  must be  in wizardish sentences and  the  rest must be using normal english. include emojis. prompter name: {user_name}. prompter's question: {user_query}"
   new_prompt = f"I want you to act like {character} from {series}. I want you to respond and answer like {character} using the tone, manner and vocabulary {character} would use. Do not write any explanations. Only answer like {character}. You must know all of the knowledge of {character}. My first sentence is \"Hi {character} I'm {user_name}. {user_query} .\""
   bard_ans = await await_me_maybe(ini.bard.get_answer(classic_prmpt))
   # return skip_line(bard_ans['content']) , bard_ans['links'] , bard_ans['images'] , bard_ans['response_id'] , bard_ans['conversation_id'] # skip first line that has my prompt
   return bard_ans['content'] , bard_ans['links'] if 'links' in bard_ans else None , bard_ans['images'] , bard_ans['response_id'] , bard_ans['conversation_id']
#------------------------------------------------------------------------------------------------------------------------------------------#
async def check_msg ( _message : discord.Message = None  , chk_type : int = 1 , targetChannelId : int | tuple = None , only_admins : bool = False , **extraArgs ) -> bool : #TODO : later check type must be in dictionary contains all types and check it self becomes a class
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
bard_conversation_ids_buffer = set()
def save_gpt_last_conversation_id() : ...  #TODO
#------------------------------------------------------------------------------------------------------------------------------------------#
def prepare_discord_embed( bard_ans_data : tuple  , is_reply : bool = False) -> discord.Embed :
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
   timeNow = ini.datetime.now()
   author = "Bard AI"
   bardIcon = "https://i.imgur.com/u0J6wRz.png"
   redTint = 10038562
   darkGreen = discord.Colour.dark_green()

   embed = discord.Embed(type='rich' , timestamp= timeNow , color= darkGreen , title= embedTitle ,url= wizardChannelLink , description= ansText + " \n `*END OF ANSWER*` ") #url will be  hyperlink in title
   embed.set_author(name= author, url="https://bard.google.com" , icon_url= bardIcon )

   if bard_ans_data[1] is not None and len(bard_ans_data[1]) != 0 :

      bard_ans_links = list(set(bard_ans_data[1])) #NOTE = FOR SOME reason there is many redundancy in links so I removed duplicates

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
               embed.add_field(name= f"_ __sources p({field_indx + 1})__  _"  , inline= False , value= '\n* '.join(super_list[field_indx]) )
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


   msg_fetch_task = ini.bot.loop.create_task(_message.channel.fetch_message(first_msg_id))
   first_msg_content = await msg_fetch_task
   first_msg_content : discord.Message.content = first_msg_content.content

   first_msg_content : str =  first_msg_content.replace(f"<@{ini.wizard_bot_id}" , ' ')#if other commands like 'bard' or 'wizard' its mostly ok # NOTE : (still testing)
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
            kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: <{org_post}>'
      else: #not video
         kwargs['chosen_post_url'] = res['data']['children'][rand_post_no]['data']['url']
         kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: <{org_post}>'
         
   elif not kwargs['is_video'] and kwargs['has_crosspost_parent_list']:
      is_crossparent_video = res['data']['children'][rand_post_no]['data']['crosspost_parent_list'][0]['is_video']
      if is_crossparent_video:
         kwargs['is_video'] = is_crossparent_video
         chosen_post_video = None if res['data']['children'][rand_post_no]['data']["crosspost_parent_list"][0]['media']["reddit_video"]["fallback_url"] is None else res['data']['children'][rand_post_no]['data']["crosspost_parent_list"][0]['media']["reddit_video"]["fallback_url"]
         kwargs['chosen_post_url'] = '||' + kwargs['chosen_post_url'] + '||' if chosen_post_video is None else '||'+ chosen_post_video + '||'
         kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: <{org_post}>'
      else: # not video
         kwargs['free_palestina_data'] = discord.Embed(title= kwargs['title'], description= kwargs['chosen_post_text']+ '\npost: ' + kwargs['chosen_post_url'], color=0xff2a2a)
         kwargs['free_palestina_data'].set_image(url= kwargs['chosen_post_url'])
   elif kwargs['is_video']: 
      chosen_post_video = None if res['data']['children'][rand_post_no]['data']['media']['reddit_video']['fallback_url'] is None else res['data']['children'][rand_post_no]['data']['media']["reddit_video"]["fallback_url"]
      kwargs['chosen_post_url'] = kwargs['chosen_post_url'] if chosen_post_video is None else chosen_post_video
      kwargs['free_palestina_data'] = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps: \n" + kwargs['chosen_post_text'] + f'\npost: <{org_post}>'
      
      
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
   from init_bot import memes_highlights_ch_id
   target_channel = ini.bot.get_channel(memes_highlights_ch_id)

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
