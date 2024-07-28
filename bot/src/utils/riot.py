import requests

from src.utils.config import Config

class Riot:

    def __init__(self):
        self.config = Config()
        self.api_key = self.config.get('riot', 'api_key')
        self.base_url = 'https://europe.api.riotgames.com'
        self.account_url = '/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'

    def account_exists(self, game_name: str, tag_line: str) -> int | None:
        """
        Check if an account exists for the given game name and tag line.
        If the account exists, return the account puuid.
        If the account does not exist, return None. 
        """
        url = self.base_url + self.account_url.format(game_name=game_name, tag_line=tag_line)
        params = {
            'api_key': self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()['puuid']
        elif response.status_code == 404:
            return None
        response.raise_for_status()
