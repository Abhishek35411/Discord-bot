import discord
import google.generativeai as genai


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:
            if self.user in message.mentions:
                channel= message.channel
                genai.configure(api_key="secret_key") 
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(f'{message.content}')
                messageToSend = response.text
                await channel.send(messageToSend)
        
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('token')
