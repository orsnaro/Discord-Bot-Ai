# belongs to : https://pypi.org/project/pyrandmeme/#files

import aiohttp
import discord
import random2


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
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Palestine/new.json?sort=hot') as r:
            res = await r.json()
            sz = len(res['data']['children'])
            rand_post_no = random2.randint(0,sz - 1)
            
            #TESTING BLOCK
            has_crosspost_parent_list: bool = True if "crosspost_parent_list" in res['data']['children'][rand_post_no]['data']  else False
            print(f"\n\n\n\n\n TESTING########### \n\n\n invoked palestina_free(): reddit palestine list size : {sz} \n\n\n #########\n")
            print(res['data']['children'][rand_post_no]['data'])
            print(has_crosspost_parent_list)
            #TESTING BLOCK
            
            chosen_post_url = res['data']['children'][rand_post_no]['data']['url']
            chosen_post_text = res['data']['children'][rand_post_no]['data']['title']
            
            #this key in the json appears when it's a video but marked spoiler (to my knowledge) and outer 'is_video' key will show false which is wrong! there is a video!
            has_crosspost_parent_list: bool = True if "crosspost_parent_list" in res['data']['children'][rand_post_no]['data'] else False
            is_video = res['data']['children'][rand_post_no]['data']['is_video'] 
            
            if not is_video and not has_crosspost_parent_list:

               free_palestina = discord.Embed(title= _title , description= chosen_post_text, color=0xff2a2a)
               free_palestina.set_image(url= chosen_post_url )
               
            elif has_crosspost_parent_list:
               is_crossparent_video = res['data']['children'][rand_post_no]['data']['crosspost_parent_list'][0]['is_video']
               if is_crossparent_video :
                  is_video = is_crossparent_video
                  chosen_post_video = None if res['data']['children'][rand_post_no]['data']["crosspost_parent_list"][0]['media']["reddit_video"]["fallback_url"] is None else res['data']['children'][rand_post_no]['data']["crosspost_parent_list"][0]['media']["reddit_video"]["fallback_url"]
                  chosen_post_url = '||' + chosen_post_url + '||' if chosen_post_video is None else '||'+ chosen_post_video + '||'
               else:
                  free_palestina = discord.Embed(title= _title , description= chosen_post_text, color=0xff2a2a)
                  free_palestina.set_image(url= chosen_post_url)
            else: 
               chosen_post_video = None if res['data']['children'][rand_post_no]['data']['media']['reddit_video']['fallback_url'] is None else res['data']['children'][rand_post_no]['data']['media']["reddit_video"]["fallback_url"]
               chosen_post_url = chosen_post_url if chosen_post_video is None else chosen_post_video
               free_palestina = chosen_post_text
            
            return is_video , free_palestina, chosen_post_url