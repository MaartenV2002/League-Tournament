import discord

from utils.config import Config


def main():
    config = Config()
    token = config.get('discord', 'token')
    intents = config.get_intents()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is connected to the following servers:')
        for server in client.guilds:
            print(f'    - {server.name} (id: {server.id})')

    client.run(token)

if __name__ == "__main__":
    main()