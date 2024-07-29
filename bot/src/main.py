import logging

from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member

from utils.config import Config
from src.bot_functions.set_initial_data import set_player_username, set_player_role, create_new_player

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


    @bot.event
    async def on_member_join(member: Member):
        create_new_player(member)
        # Possibly add a welcome message here


    @bot.event
    async def on_member_remove(member: Member):
        print(f'{member} has left the server!')


    @bot.command(name='username')
    async def set_username(ctx: Context, arg: str):
        message = set_player_username(ctx, arg)
        return await ctx.send(message)


    @bot.command(name='role')
    async def set_role(ctx: Context, arg: str):
        message = set_player_role(ctx, arg)
        return await ctx.send(message)


    @bot.command(name='ping')
    async def ping(ctx):
        await ctx.send('Pong!')


    bot.run(token)

if __name__ == "__main__":
    main()