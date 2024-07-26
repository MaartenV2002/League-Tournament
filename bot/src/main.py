import logging

from discord.ext import commands

from utils.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    config = Config()
    token = config.get('discord', 'token')
    prefix = config.get('discord', 'prefix')
    intents = config.get_intents()
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f'{bot.user} is connected to Discord!')
        server_ifo = '\n    - '.join([f'{server.name} (id: {server.id})' for server in bot.guilds])
        logger.info(f'Connected to the following servers:\n    - {server_ifo}')

    @bot.command(name='ping')
    async def ping(ctx):
        await ctx.send('Pong!')

    bot.run(token)

if __name__ == "__main__":
    main()