# Roommate Stat Tracker

Real rough stuff

Meant to eventually run on a raspberry pi zero for remote stat tracking of stupid things we as roommates of the wonderful apartment [[REDACTED]] do on an everyday basis. More of a learning project than anything 

## Main table schema

SQLite3 used for a simple local database
`CREATE TABLE table_name (id integer primary key, name text, stat text, amount integer);`

## Dependencies

[Flask](https://palletsprojects.com/p/flask/) `pip install flask` easy peasy
