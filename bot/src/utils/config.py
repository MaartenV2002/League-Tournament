from configparser import ConfigParser
from pathlib import Path

from discord import Intents

class Config:
    def __init__(self):
        self.config = {}
        self.filepath = Path(__file__).resolve().parents[2] / '.env'
        self.load()

    def load(self):
        """Load the configuration from the .env file."""
        config = ConfigParser()
        config.read(self.filepath)
        self.config = {section: dict(config[section]) for section in config.sections()}
    
    def get(self, section, key):
        """Get a value from the configuration."""
        if section not in self.config:
            raise KeyError(f'Section {section} not found in configuration')
        if key not in self.config[section]:
            raise KeyError(f'Key {key} not found in section {section}')
        return self.config[section][key]

    def get_intents(self):
        """Get the intents from the configuration and return a discord.Intents object."""
        if 'discord' not in self.config:
            raise KeyError(f'Section discord not found in configuration. Make sure to configure the environmental variables correctly.')
        intent_dict = {}
        for key in self.config['discord']:
            if key.startswith('intent_'):
                intent_name = key.split('intent_')[-1]
                intent_value = self.get('discord', key)
                intent_dict[intent_name] = bool(intent_value)
        return Intents(**intent_dict)
