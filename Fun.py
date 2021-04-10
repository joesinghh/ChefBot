from discord.ext import commands
import discord
import random
from menu import slap_url, ban_url, emoji_choice, smile_url, laugh_url, emoji_choice1,drugs_url


class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.lmt = 3


    @commands.command(name="hello",help='say hello to your friends')
    async def hello(self,ctx,*,member:discord.Member = None):
        member = member or ctx.author
        hearts = ['👋','🙋‍♂️','😀']
        await ctx.send("Hello {0}  {1}\nHow are u doin' ".format(member.mention,random.choice(hearts)))

    @hello.error
    async def hello_error(self,ctx,error):
        if isinstance(error,commands.MemberNotFound):
            await ctx.send("Member not Found !!! Hello btw")
        else:
            await ctx.send("Something went crazy , i think it was your mind!!!")
    @commands.command(help="Slap the one who irritates you")
    async def slap(self,ctx,member : discord.Member = None ,* , reason=None):
        
        url = random.choice(slap_url)
        reason = "it seems to be a revenge " if reason==None else  reason
        if member==ctx.author:
            await ctx.send("You better go to Mental hospital🏥 Kiddo. You need some serious help 🆘")
        
        
        else:
            if member==None:
                member = "Everyone"
                description="`c!slap <member_name> `"
            else:
                member = member.name
                description = reason

            embed = discord.Embed(title='{} slaped {}'.format(ctx.author.name,member),color = random.randint(0,0xffffff),
            description=description+str(member))
            embed.set_image(url = url)
            embed.set_footer(text = "{}".format(ctx.author.name),icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @slap.error
    async def slap_error(self,ctx,error):
        
        if isinstance(error,commands.MemberNotFound):
            print(error)
            await ctx.send("Member not found {} or you tried slapping a bot".format(random.choice(emoji_choice)))
    
    @commands.command(help='ban stupid people')
    async def ban(self,ctx,member:discord.Member = None,):

        url = random.choice(ban_url)
        if member==None:
            message = "Noob found!!! \nWhom you wanna ban kiddo , yourself ??\n`c!ban <member_name>`"


        else :
            message = "{} banned {} , hehe..😂".format(ctx.author.name,member.mention)
        
        embed = discord.Embed(title = "Ban!!",description=message,color = random.randint(0,0xffffff))
        embed.set_image(url=url)
        embed.set_footer(text = "{}".format(ctx.author.name),icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed) 
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MemberNotFound):
            print(error)
            await ctx.send("Member not found {}".format(random.choice(emoji_choice)))
    
    @commands.command(help='smile......')
    async def smile_at(self,ctx,member:discord.Member = None,):

        url = random.choice(smile_url)
        if member==None:
            message = "Hmm... on one is smiling, use this command wisely."


        else :
            message = "Lool at that lovely smile {} ".format(member.mention)
        
        embed = discord.Embed(title = " 😊",description=message,color = random.randint(0,0xffffff))
        embed.set_image(url=url)
        embed.set_footer(text = "{}".format(ctx.author.name),icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

    @smile_at.error
    async def smile_at_error(self,ctx, error):
        if isinstance(error, commands.MemberNotFound):
            print(error)

            await ctx.send("Member not found {}".format(random.choice(emoji_choice)))

        
    @commands.command(help='Gift someone Drugs')
    async def drugs(ctx, member :discord.Member = None,):
        url = random.choice(drugs_url)
        if member==None:
            message = "Stop Doing drugs Mr. {}".format(ctx.author.mention)


        else :
            message = "{} {} ".format(member.mention,random.choice(["Drugs are not good for health"," got caught taking drugs, what a noob."]))
        
        embed = discord.Embed(title = "Drugz....",description=message,color = random.randint(0,0xffffff))
        embed.set_image(url=url)
        embed.set_footer(text = "{}".format(ctx.author.name),icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)
    
    @drugs.error
    async def drugs_error(self,ctx,error):
        if isinstance(error,commands.MemberNotFound):
            await ctx.send("Are you high or what {} ? {}".format(random.choice(emoji_choice1).ctx.author.mention))


def setup(bot):
    bot.add_cog(Fun(bot))