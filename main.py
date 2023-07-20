import os

import asyncio
from audio.music import bot, MusicCommands
from dotenv import load_dotenv
load_dotenv()


async def main():
    if os.getenv('BOT_TOKEN'):
        async with bot:
            await bot.add_cog(MusicCommands(bot))
            await bot.start(os.getenv('BOT_TOKEN'))
    print('Bot token required!')

asyncio.run(main())
