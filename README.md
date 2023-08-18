# __Discord Bot Project (Wizard GPTeous)__  [![version badge](https://img.shields.io/badge/Remote%20Host%20(down)-v2.5.2B-FF0000)](https://free.pylexnodes.net/)


##### _Discord Bot with generative AI features using python as main project language_

---


> ## 📣 new  patch (`v2.5.2B`) is out!

<details>
<summary><em>  ✨Patch (2.5.2B) notes </em> </summary>
    
* fixed quote length  in-accuracy 
* added new command `quotesz` to control quote length only for admins (btw `togglerandom` is now only for admins and some special roles)
* wizard tells you if you cant use specific command and who can!
* now some command messages will be deleted after being read to keep server channels clean
* fixed quote feature blocks bot event loop (tempror solution)
* fixed auto meme/quote sender feature!
* bot ping now is separated from users commands latency (still not 100% accurate)
* now bot can join and leave voice channels! (if not moved he stays most of time in  `admins room`)
* updated bard cookie 
 </details> 
      
  

<details>
<summary><em>  ✨ Current version (v2.5B) main features! </em> </summary>
    
 * now understands your arabic messages! ( but still responds in English will respond in arabic __soon...__)

 * now can enjoy Mighty GPTeuos memes using `BoringWizard` command

 * now can learn for the Wisest on [Discord's Lands](https://discord.com/invite/Y23B7R3FPq) using `WiseWiz` command

 * now long Bard AI answers is working in [`🧙Ask-the-Wizard Channel`](https://discord.gg/ptAVHmrtJX)

 * now Bot sends random quotes and memes multiple times a day

 * now bot has basic voice commands e.g.(`wizyjoin`/`wizyleave`) commands

    - <sub> (_🔴disabled temporarily_: &nbsp; not stable. though you can toggle  it via `toggle random`) command </sub>

 * ~~fixed some bugs~~

 </details>


![ alt text for screen readers](./wizard_bot.ico "icon") 

</br>
</br>
</br>





> ##  🧙 How to Use Me?!

&ensp;***FIRST***: &ensp;&nbsp;✔️Invite me to a server  [`invite link`](https://discord.com/api/oauth2/authorize?client_id=1117540489365827594&permissions=69241357196993&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Foauth2%2Fauthorize%3F%26client_id%3D1117540489365827594%26scope%3Dbot&response_type=code&scope=identify%20guilds%20gdm.join%20rpc.voice.read%20rpc.video.write%20rpc.activities.write%20messages.read%20applications.commands%20activities.read%20voice%20applications.commands.permissions.update%20dm_channels.read%20activities.write%20applications.store.update%20applications.builds.upload%20bot%20rpc.screenshare.read%20rpc.voice.write%20rpc%20guilds.join%20email%20role_connections.write%20relationships.read%20applications.entitlements%20applications.builds.read%20webhook.incoming%20rpc.screenshare.write%20rpc.video.read%20rpc.notifications.read%20guilds.members.read%20connections)

***SECOND***: ✔️type `help` in any Chat channel to learn my commands then use them!
   
***FINALLY***: &nbsp;✔️report me any issues!
   
<sub> ***NOTE:*** _for now_ you wouldn't be able to make your own  sepcial channel [`🧙Ask-the-wizard channel`](https://discord.gg/ptAVHmrtJX) for now only try it in our [**server**](https://discord.com/invite/Y23B7R3FPq) </sub>

<sub> ***NOTE:*** the bot does not have any `adminstration` / `managing` / `moving` /  etc.. permissions. though I  recommend always to take a look at allowed permissions in <br> [`beta-bot invite link`](https://discord.com/api/oauth2/authorize?client_id=1117540489365827594&permissions=69241357196993&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Foauth2%2Fauthorize%3F%26client_id%3D1117540489365827594%26scope%3Dbot&response_type=code&scope=identify%20guilds%20gdm.join%20rpc.voice.read%20rpc.video.write%20rpc.activities.write%20messages.read%20applications.commands%20activities.read%20voice%20applications.commands.permissions.update%20dm_channels.read%20activities.write%20applications.store.update%20applications.builds.upload%20bot%20rpc.screenshare.read%20rpc.voice.write%20rpc%20guilds.join%20email%20role_connections.write%20relationships.read%20applications.entitlements%20applications.builds.read%20webhook.incoming%20rpc.screenshare.write%20rpc.video.read%20rpc.notifications.read%20guilds.members.read%20connections). feel free to sneak peak at our soucre code for any future changing of these intents/permissions💙 </sub>


</br>
</br>


> ##  🛠 TODO :
#### ⚠️ Do This BEFORE any New Features  &rarr;  *MIGRATE TO PYCORD!*

*   Documentation for functions / classes repo. first readme.md draft
  
*   implement new bard feature _i.e.( upload image and ask about it )_ in your bot since it's now available and [Bard API wrapper v0.1.27](https://github.com/dsdanielpark/Bard-API/releases/tag/0.1.27) now also  supports it
  
    
*   send Embeds fragmented in parts/pages if it exceeds max size  (6000char) or exceeds max fields (25 field)  <sub>note: use pagination </sub>

*   show embedded images in bard answer (seperate images in links -> append them to an image section 'embed or normal message' -> show the images!)

*   wizard bot sqlite-DB  design and connect the DB with bot code
  
*   Implement `Competitive Programming` Features on Bot and [Narol's Island](https://discord.com/invite/Y23B7R3FPq) server  <sub>( more in  M O D S channels in the server)</sub>

*   OOP it!  and handle errors!

*   save last conversation ID (load it in init_bot.py) in text file and add command to start new conv. and set default  to continue old one.

*   complete [`bard_key_refresh.py`](./bard_key_refresh.py)

*   add `TTS` feature : read text in audio + ability for bot to join voice chats

*   ADD `STT`  feature to enable full voice chat feature between bot and island server's users ( make bot make real voice chat with members)

* use [`Rapidapi`](https://rapidapi.com)

* complete your [`quote`](https://github.com/orsnaro/quote-async) lib fork and make it fully async.

*   add and test poe-API (starred at my GitHub)
     - _NOTE:_ BARD API is the one used now due to connection and belling issues beteen GPT-API i.e.(openAI API) and my country (Egypt)

*   add command to switch between BARD mode and poe-GPT mode
  
*   ~use google translator API~
  
       *  _(NOT necessary  NEED any more! now bard speaks arabic and bard API python wrapper also supports that  just edit your internal prompt / appendings and formating to discord messages to have arabic variation)_
    
*   Edit your bard args. and prompt to send full arabic query to bard (Bard now has arabic lang suuport)


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



</br>
</br>
</br>




---
> ### [🧾 References ](./sources&refs.md)

  * **Active Branches lately:**  `main` and [`bot_pycordv2.5.1B`](https://github.com/orsnaro/Discord-Bot-Ai/tree/bot_pycordv2.5.1B)
