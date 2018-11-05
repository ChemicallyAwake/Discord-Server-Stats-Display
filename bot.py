import discord
from discord.ext import commands
import os
import format

bot = commands.Bot(command_prefix='!@#$%^&*()')
bot.remove_command('help')

async def get_server_count():
    all=online=robot=0
    for member in bot.get_all_members():
        if member.bot:
            robot += 1
        else:
            all += 1
            if member.status != discord.Status.offline:
                online += 1 
        
    return all,online,robot

async def update_count(count):
    all, online, robot = count
    nameTotal, nameOnline, nameBots = "total","online","bots"
    
    if online == 314:
        online = "1"
    elif online == 404:
        nameOnline = "error"
        online = "not found"
    elif online == 666:
        nameTotal = "eɹror"
        all = 666
        nameOnline = "hail"
        online = "satan"
    elif online == 1024:
        online = "1kb"
    elif total == 9001:
        total = "over 9000"
        
    await bot.edit_channel(channel=bot.get_channel(os.getenv('TOTAL')),
                           name= await format.convert_string(nameTotal + ' : ') + str(all))
    await bot.edit_channel(channel=bot.get_channel(os.getenv('ONLINE')),
                           name=await format.convert_string(nameOnline + ' : ') + str(online))
    await bot.edit_channel(channel=bot.get_channel(os.getenv('BOTS')),
                           name=await format.convert_string(nameBots + ' : ') + str(robot))

@bot.event
async def on_member_join(member):
    await update_count(await get_server_count())

@bot.event
async def on_member_remove(member):
    await update_count(await get_server_count())

@bot.event
async def on_member_update(before, after):
    await update_count(await get_server_count())

@bot.event
async def on_ready():
    await update_count(await get_server_count())

bot.run(os.getenv('TOKEN'))
