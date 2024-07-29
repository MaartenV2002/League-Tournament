import logging

from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member

from utils.config import Config
from src.bot_functions.set_initial_data import set_player_username, set_player_role, create_new_player

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DiscordBot:
    def __init__(self):
        self.config = Config()
        self.token = self.config.get('discord', 'token')
        self.prefix = self.config.get('discord', 'prefix')
        self.intents = self.config.get_intents()
        self.bot = commands.Bot(command_prefix=self.prefix, intents=self.intents)
        self.setup_events()
        self.setup_commands()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            logger.info(f'{self.bot.user} is connected to Discord!')
            server_ifo = '\n    - '.join([f'{server.name} (id: {server.id})' for server in self.bot.guilds])
            logger.info(f'Connected to the following servers:\n    - {server_ifo}')
        
        @self.bot.event
        async def on_member_join(member: Member):
            create_new_player(member)
            # Possibly add a welcome message here
        
    def setup_commands(self):
        @self.bot.command(name='username')
        async def set_username(ctx: Context, arg: str):
            message = set_player_username(ctx, arg)
            return await ctx.send(message)
        
        @self.bot.command(name='role')
        async def set_role(ctx: Context, arg: str):
            message = set_player_role(ctx, arg)
            return await ctx.send(message)
    
    def run(self):
        self.bot.run(self.token)

if __name__ == '__main__':
    bot = DiscordBot()
    bot.run()