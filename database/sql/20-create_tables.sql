CREATE TABLE IF NOT EXISTS players (
	id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    summoner_name TEXT NOT NULL UNIQUE,
    role roles NOT NULL
);