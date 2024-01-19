import keys
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=keys.openaiAPI_KEY, organization= keys.openaiAPI_ORG_ID
)


async def main() -> None:
   stream = await client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[{"role": "user", "content": "what was my last questio"}],
   stream=True
   )
   async for part in stream:
    print(part.choices[0].delta.content or "")


asyncio.run(main())