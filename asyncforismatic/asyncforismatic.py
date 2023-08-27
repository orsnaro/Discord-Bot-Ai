"""
# Forismatic ( async but deprecated from:  https://github.com/EgorBron/asyncforismatic)

## An unoficall library for getting quotes from the Forismatic API. Supports asynchronous syntax.


## Installing 

```bash
pip3 install asyncforismatic
```

Requires aiohttp and requests

## Examples 

```py
import asyncforismatic
import asyncio

# getting sync quote on russian as dict
print(asyncforismatic.quote(lang='ru', as_dict=True)) 

# getting async quote with default params (english language and formated quote)
async def example():
    return await asyncforismatic.async_quote()
print(asyncio.run(example()))
```

## Methods 

### Getting a quote (async) 

***corotinue*** `async_quote(lang='en', *, as_dict=False)`

* Returns an quote from Forismatic API

#### Parameters 

*as_dict*: `bool`

* If True, quote returns as JSON-like object (dict)

#### Raises exceptions 

`TypeError`

* The language is not passed as 'str'

`LangIsNotSupported`

* The language is not supported

**Returns** `Union[str, dict]`

### Getting a quote || Получение цитаты

***def*** `quote(lang='en', *, as_dict=False)`

* Returns an quote from Forismatic API

#### Parameters 
*as_dict*: `bool`

* If True, quote returns as JSON-like object (dict)

#### Raises exceptions 

`TypeError`

* The language is not passed as 'str'

`LangIsNotSupported`

* The language is not supported

**Returns** `Union[str, dict]`

## Exceptions || Исключения

`LangIsNotSupported`

* Raises when the language is not supported
"""
from typing import Union
import aiohttp, requests

class LangIsNotSupported(Exception):
	pass
async def async_quote(lang = 'en', *, as_dict = False) -> Union[str, dict]:
	"""
	corotinue `async_quote(lang='en', *, as_dict=False)`\n
	### Getting a quote (async) \n\n
		Returns an quote from Forismatic API\n
		#### Parameters 
		as_dict: `bool`\n
			```If True, quote returns as JSON-like object (dict)```\n
		#### Raises exceptions 
		`TypeError`\n
				The language is not passed as 'str'\n
		`LangIsNotSupported`\n
				The language is not supported\n
		Returns `Union[str, dict]`\n
		
	"""
	if not isinstance(lang, str):
		raise TypeError(f'You must use language as \'str\', not as {type(lang)}')
	if lang not in ['en', 'ru']:
		raise LangIsNotSupported('This language not in supported (english - en and russian - ru).')
	async with aiohttp.ClientSession() as requester:
		async with requester.get(url = f"http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang={lang}") as response:
			quote = await response.json()
			if as_dict: return quote
			author = '©'+quote["quoteAuthor"] if quote["quoteAuthor"] else ''
			return quote["quoteText"] , author 
