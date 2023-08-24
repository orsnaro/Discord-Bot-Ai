# import asyncio as aio
# from bardapi import Bard

# #from cockie name : "__Secure-1PSID"
# api_coockie = "XQgoSOoCldBR7LdYjh8OAX1U1vfHU0cheOu89QFRKpkZu21qUw3RZXG75uGEYY4zCiBKVw."
# bard = Bard(token=api_coockie)

# def skip_line(full_ans):
#   lines = full_ans.split('\n')
#   return '\n'.join(lines[1:])


# async def ask_bard(user_query : str , user_name = "3cem" ):
#    bard_ans = bard.get_answer(f"act as a wizard named Gpteous living in master Narol's island. start and end of  answer  must be  in wizardish sentences  that also  has emojies like :fog: etc.. . the  rest must be using normal english. {user_name} question: {user_query}")
#    for key , val in bard_ans.items() :
#       print (f" {key} : {val}")
      
#    return skip_line(bard_ans['content']) # skip first line that has my prompt 


# async def main():
# 	ans = aio.create_task(ask_bard("explain quantum theory in simple words"))
# 	ans = await ans

# 	print (ans)	
 
# aio.run(main())
#----------------------------------------------------------------------#
#                     PRACTISE HTTP
# import requests
# import urllib
# # The API endpoint
# url = "https://jsonplaceholder.typicode.com/posts/"

# # Adding a payload
# payload = {"id": [1, 2, 3], "userId":1}

# # A get request to the API
# response = requests.get(url, params=payload)

# # Print the response
# response_json = response.json()

# for i in response_json:
#     print(i, "\n")