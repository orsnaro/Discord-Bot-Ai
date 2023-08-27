"""
# Forismatic

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

### Getting a quote 

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
**Возвращает** `Union[str, dict]`

## Exceptions 

`LangIsNotSupported`

* Raises when the language is not supported
"""



from .asyncforismatic import LangIsNotSupported, async_quote
from . import example

__author__ = 'EgorBron'
__version__ = '0.0.1'
__mail__ = 'bataikinegor@yandex.ru'