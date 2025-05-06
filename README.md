 [![Live version badge](https://img.shields.io/badge/Live%20Version-Maintainance-red?logo=amazonaws)](https://github.com/orsnaro/Discord-Bot-Ai/tree/production-AWS) 
 [![lastest pre release was](https://img.shields.io/github/release-date-pre/orsnaro/discord-bot-ai?label=latest%20release&color=9332af)](https://github.com/orsnaro/discord-bot-ai/releases/latest)
[![Deploy-workflow-status](https://github.com/orsnaro/Discord-Bot-Ai/actions/workflows/aws-disc-bot-repo-actions.yml/badge.svg?branch=production-AWS)](https://github.com/orsnaro/Discord-Bot-Ai/actions/workflows/aws-disc-bot-repo-actions.yml)

# __Discord Bot Project (Wizard GPTeous)__  [![version badge](https://img.shields.io/badge/Remote%20Host-v2.5.6B-green)](TODO)



##### _Discord Bot with generative AI features using python as main project language_

![wizy image](./wizard_bot.ico "icon") 

---


> ## Officially [`2.5.6B`](https://github.com/orsnaro/Discord-Bot-Ai/releases/tag/V2.5.6B) is out 🧙‍♂️🎊!


<details>
<summary><em>  ✨Patch (2.5.6B) notes </em> </summary>

* now wizy  lives on a home server running ♾️
* now wizy  supports partially DeepSeek R1 AI model 🐳
* and more! **Full Changelog**: https://github.com/orsnaro/Discord-Bot-Ai/compare/V2.5.5B...V2.5.6B
</details>

      
      
  
 * now Finally you can use Chat GPT for free via our wizy bot -_[video](https://youtu.be/8Je6Pb5EYmI)_- in discord (you are also free to choose between `gpt` or `bard` though bard's API isn't stable at all!)
     
 * now understands your arabic messages! 

 * now can enjoy Mighty GPTeuos memes using `/BoringWizard` command
 
 * now all bot commands work in slash commands menu! as well as classic commands style

 * now can enjoy Mighty GPTeuos memes using `/BoringWizard` command

 * now can learn for the Wisest on [Discord's Lands](https://discord.com/invite/Y23B7R3FPq) using `/WiseWiz` command

 * now chat mode is live! get Wizy DeepSeeker answers in [`🟢🧙Ask-the-Wizard Channel`](https://discord.gg/ptAVHmrtJX)

 * now Bot sends random quotes and memes multiple times a day

 * now bot has basic voice commands e.g.(`/wizyjoin`/`/wizyleave`) commands


* and more! (just type `/help`) 

 </details>
 
> [!IMPORTANT]  
> #### NEW release is out ( patch `V2.5.6B`  )! [Latest Release Notes](https://github.com/orsnaro/Discord-Bot-Ai/releases/latest)

> [!IMPORTANT]  
> #### Now Bot is hosted on AWS EC2 servers(🔴)! [AWS-branch](https://github.com/orsnaro/Discord-Bot-Ai/blob/production-AWS)
---




</br>
</br>
</br>





> ##  🧙 How to Use Me?!

&ensp;***FIRST***: &ensp;&nbsp;✔️Invite me to a server  [`invite link`](https://discord.com/api/oauth2/authorize?client_id=1117540489365827594&permissions=8&scope=bot%20applications.commands)

***SECOND***: ✔️type `/help` in any Chat channel to learn my commands then use them!
   
***FINALLY***: &nbsp;✔️report me any issues!
   
<sub> ***NOTE:*** _for now_ you wouldn't be able to make your own  special channels e.g.( [`🧙Ask-the-wizard channel`](https://discord.gg/ptAVHmrtJX) ) try it in our [**server**](https://discord.com/invite/Y23B7R3FPq). If you want to add  wizy(feed,voice,chat) channels to your server contact me! later on this will be available to all via a command isha</sub>

<sub> ***NOTE:*** the bot does not have any `adminstration` / `managing` / `moving` /  etc.. permissions. though I  recommend always to take a look at allowed permissions in <br> [`beta-bot invite link`](https://discord.com/api/oauth2/authorize?client_id=1117540489365827594&permissions=8&scope=bot%20applications.commands). feel free to sneak peak at our soucre code for any future changing of these intents/permissions💙 </sub>


</br>
</br>


> ##  🛠 TODO :
#### ~⚠️ Do This BEFORE any New Features  &rarr;  *MIGRATE TO PYCORD.py!*~ -> [discord.py](https://github.com/Rapptz/discord.py)  is maintained Again!

<details>
<summary><em>  ⌛  in-progress </em> </summary>
    
*  [ ]  Documentation for functions / classes repo. first readme.md draft
*  [ ] ON-reaction feedback feature :
<details>
<summary><em> <sub> details </sub> </em> </summary> 
when user reacts on a wizy message wizy responds depending on category of emoji (good, bad, need_help,idk) (feature name : bot ON-reaction feedback feature) (reaction response will only stay for ~5secs except responses to  need_help reactions) 
</details>

*  [ ] complete track/songs queue class and it's two commands look(https://stackoverflow.com/questions/61276362/how-to-play-the-next-song-after-first-finished-discord-bot)
       
*  [ ] tutorial video on all bot features and how to use and invite it to you server ( 2 videos short & long  )
    
*  [ ] make command groups or cogs
  
*   implement new Gemini feature _i.e.( upload image and ask about it )_ in your bot since it's now available and [Gemini API wrapper v0.1.27](https://github.com/dsdanielpark/Gemini-API/releases/tag/0.1.27) now also  supports it
  
    
* [ ]  send Embeds fragmented in parts/pages if it exceeds max size  (6000char) or exceeds max fields (25 field)  <sub>note: use pagination </sub>

*   show embedded images in Gemini answer (seperate images in links -> append them to an image section 'embed or normal message' -> show the images!)

* [ ]  wizard bot sqlite-DB  design and connect the DB with bot code
  
* [ ]  Implement `Competitive Programming` Features on Bot and [Narol's Island](https://discord.com/invite/Y23B7R3FPq) server  <sub>( more in  M O D S channels in the server)</sub>

* [ ]  OOP it!  and handle errors!

* [ ]  (bard)save last conversation ID (load it in init_bot.py) in text file and add command to start new conv. and set default  to continue old one.

*   ~complete [`Gemini_key_refresh.py`](./Gemini_key_refresh.py)~

* [ ]  add `TTS` feature : read text in audio + ability for bot to join voice chats

* [ ]  ADD `STT`  feature to enable full voice chat feature between bot and island server's users ( make bot make real voice chat with members)

* [ ] use [`Rapidapi`](https://rapidapi.com)

* [ ] complete your [`quote`](https://github.com/orsnaro/quote-async) lib fork and make it fully async.

*   add and test poe-API (starred at my GitHub)
     - _NOTE:_ DeepSeek API is the one used now due to connection and belling issues beteen GPT-API i.e.(openAI API) and my country (Egypt)

*   add command to switch between Gemini mode and poe-GPT mode
  
       *  _(NOT necessary  NEED any more! now Gemini speaks arabic and Gemini API python wrapper also supports that  just edit your internal prompt / appendings and formating to discord messages to have arabic variation)_
    
*   Edit your Gemini args. and prompt to send full arabic query to Gemini (Gemini now has arabic lang suuport)


 </details> 


<details>
<summary><em>  🟢 Done </em> </summary>
 
![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) add command to switch between BARD mode and poe-GPT mode
    
![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) converte all command to be hybrid (works in legacy style and new slash command style) -> use discord's new paradigm 'interaction based system'

![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) Bot Ambient track (MMO Chill music) via `wizyplay`

![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) Bot plays specific song from YouTube Music via `wizyplay url`

![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) remove all async sleep in commands and replace with cooldown inside the command itself

![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) Replace all your manual auto meme/quote sender logic with this (les bot event loop handle it auto!)(no need even for acync event control var):

![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~make message fragmenter function for both msg and links msg in utils_bot.py~
  
 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) ~repo. first readme.md draft~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)   ~Use any free hosting service for `beta` versions~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
) ~connect to a cdn that has memes / quotes  and set on_time() event to send to `chat-chill` and `Ask-the-Wizard`~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)   ~make bot see prev messages (use session)~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)
  ~talk to bot by mention him~  

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~talk to bot in specific channel no need to mention or trigger him by command just send the question as plain message~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)   ~reply to his message (take the content of replayed message and respond accordingly to it + new message)~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~use SESSION with ASYNC Gemini ( contact GeminiAPI maker or raise issue in their repo)(I was  kinda  wrong)~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~show embedded links in Gemini answer~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~show  images in Wizard special channel~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~send msg in parts is it exceeds max size in bot special channel~

<sub>  _more todoes and tasks in discrod `testing` channel and in [`main_wizard_bot.py`](./main_wizard_bot.py)_ </sub>


 </details> 
 




</br>
</br>
</br>




---
> ### [🧾 References ](./sources&refs.md)

  * **Active Branches lately:**  `main` and [`bot_pycordv2.5.xB`](https://github.com/orsnaro/Discord-Bot-Ai/edit/bot_pycordv2.5.xB)
