import discord
from discord.ext import commands
import os
import time

client = commands.Bot(command_prefix="1O9YOdZN027K8P1dyLmQVUG8d7vFWlkLoS0VBVTZcK1u6J1xUEoojFQJRqpidkz9NVF589Rralq3JTus8tiz1ouhD3t1BgxFdkP6hCQ4oN5mptxjcV08pRjFcSyW73JGZNgxov80quCusQBiKuXHqtUafsHDpNIIe8zKFmRDwwkmrWtDFnUdqxqn2cq3IPXHHWWXZcV3")
client.remove_command('help')

@client.event
async def on_ready():
    while True:
        await update_server_count()
        await time.sleep(5)
        
async def get_server_count():
    all = 0
    online = 0
    for server in client.servers:
        for member in server.members:
            all += 1
            if str(member.status) != "offline":
                online += 1
    return all, online

async def  update_server_count():
    all, online = await get_server_count()
    await client.edit_channel(channel=client.get_channel('487367521679179787'), name="Server Members: " + str(all))
    await client.edit_channel(channel=client.get_channel('488235513430540310'), name="Online Members: " + str(online))

@client.event
async def on_member_join(member):
    await update_server_count()

@client.event
async def on_member_remove(member):
    await update_server_count()

client.run(os.getenv('TOKEN'))
