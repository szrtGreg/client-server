import json

users = {
    'greg1': {
        'role':'admin',
        'pass': 'ala',
        'messages': [1,2,3]
    },
    'greg2': {
        'role':'admin',
        'pass': 'ala2',
        'messages': []
    },
    'greg3': {
        'role':'admin',
        'pass': 'ala2',
        'messages': [1]
    }
}

#Read from file
""" with open('users_data.json') as json_file:
    users = json.load(json_file) """

    
#Create users
""" name = input('Podaj usera: ')
password = input('Podaj haslo: ')

users[name] = {'role': 'user', 'pass':password}  """





#Loging
""" print(users)

login, password = input('Podaj usera i haslo: ').split()

if login not in users:
    print('Nie ma takiego usera')
    exit()

if password != users[login]['pass']:
    print('zle haslo')
    exit()

for i in users[login].items():
    print(i)
 """



##Send messages
""" print(users)

login, *message = input('Podaj usera i haslo: ').split()

if message:
    message = ' '.join(message)

if login not in users:
    print('Nie ma takiego usera')
    exit()

number_of_messages = len(users[login]['messages'])
if number_of_messages > 5:
    print('Nie mozna wyslac wuiadomosci')
else:
    users[login]['messages'].append(message)
 """


#Save to a file
""" json_string = json.dumps(users)
with open('users_data.json', 'w') as outfile:
    outfile.write(json_string) """

""" with open('users_data.json', 'w') as outfile:
    json.dump(users, outfile) """



""" dupa = "1\n2\n3"
with open('users_data.json', 'w') as outfile:
    outfile.write(dupa)

with open('users_data.json', 'r') as outfile:
    print(outfile.readlines())
 """

