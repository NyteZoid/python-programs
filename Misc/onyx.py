#start

import discord 

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, 
        activity=discord.Game(name="nytezoid for mod", type=3)
    )
    print("Bot Connected")

    channel = client.get_channel(851049451660247083)
    if channel is not None:
        message = await channel.send("Hey I am Onyx")
        await message.add_reaction("<:onyx:1395127851929305230>")
    else:
        print("Channel not found")

client.run('bot token')

#end

