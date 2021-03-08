import random, discord, os


#Variables
token = open('note_token_test', 'r').read()
client = discord.Client()


#Pick the card
@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content == '*help':
      await message.channel.send('''
      Prefix: *\n
      Website:\n
      Support: https://discord.gg/4sutReEVE8\n
      Creator: https://github.com/AlmirPaulo\n
      Vote for us: Soon...\n
      Premium: Soon...''')
    
    
    if message.content == '*1card':
      pick = random.randint(0,21)
      await message.channel.send( 'An advice.',file=discord.File(f"cards/{str(pick)}.png"))

    if message.content == '*3cards':
      cards = 3
      pick = []
      while cards > 0:
        pick.append(random.randint(0,21))
        cards = cards -1
        
      await message.channel.send('The Past, Present and Future.',files=[discord.File(f"cards/{str(pick[0])}.png"),
                                discord.File(f"cards/{str(pick[1])}.png"),
                                discord.File(f"cards/{str(pick[2])}.png")])  



    if message.content == '*2cards':
      cards = 2
      pick = []
      while cards > 0:
        pick.append(random.randint(0,21))
        cards = cards -1
        
      await message.channel.send('The Positive and Negative sides.',files=[discord.File(f"cards/{str(pick[0])}.png"),
                                discord.File(f"cards/{str(pick[1])}.png")])  

    if message.content.startswith('*card'):
      num = message.content[6:8]
      await message.channel.send(file=discord.File(f"cards/{num}.png"))


#Run the bot
#keep_alive.alive()
client.run(token.strip())