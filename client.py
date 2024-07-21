from info import *
from pyrogram import Client

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "Post-Search-Bot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    async def start(self):                        
        await super().start()  
        print("Bot Started 🔧")   
    async def stop(self, *args):
        await super().stop()
