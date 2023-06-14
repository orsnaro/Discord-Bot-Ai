import asyncio as aio
from discord.ext import commands


for attr in dir(commands.HelpCommand):
      if  not (attr.startswith('__') or  attr.startswith('_')) :
         value = getattr(commands.HelpCommand, attr)
         print(f'    {attr}: {value}')
   

# async def fetchData():
#     # simulating time needed to connect fetch .. form server
#     print("fetching data...")
#     await aio.sleep(3)
#     print("data is fetched...")
#     return {"data" : 100}


# async def secCounter(): 
#     for i in range(10, 0, -1):  # start stop step (stop not with us)
#         await aio.sleep(2)
#         print(i)


# async def main():
#     task1ret = aio.create_task(fetchData() , name="task1fetchData")
#     task2ret = aio.create_task(secCounter())

# #.result() pause exec until task1 finish
#    #  await task1ret
#    #  print(task1ret.result())
   
#    #assigning return does not puase like result() does
#     task1out = await task1ret
#     print(task1out)
#     await task2ret
    


# aio.run(main())
