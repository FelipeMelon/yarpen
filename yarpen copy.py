import discord
import os
import random
import string


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Elo'):
        await message.channel.send('Witam wielmożnego pana!')

    elif message.content.startswith('Witam'):
        await message.channel.send('Witaj! Zjedzmy coś i się napijmy!')            

    elif message.content.startswith('elo'):
        await message.channel.send('Witam wielmożnego pana!')

    elif message.content.startswith('.Zoltan jest lepszy od yarpena'):
        await message.channel.send('Odrąbię Ci ten głupi łeb toporem!')

    elif message.content.startswith('.Skąd macie mięsko?'):
        await message.channel.send('Samo przypełzło!')

    elif message.content.startswith('.Napijmy się!'):
        await message.channel.send(':beers:')

    elif message.content.startswith('.pieszgitarą'):
        await message.channel.send(file=discord.File('Pies.png'))

    elif message.content.startswith('.Bitka!'):
        await message.channel.send('Bitka? Gdzie?!')
        await message.channel.send(file=discord.File('Krasnolud.png'))

    elif message.content.startswith('.krzak'):
        await message.channel.send('Proszę bardzo:')

        listaObrazkow = ['krzak1.png', 'krzak2.png', 'krzak3.png', 'krzak4.png', 'krzak5.png', 'krzak6.png', 'krzak7.png', 'krzak8.png', 'krzak9.png', 'krzak10.png', 'krzak11.png', 'krzak12.png', 'krzak13.png', 'krzak14.png', 'krzak15.png' ]

        await message.channel.send(file=discord.File(random.choice(listaObrazkow)))



client.run('token')
