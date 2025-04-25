import  keys
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=keys.openaiAPI_KEY, base_url="https://api.deepseek.com", organization= keys.openaiAPI_ORG_ID
)


async def main() -> None:
   stream = await client.chat.completions.create(
   model="deepseek-chat",
   messages=[
        {"role": "system", "content": "You are a helpful assistant"},
       {"role": "user", "content": "what was my last question"}
    ],
   stream=True
   )
   async for part in stream:
    print(part.choices[0].delta.content or "")


asyncio.run(main())