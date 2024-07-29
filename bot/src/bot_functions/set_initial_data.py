from discord.member import Member
from discord.ext.commands.context import Context
from requests.exceptions import HTTPError

from src.database.types import Role
from src.database.helpers import create_db_session, get_player_from_discord_id
from src.database.models import Player
from src.utils.riot import Riot

def validate_role(role: str) -> tuple[bool, str]:
    if role.upper() not in Role.__members__:
        valid_roles = ', '.join(role.lower() for role in Role.__members__)
        return False, f'Invalid role {role}. Valid roles are {valid_roles}'
    return True, ''

def create_new_player(member: Member) -> None:
    with create_db_session() as session, session.begin():
        new_player = Player(
            discord_id=member.id,
            discord_name=member.name
        )
        session.add(new_player)
        session.commit()
    return

def check_summoner_name(summoner_name: str) -> tuple[bool, str]:
    riot = Riot()
    name = summoner_name.split('#')[0]
    tag = summoner_name.split('#')[1]
    try:
        puuid = riot.account_exists(name, tag)
    except HTTPError:
        return False, "Something went wrong, please try again later"
    if not puuid:
        return False, "This summoner name does not exist on the EUW server"
    return True, puuid


def set_player_username(ctx: Context, username: str) -> str:
    with create_db_session() as session, session.begin():
        player = get_player_from_discord_id(session, ctx.message.author.id)
        if not player:
            return "Something went wrong, please contact the admin"
        exists, puuid = check_summoner_name(username)
        if not exists:
            return puuid
        player.summoner_name = username
        player.riot_puuid = puuid
        session.commit()
    return "Your username has been set successfully"


def set_player_role(ctx: Context, role: str) -> str:
    with create_db_session() as session, session.begin():
        player = get_player_from_discord_id(session, ctx.author.id)
        if not player:
            return "Something went wrong, please contact the admin"
        succes, message = validate_role(role)
        if not succes:
            return message
        player.role = Role[role.upper()].value
        session.commit()
    return "Your role has been set successfully"
