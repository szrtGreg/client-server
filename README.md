# Client-server app
Implementation of client-server. Use commands to comunicate with server
```python
{
	'info':     'show server version',
	'stop' :    'stops server',
	'help' :    'show all commands',
	'uptime':   'show server uptime',
	'send':     'send message to user',
	'delete':   'delete user',
	'create':   'create user'
}
```

# Prepare databse
To run you need to have database in postgres created. Now, create 2 tables and insert sample data
```sql
create table users (
 id SERIAL PRIMARY KEY,
 name varchar(20) NOT NULL,
 password varchar(20) NOT NULL,
 role varchar(6) NOT NULL
 );
 
 create table messages (
 id SERIAL PRIMARY KEY,
 sender varchar(20) NOT NULL,
 receiver varchar(20) NOT NULL,
 text varchar(255) NOT NULL
 );
 
 insert into users (name, password, role) values 
('greg','123456', 'ADMIN');

```
With this in place, create file **settings.ini** in root folder of your application
```ini
[postgresql]
host=<hostname>
database=<database>
user=<user>
password=<password>
port=5432
```



# Usage
To start this server you need just follow these commands.
```
For run app in first bash windnow
-> python server.py
In second bash
-> python client.py
```

# Screen
![obraz](https://user-images.githubusercontent.com/27915290/185364029-3d8407e9-7e31-4545-8333-0e7695671893.png)

