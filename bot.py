import discord
from discord.ext import commands
import os
import format

bot = commands.Bot(command_prefix='Hello Friend')
bot.remove_command('help') # remove that help command

async def get_server_count():
    all=online=robot=0  # set vars to zero
    for member in bot.get_all_members():
        all += 1
        if member.status != discord.Status.offline:
            online += 1
        if member.bot:
            robot += 1

    return all,online,robot

async def update_count(count):
    all, online, robot = count
    
    ch_all = bot.get_channel('489143518716100629')
    name_all = await format.convert_string('Total : ') + str(all)

    ch_online = bot.get_channel('489146748720119818')
    name_online = await format.convert_string('Online : ') + str(online-robot)

    ch_robot = bot.get_channel('489146790482935808')
    name_robot = await format.convert_string('Bots : ') + str(robot)

    await bot.edit_channel(channel=ch_all, name=name_all)
    await bot.edit_channel(channel=ch_online, name=name_online)
    await bot.edit_channel(channel=ch_robot, name=name_robot)

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
