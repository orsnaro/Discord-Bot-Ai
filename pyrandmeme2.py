# forked from to: https://pypi.org/project/pyrandmeme/#files

import aiohttp
import discord
import random2
from utils_bot import extract_post_info, prepare_special



async def pyrandmeme2( _title : str = "Random meme") -> discord.Embed :
    pymeme = discord.Embed(title= _title , description="gpteous finds this funny", color=0xe91e63)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            sz = len(res['data']['children'])
            
            #TESTING BLOCK
            print(f"\n\###########invoked pyrandmeme2.py: reddit memes list size : {sz}#########\n")
            #TESTING BLOCK
            
            pymeme.set_image(url=res['data']['children'][random2.randint(0,sz - 1)]['data']['url'])
            return pymeme
        await pyrandmeme2("Random meme")
        
        
        
        
async def palestina_free( _title : str = ":flag_ps: OPEN YOUR EYES & WATCH! :flag_ps:") -> discord.Embed : 
   #NOTE: for way simpler logic just make them all normal messages not embedded discord messages
   async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/Palestine/new.json?sort=hot') as r:
         
         
         res = await r.json()
         sz = len(res['data']['children'])
         
         rand_post_no, chosen_post_url, org_post, chosen_post_text, has_crosspost_parent_list, is_video = extract_post_info(res, sz)
         is_video, free_palestina_data, chosen_post_url = prepare_special(res,
                                                                                 rand_post_no,
                                                                                 special_type= 'ps',
                                                                                 chosen_post_url= chosen_post_url,
                                                                                 org_post= org_post,
                                                                                 chosen_post_text= chosen_post_text,
                                                                                 has_crosspost_parent_list= has_crosspost_parent_list,
                                                                                 is_video= is_video,
                                                                                 title= _title)
         
         return is_video, free_palestina_data, chosen_post_url