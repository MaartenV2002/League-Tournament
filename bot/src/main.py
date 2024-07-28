import logging

from discord.ext import commands

from utils.config import Config
from database.types import Role
from database.models import Player
from database.helpers import create_db_session

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

    @bot.command(name='create-player')
    async def create_player(ctx, summoner_name: str, role: str):
        if role not in Role.__members__:
            return await ctx.send(f'Invalid role {role}. Valid roles are {", ".join(Role.__members__)}')
        new_player = Player(
            summoner_name=summoner_name,
            role=Role[role].value
        )
        with create_db_session() as session, session.begin():
            session.add(new_player)
            session.commit()
            session.close()
            return await ctx.send(f'Created player with name {summoner_name} and role {role}')

    bot.run(token)

if __name__ == "__main__":
    main()