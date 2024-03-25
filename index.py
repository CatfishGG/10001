import discord
from discord.ext import commands
import asyncio 
import requests


intents = discord.Intents.all()
bot = discord.Client(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("The bot is online")
    

    @bot.event
    async def on_member_join(member):
        channel_id = 1234567890  # Replace with the actual channel ID
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(f"Welcome {member.mention} to the server!")

            @bot.event
            async def on_member_remove(member):
                channel_id = 1234567890  # Replace with the actual channel ID
                channel = bot.get_channel(channel_id)
                if channel:
                    await channel.send(f"{member.mention} has left the server.")

                    @bot.command()
                    @commands.has_permissions(administrator=True)
                    async def timeout(ctx, member: discord.Member, duration: int, *, reason: str):
                        role = discord.utils.get(ctx.guild.roles, name="Timeout")
                        if not role:
                            role = await ctx.guild.create_role(name="Timeout")
                            for channel in ctx.guild.channels:
                                await channel.set_permissions(role, send_messages=False)
                        await member.add_roles(role)
                        await ctx.send(f"{member.mention} has been timed out for {duration} seconds. Reason: {reason}")
                        await asyncio.sleep(duration)
                        await member.remove_roles(role)

                    @bot.command()
                    @commands.has_permissions(administrator=True)
                    async def untimeout(ctx, member: discord.Member):
                        role = discord.utils.get(ctx.guild.roles, name="Timeout")
                        if role in member.roles:
                            await member.remove_roles(role)
                            await ctx.send(f"{member.mention} has been untimed out.")

                    @bot.command()
                    @commands.has_permissions(administrator=True)
                    async def kick(ctx, member: discord.Member, *, reason: str):
                        await member.kick(reason=reason)
                        await ctx.send(f"{member.mention} has been kicked from the server. Reason: {reason}")

                    @bot.command()
                    @commands.has_permissions(administrator=True)
                    async def ban(ctx, member: discord.Member, *, reason: str):
                        await member.ban(reason=reason)
                        await ctx.send(f"{member.mention} has been banned from the server. Reason: {reason}")


@bot.command()
async def quote(ctx):
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:  # Success
        data = response.json()
        quote = f'"{data["content"]}" - {data["author"]}'
        await ctx.send(quote)
    else:
        await ctx.send('Could not retrieve a quote at this time.')



@bot.command()
async def meme(ctx):
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    if response.status_code == 200:  # Success
        data = response.json()
        embed = discord.Embed(title=data['title'], color=discord.Color.blue())
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)
    else:
        await ctx.send('Could not retrieve a meme at this time.')
    
bot.run("")
