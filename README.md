
 [![Live version badge](https://img.shields.io/badge/Live%20Version-Maintainance-red?logo=amazonaws)](https://github.com/orsnaro/Discord-Bot-Ai/tree/production-AWS) 
 [![lastest pre release was](https://img.shields.io/github/release-date-pre/orsnaro/discord-bot-ai?label=latest%20release&color=9332af)](https://github.com/orsnaro/discord-bot-ai/releases/latest)
[![Deploy-workflow-status](https://github.com/orsnaro/Discord-Bot-Ai/actions/workflows/aws-disc-bot-repo-actions.yml/badge.svg?branch=production-AWS)](https://github.com/orsnaro/Discord-Bot-Ai/actions/workflows/aws-disc-bot-repo-actions.yml)

# __Discord Bot Project (Wizard GPTeous)__ 





##### _Discord Bot with generative AI features using python as main project language_

---


> ## 📣 Now Bot is hosted on AWS EC2 servers(🔴)!
[AWS-branch](https://github.com/orsnaro/Discord-Bot-Ai/blob/production-AWS)

> ## 📣 NEW release is out ( for patch V2.5.5B  )!
[Release v2.5.5B Notes](https://github.com/orsnaro/Discord-Bot-Ai/releases/tag/V2.5.5B)

<details>
<summary><em>  ✨Patch (2.5.5B) notes </em> </summary>
    
* add Special events feature to auto meme/quote sender
* activate one of current special events `FREE PALESTINE 🇵🇸🍉`
* add command for this event `/wizyawakened` (will mostly be the command to wellingly call the current event at any time instead of waiting the channel to send post by it self)
* fix some bugs regarding reddit post types
* fix some bugs in `/togglerandom` command also now can toggle special events using it with arg state=2


 </details> 
      
      
  

<details>
<summary><em>  ✨ Current version (v2.5B) main features! </em> </summary>

 * now Finally you can use Chat GPT for free via our wizy bot -_[video](https://youtu.be/8Je6Pb5EYmI)_- in discord (you are also free to choose between `gpt` or `bard` though bard's API isn't stable at all!)
 *     
 * now understands your arabic messages! 

 * now can enjoy Mighty GPTeuos memes using `/BoringWizard` command
 
 * now all bot commands work in slash commands menu! as well as classic commands style

 * now can learn from the Wisest on [Discord's Lands](https://discord.com/invite/Y23B7R3FPq) using `/WiseWiz` command

 * now long Bard AI answers is working in [`🧙Ask-the-Wizard Channel`](https://discord.gg/ptAVHmrtJX)

 * now Bot sends random quotes and memes multiple times a day

 * now bot has basic voice commands e.g.(`wizyjoin`/`wizyleave`/`wizyplay`/`wizypause`/`wizyresume`/`wizystop`) commands

 * now if wizy is free in a voice channel he plays an abmient chilling music track!
   
 * now wizy have special events in command and channel ! current special event `FREE PALESTINE 🇵🇸🍉`

 * _soon_ music/tracks queue feature!

 </details>


![ alt text for screen readers](./wizard_bot.ico "icon") 

</br>
</br>
</br>





> ##  🧙 How to Use Me?!

&ensp;***FIRST***: &ensp;&nbsp;✔️Invite me to a server  [`invite link`](https://discord.com/api/oauth2/authorize?client_id=1117540489365827594&permissions=8&scope=bot%20applications.commands)

***SECOND***: ✔️type `/help` in any Chat channel to learn my commands then use them!
   
***FINALLY***: &nbsp;✔️report me any issues!
   
<sub> ***NOTE:*** _for now_ you wouldn't be able to make your own  sepcial channel [`🧙Ask-the-wizard channel`](https://discord.gg/ptAVHmrtJX) for now only try it in our [**server**](https://discord.com/invite/Y23B7R3FPq) </sub>

<sub> ***NOTE:*** the bot does not have any `adminstration` / `managing` / `moving` /  etc.. permissions. though I  recommend always to take a look at allowed permissions in <br> [`beta-bot invite link`](https://discord.com/api/oauth2/authorize?client_id=1117540489365827594&permissions=8&scope=bot%20applications.commands). feel free to sneak peak at our soucre code for any future changing of these intents/permissions💙 </sub>


</br>
</br>


> ##  🛠 TODO :
#### ~⚠️ Do This BEFORE any New Features  &rarr;  *MIGRATE TO PYCORD.py!*~ -> [discord.py](https://github.com/Rapptz/discord.py)  is maintained Again!

<details>
<summary><em>  ⌛  in-progress </em> </summary>
    
*  [ ]  Documentation for functions / classes repo. first readme.md draft

*  [ ] complete track/songs queue class and it's two commands look(https://stackoverflow.com/questions/61276362/how-to-play-the-next-song-after-first-finished-discord-bot)
       
*  [ ] tutorial video on all bot features and how to use and invite it to you server ( 2 videos short & long  )
    
*  [ ] make command groups or cogs
  
* [ ]  remove any global variables
  
* [ ]  use `logging` library to print debug and testing info to console instead of `print()` (🔵DONE PARTIALLY)
  
* [ ] to increase bot speed and avoid non-async http api requests effects -> every  48 hour or initializing of bot  store new 24 memes and 24 quotes  locally
  
* [ ]  implement new bard feature _i.e.( upload image and ask about it )_ in your bot since it's now available and [Bard API wrapper v0.1.27](https://github.com/dsdanielpark/Bard-API/releases/tag/0.1.27) now also  supports it
  
    
* [ ]  send Embeds fragmented in parts/pages if it exceeds max size  (6000char) or exceeds max fields (25 field)  <sub>note: use pagination </sub>

* [ ]  show embedded images in bard answer (seperate images in links -> append them to an image section 'embed or normal message' -> show the images!)

* [ ]  wizard bot sqlite-DB  design and connect the DB with bot code
  
* [ ]  Implement `Competitive Programming` Features on Bot and [Narol's Island](https://discord.com/invite/Y23B7R3FPq) server  <sub>( more in  M O D S channels in the server)</sub>

* [ ]  OOP it!  and handle errors!

* [ ]  save last conversation ID (load it in init_bot.py) in text file and add command to start new conv. and set default  to continue old one.

* [ ]  complete [`bard_key_refresh.py`](./bard_key_refresh.py)

* [ ]  add `TTS` feature : read text in audio + ability for bot to join voice chats

* [ ]  ADD `STT`  feature to enable full voice chat feature between bot and island server's users ( make bot make real voice chat with members)

* [ ] use [`Rapidapi`](https://rapidapi.com)

* [ ] complete your [`quote`](https://github.com/orsnaro/quote-async) lib fork and make it fully async.

* [ ]  add and test poe-API (starred at my GitHub)
     - _NOTE:_ BARD API is the one used now due to connection and belling issues beteen GPT-API i.e.(openAI API) and my country (Egypt)

* [ ] add command to switch between BARD mode and poe-GPT mode
  
* [ ]  ~use google translator API~
  
    *    _(NOT necessary  NEED any more! now bard speaks arabic and bard API python wrapper also supports that  just edit your internal prompt / appendings and formating to discord messages to have arabic variation)_
    
* [ ] Edit your bard args. and prompt to send full arabic query to bard (Bard now has arabic lang suuport)


 </details> 


<details>
<summary><em>  🟢 Done </em> </summary>
    
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
)  ~use SESSION with ASYNC BARD ( contact BardAPI maker or raise issue in their repo)(I was  kinda  wrong)~

 ![**(DONE)**](https://img.shields.io/badge/DONE-green?style=for-the-badge
)  ~show embedded links in bard answer~

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

  * **Active Branches lately:**  `master` and [`bot_pycordv2.5.xB`](https://github.com/orsnaro/Discord-Bot-Ai/tree/bot_pycordv2.5.1B)
