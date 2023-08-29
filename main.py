import discord
import os
import time
from discord.ext import commands

#Variables

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)
embedclr = 	800080

#Rich Presence

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name='Enter Status Here'))
	print('Logging as {0.user}'.format(client))
	try:
		synced = await client.tree.sync()
		print(f"sycned {len(synced)} command(s)")
	except exception as e:
		print(e)

#Trip Command

@client.tree.command(name="trip", description="[short description of the trip]")
@commands.has_permissions(administrator = True)
async def summercamp(interaction: discord.Interaction):
	embed = discord.Embed(title="[TRIP NAME]", description="Here are a details about [trip name]", color=embedclr, url= "[INSERT DISCORD EVENT URL HERE]")
	embed.set_footer(text="embed footer text enter here")
	embed.set_image(url="enter image url here")
	embed.add_field(name="[Subheading]", value="[info relating to subheading]", inline=False)
	#COPY + PASTE embed.add_field section per section needed.
	await interaction.response.send_message(embed=embed)


token = os.environ['token']
client.run(token)