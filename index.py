import discord
from discord.ext import commands
import asyncio 
import requests
import random
import string


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
    response = requests.get('')
    if response.status_code == 200:  # Success
        data = response.json()
        meme = random.choice(data['data']['memes'])
        embed = discord.Embed(title=meme['name'], color=discord.Color.blue())
        embed.set_image(url=meme['url'])
        await ctx.send(embed=embed)
    else:
        await ctx.send('Could not retrieve a meme at this time.')



@bot.command()
async def text_to_image(ctx, *, text):
    response = requests.post(
        'https://api.deepai.org/api/text2img',
        data={
            'text': text,
        },
        headers={'df95b90c-089a-4388-93b6-3acc320498a7': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    if response.status_code == 200:  # Success
        data = response.json()
        embed = discord.Embed(color=discord.Color.blue())
        embed.set_image(url=data['output_url'])
        await ctx.send(embed=embed)
    else:
        await ctx.send('Could not generate an image at this time.')


@bot.command()
async def text_to_speech(ctx, *, text):
    response = requests.get(
        'http://api.voicerss.org/',
        params={
            'key': 'your_api_key',
            'hl': 'en-us',
            'src': text,
            'f': '44khz_16bit_stereo',
            'c': 'mp3'
        }
    )
    if response.status_code == 200:  # Success
        with open('speech.mp3', 'wb') as f:
            f.write(response.content)
        await ctx.send(file=discord.File('speech.mp3'))
    else:
        await ctx.send('Could not generate speech at this time.')
import secrets


@bot.tree.command(name="password", description="Generates a strong random password")
async def password(interaction: discord.Interaction):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(16))

    await interaction.response.send_message(f"Your strong password is: {password}", ephemeral=True)
    await bot.tree.sync()



bot.run("your_bot_token")