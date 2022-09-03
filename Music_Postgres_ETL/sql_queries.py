# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"

# CREATE TABLES
songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP, 
    user_id INTEGER,
    level VARCHAR, 
    song_id VARCHAR, 
    artist_id VARCHAR, 
    session_id INTEGER,
    location VARCHAR, 
    user_agent VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR, 
    last_name VARCHAR,
    gender VARCHAR, 
    level VARCHAR
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY,
    title VARCHAR, 
    artist_id VARCHAR,
    year INTEGER, 
    duration FLOAT(5)
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY,
    name VARCHAR, 
    location VARCHAR,
    latitude FLOAT(5), 
    longitude FLOAT(5)
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour INTEGER, 
    day INTEGER,
    week INTEGER, 
    month INTEGER,
    year INTEGER,
    weekday VARCHAR
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT(songplay_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users (user_id,first_name,last_name,gender,level)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT(user_id) DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id,title,artist_id,year,duration)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id,name,location,latitude,longitude)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT(artist_id) DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time,hour,day,week,month,year,weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT(start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT ss.song_id, ss.artist_id FROM songs ss 
    JOIN artists ars on ss.artist_id = ars.artist_id
    WHERE ss.title = %s
    AND ars.name = %s
    AND ss.duration = %s
;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]