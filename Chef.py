from discord.ext import commands
import discord
import random
import requests
from menu import menu,fooditems

class MainChef(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(name='chef',invoke_without_command=True)
    async def chef(self,ctx,*,Content = []):
        if len(Content)==0:
            await ctx.send("YOLO Noob 🤓")


    @chef.command
    async def meme(ctx):
        pass



    @chef.command
    async def foodfor(ctx):
        pass
    

    @chef.command
    async def kick(ctx,member : discord.member=None,):
        pass


        
        

def setup(bot):
    bot.add_cog(MainChef(bot))
    