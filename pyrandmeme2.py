# belongs to : https://pypi.org/project/pyrandmeme/#files

import aiohttp
import discord
import random2


async def pyrandmeme2( _title : str = "Random meme") -> discord.Embed :
    pymeme = discord.Embed(title= _title , description="gpteous finds this funny", color=0xe91e63)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            pymeme.set_image(url=res['data']['children'][random2.randint(0, 24)]['data']['url'])
            return pymeme
        await pyrandmeme2("Random meme")