CREATE TABLE IF NOT EXISTS players (
	id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    discord_id BIGINT NOT NULL UNIQUE,
    discord_name TEXT NOT NULL,
    summoner_name TEXT UNIQUE,
    role roles,
    riot_puuid VARCHAR UNIQUE
);