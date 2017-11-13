DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;

CREATE TABLE Artists (
	id INTEGER PRIMARY KEY,
	name TEXT
);

CREATE TABLE Albums (
	id INTEGER PRIMARY KEY,
    name TEXT,
    artistID INTEGER
);

CREATE TABLE Songs (
	id INTEGER PRIMARY KEY,
    name TEXT,
    albumID INTEGER,
    trackNumber INTEGER,
    duration INTEGER
);