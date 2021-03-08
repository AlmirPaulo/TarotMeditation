
import random, discord


#Variables
token = open('note_token_test', 'r').read()
client = discord.Client()


#Pick the card
@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content == '*onecard':
      pick = random.randint(0,21)
      await message.channel.send( file=discord.File(f"cards/{str(pick)}.png"))

    if message.content == '*3cards':
      cards = 3
      pick = []
      while cards > 0:
        pick.append(random.randint(0,21))
        print(pick)
        cards = cards -1
        
      await message.channel.send(files=[discord.File(f"cards/{str(pick[0])}.png"),
                                discord.File(f"cards/{str(pick[1])}.png"),
                                discord.File(f"cards/{str(pick[2])}.png")])  



    if message.content == '*2cards':
      cards = 2
      pick = []
      while cards > 0:
        pick.append(random.randint(0,21))
        print(pick)
        cards = cards -1
        
      await message.channel.send(files=[discord.File(f"cards/{str(pick[0])}.png"),
                                discord.File(f"cards/{str(pick[1])}.png")])  




    if message.content.startswith('*card'):
      num = message.content[6:8]
      await message.channel.send(file=discord.File(f"cards/{num}.png"))


#Run the bot
client.run(token.strip())