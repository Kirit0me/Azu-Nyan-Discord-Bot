import discord
import os
import random
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands
from discord import app_commands
from typing import Optional
import jthon

load_dotenv()
guildmugi = discord.Object(id = 1077593727540936766)
token = os.getenv('TOKEN')

azu = jthon.load("azu", [])

def run_discord_bot():
    class MyClient(discord.Client):
        def __init__(self, *, intents: discord.Intents):
            super().__init__(intents=intents)
            # A CommandTree is a special type that holds all the application command
            # state required to make it work. This is a separate class because it
            # allows all the extra state to be opt-in.
            # Whenever you want to work with application commands, your tree is used
            # to store and work with them.
            # Note: When using commands.Bot instead of discord.Client, the bot will
            # maintain its own tree instead.
            self.tree = app_commands.CommandTree(self)
        async def setup_hook(self):
            # This copies the global commands over to your guild.
            self.tree.copy_global_to(guild=guildmugi)
            await self.tree.sync(guild=guildmugi)

    
    intents = discord.Intents.all()
    client = MyClient(intents=intents)
    async def nyanify(member):
            if not member.bot:
                if member.id not in azu.data:
                    azu.append.append(member.id)
                    azu.save()
                await member.edit(azu = f"{member.name}-Nyan")      

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == guildmugi:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    @client.event
    async def on_member_join(member):
        await nyanify(member)
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, Sup Incel.')
    
    @client.event
    async def on_user_update(before, after):

        if before.name != after.name:
            guild = client.get_guild(guild)
            member = guild.get_member(after.id)
            await nyanify(member)       

    @client.event
    async def on_message(message):
        username = str(message.author).split("#")[0]
        channel = str(message.channel.name)
        user_message = str(message.content)

        print(f'Message {user_message} by {username} on {channel}')

        if message.author == client.user:
            return

        if channel == "general":
            if user_message.lower() == "hello" or user_message.lower() == "hi":
                await message.channel.send(f'Hello {username}')
                return
            elif user_message.lower() == "bye":
                await message.channel.send(f'Bye {username}')
            elif user_message.lower() == "recommend me an anime":
                animes = ["K-ON!\nU got lucky getting this one :)", 
                          "Nodame Cantabille\nPiano at its finest",
                          "Battle Programmer Shirase\nBlack Hats at their finest",
                          "Trinity Seven\nHarem at its finest",
                          "Shirobako\nAnime Industry at its finest",
                          "New Game\nGame Industry at its finest",
                          "Koe de Oshigoto\nVoice acting at its finest",
                          "Yuyushiki\nSOL at its finest"]
                await message.channel.send(random.choice(animes))
    
    @client.tree.command()
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f'Hi, {interaction.user.mention}')

    @client.tree.command(name = "math-nyan")
    @app_commands.describe(
        first_value='Number of cats you want to breed',
        second_value='Amount of nyans per cat',
    )
    async def cats(interaction: discord.Interaction, first_value: int, second_value: int):
        await interaction.response.send_message(f'{first_value} nyan {second_value} = {(first_value + second_value)*(first_value-second_value)}')

    @client.tree.command(name = "azunyan")
    async def azubed(interaction: discord.Interaction):
        azubed = discord.Embed(title = "Azu-Nyan Appreciation", 
                               url = "https://k-on.fandom.com/wiki/Azusa_Nakano", 
                               description = "I like Azu-Nyan so you should too.",
                               color = 0x40008b,
                               )
        azubed.set_author( name = "Kiri-Nyan", icon_url= "https://th.bing.com/th/id/OIP.sBJGJuVGCIeVxcHsvji2ugHaIF?pid=ImgDet&rs=1" )
        azubed.set_thumbnail(url="https://th.bing.com/th/id/OIP.M_1-6Io8gYvp4LMANvWpawHaEK?pid=ImgDet&rs=1")
        azubed.add_field(name="What is K-ON!", value = "Kyo-Ani show which focusses on highschool girls being good at instruments and having fun because music = fun", inline = True)
        azubed.add_field(name="Why is K-ON!", value = "Because it is.", inline = False)
        azubed.add_field(name="When is K-ON!", value = "Apr-3-2009", inline = True)
        azubed.add_field(name="How is K-ON!", value = "10/10", inline = True)
        azubed.set_image(url= "https://th.bing.com/th/id/R.f3a66686664c1b3ff396ba9ef0b8f35b?rik=ejoCyEpv7zHdfA&riu=http%3a%2f%2fimages5.fanpop.com%2fimage%2fphotos%2f25000000%2fazunyan-wallpaper-nakano-azusa-25033054-1920-1080.jpg&ehk=YfgG84MSIjw0ECdmSshRrJPTt%2bvRytn%2fg5weM0FOhKg%3d&risl=&pid=ImgRaw&r=0")
        #azubed.footer(text = "K-ON! is good and is better than all music animes combined. But Azunyan is better :)")
        await interaction.response.send_message(embed=azubed)

    @client.tree.command(name = "nijika-life")
    async def nijika(interaction: discord.Interaction):
        nijibed = discord.Embed(title= "Nijika Appreciation",
                                url = "https://bocchi-the-rock.fandom.com/wiki/Nijika_Ijichi",
                                description="I like Nijika so you should too",
                                color = 0xf0e68c,
                                )
        nijibed.set_author( name = "Kiri-Nyan", icon_url= "https://th.bing.com/th/id/OIP.sBJGJuVGCIeVxcHsvji2ugHaIF?pid=ImgDet&rs=1" )
        nijibed.set_thumbnail(url = "https://animecorner.me/wp-content/uploads/2022/10/FfSSByFVsAUKquX.jpeg")
        nijibed.add_field(name = "Who is Nijika?", value = "For the blind, she is vision. For the hungry, she is the chef. For the thirsty, she is water. If Nijika thinks, I agree. If Nijika speaks, I'm listening. If Nijika has a million fans, I am one of them. If Nijika has ten fans, I am one of them. If Nijika has only one fan, that is me. If Nijika has no fans, I no longer exist. If the whole world is against Nijika, I am against the whole world. I will love Nijika until my very last breath.")
        nijibed.set_image(url = "https://animecorner.me/wp-content/uploads/2022/09/bocchi-the-rock-nijika-ijichi-trailer.jpg")

        await interaction.response.send_message(embed = nijibed)

    @client.tree.command(name = "ryo-yamada")
    async def ryo(interaction: discord.Interaction):
        ryobed = discord.Embed(title= "Ryo Appreciation",
                                url = "https://bocchi-the-rock.fandom.com/wiki/Nijika_Ijichi",
                                description="I like Ryo so you should too",
                                color = 0xf0e68c,
                                )
        ryobed.set_author( name = "Kiri-Nyan", icon_url= "https://th.bing.com/th/id/OIP.sBJGJuVGCIeVxcHsvji2ugHaIF?pid=ImgDet&rs=1" )
        ryobed.set_thumbnail(url = "https://animecorner.me/wp-content/uploads/2022/09/bocchi-the-rock-ryo-yamada-trailer.jpg")
        ryobed.add_field(name = "Why is Ryo so important?", value = "Ryo is a fine lady and has great taste in music. She is unfathomably smart. The owner of this bot relates to her and so she is important. She also doesnt care about being an introvert.")
        ryobed.set_image(url = "https://i.ytimg.com/vi/R4nY5dtwW4U/hqdefault.jpg")

        await interaction.response.send_message(embed = ryobed)
    
    @client.tree.command(name = "mugi-ojo")
    async def mugi(interaction: discord.Interaction):
        mugibed = discord.Embed(title= "Mugi Appreciation",
                                url = "",
                                description="I like Mugi so you should too",
                                color = 0xf0e68c,
                                )
        mugibed.set_author( name = "Kiri-Nyan", icon_url= "https://th.bing.com/th/id/OIP.sBJGJuVGCIeVxcHsvji2ugHaIF?pid=ImgDet&rs=1" )
        mugibed.set_thumbnail(url = "https://th.bing.com/th/id/OIP.NGYYz61z5CTy3EihveCwMgHaH7?pid=ImgDet&rs=1")
        mugibed.add_field(name = "What is Mugi?", value = "She is the owner of this bot's princess. No one is allowed to steel her from him. She is sassy and she is swag. She is cute and angelic and she plays the piano")
        mugibed.set_image(url = "https://th.bing.com/th/id/R.05095b5250d96fcd5064729a064552e0?rik=3tjYwCPVR7TstA&riu=http%3a%2f%2fimages4.fanpop.com%2fimage%2fphotos%2f14800000%2fmugi-k-on-14849554-1050-700.jpg&ehk=Zzu0x4KQw29qQrVIqVAnvMPI5KH28HLKgo%2f6KmPEkbs%3d&risl=&pid=ImgRaw&r=0")

        await interaction.response.send_message(embed = mugibed)

    @client.tree.command()
    @app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
    async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
        # If no member is explicitly provided then we use the command user here
        member = member or interaction.user
        await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

    @client.tree.context_menu(name='Show Join Date')
    async def show_join_date(interaction: discord.Interaction, member: discord.Member):
        # The format_dt function formats the date time into a human readable representation in the official client
        await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')

    '''@client.tree.context_menu(name='Report to Moderators')
    async def report_message(interaction: discord.Interaction, message: discord.Message):
        # We're sending this response message with ephemeral=True, so only the command executor can see it
        await interaction.response.send_message(
            f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
        )

        # Handle report by sending it into a log channel
        log_channel = interaction.guild.get_channel(1077875522375270420)  # replace with your channel id

        embed = discord.Embed(title='Reported Message')
        if message.content:
            embed.description = message.content

        embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
        embed.timestamp = message.created_at

        url_view = discord.ui.View()
        url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

        await log_channel.send(embed=embed, view=url_view)'''
        
    client.run(token)

