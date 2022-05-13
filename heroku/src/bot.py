import os
import nextcord

from config import BOT_STATUS, BOT

# Start bot
@BOT.event
async def on_ready():
    await BOT.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=BOT_STATUS)
    )
    print(f"{BOT.user} has started.")


BOT.run(os.environ["TOKEN"])
