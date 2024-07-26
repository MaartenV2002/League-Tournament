import logging

import discord

from utils.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    config = Config()
    token = config.get('discord', 'token')
    intents = config.get_intents()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        logger.info(f'{client.user} is connected to Discord!')
        server_ifo = '\n    - '.join([f'{server.name} (id: {server.id})' for server in client.guilds])
        logger.info(f'Connected to the following servers:\n    - {server_ifo}')

    client.run(token)

if __name__ == "__main__":
    main()