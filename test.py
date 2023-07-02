from quote import quote
from random_word import RandomWords

res = None
	
while res is None and len(res[0]['quote']) <= 200 :
	random_word = RandomWords()
	category = random_word.get_random_word()
	res = quote(category , limit=1)
  
quotes = " "
for i in range(len(res)): # loop if there is multiple quotes e.g.(limit > 1)
	quotes : str = f"{res[i]['quote']} -GPTeous A. Wise Spirit;"
 
print (quotes)