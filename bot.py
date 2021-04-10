from discord.ext import commands
import discord
import random
import os
from pretty_help import PrettyHelp, Navigation
from menu import rules_

bot = commands.Bot(command_prefix=['c!','C!'],case_insensitive=True,help_command=PrettyHelp(active_time=3))

@bot.event
async def on_ready():
    await bot.change_presence( activity=discord.Game("& Cooking at CU"))


class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@bot.command(help='Check roles')
async def roles(ctx, *, member: MemberRoles=None):
	if member==None:
		await ctx.send('I see the following roles: ' + ', '.join(ctx.author))
	else:
	    await ctx.send('I see the following roles: ' + ', '.join(member))


@roles.error
async def roles_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("{} you have crossed the limit of stupidness.".format(ctx.author.mention))


@bot.command(help="Reload a Cog")
@commands.has_role("Admin")
async def reload(ctx, extension):
	if extension == '':
		await ctx.send("Please enter a valid Cog/Category.")
	try:
		bot.unload_extension(extension)
		bot.load_extension(extension)
		await ctx.send(f'Reloaded {extension}! 🔄')
	except Exception as error:
		await ctx.send(f'Failed to reload Cog {extension}. Reason: {error}')

@reload.error
async def reload_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("`c!reload <Cog_name>`\nThat's how you use this command Noob {}".format(ctx.author.mention))

extensions  = ['Chef','Fun']
for extension in extensions:
    bot.load_extension(extension)

@bot.command()
async def rules(ctx,number:int = None):
    embed = discord.Embed(title = "Rule Book",color = discord.Color.blue())
    embed.set_footer(text='follow the rules or die🔪')
    if number ==None:
        embed.description = "Some Rules for this server 🧾"
        for i,key in enumerate(rules_):
            embed.add_field(name= "Rule {}".format(i+1),value = "{:s}".format(key),inline=False)
	
    elif number in range(1,len(rules_)+1):
        embed.description = "`c!rules` for all rules"
        embed.add_field(name = "Rule {}".format(number),value = rules_[number-1],inline=False) 

    else:
        raise commands.MemberNotFound

    await ctx.send(embed = embed)

@rules.error
async def rules_error(ctx, error):
	if isinstance(error, commands.MemberNotFound):
		await ctx.send("Not a Valid Number")
		


bot.run('Nzc0ODkwODc1NjA3NzExNzc0.X6eXXQ.zl6ByL7daViAoqdckcg6gpVEtso')
