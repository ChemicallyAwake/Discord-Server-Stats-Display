import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="1O9YOdZN027K8P1dyLmQVUG8d7vFWlkLoS0VBVTZcK1u6J1xUEoojFQJRqpidkz9NVF589Rralq3JTus8tiz1ouhD3t1BgxFdkP6hCQ4oN5mptxjcV08pRjFcSyW73JGZNgxov80quCusQBiKuXHqtUafsHDpNIIe8zKFmRDwwkmrWtDFnUdqxqn2cq3IPXHHWWXZcV3")
client.remove_command('help')

@client.event
async def on_ready():
    await update_server_count()

async def get_server_count():
    count = 0
    for server in client.servers:
        for member in server.members:
            count += 1
    return count

async def  update_server_count():
    count = "M󠀠󠀠embers_󠀠" + str(await get_server_count())
    await client.edit_channel(channel=client.get_channel('487361010207031299'), name=count)

@client.event
async def on_member_join(member):
    await update_server_count()

@client.event
async def on_member_remove(member):
    await update_server_count()

client.run(os.getenv('TOKEN'))
