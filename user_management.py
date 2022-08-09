import json


def create_new_user(username, password, file):
    # Read from json users file --> Returns dict()
    with open(file) as json_file:
        users = json.load(json_file)
        
    users[username] = {'role': 'user', 'pass': password, 'messages': []}
    
    #Save file
    with open('users_data.json', 'w') as outfile:
        json.dump(users, outfile)


def login(username, password, file):
    # Read from users file
    with open(file) as json_file:
        users = json.load(json_file)

    if username not in users:
        return 'User does not exist'

    if password != users[username]['pass']:
        return 'Wrong password'
    
    return users[username]


def send(username, message, file):
    with open(file) as json_file:
        users = json.load(json_file)

    if username not in users:
        return 'User does not exist'

    if message:
        message = ' '.join(message)

    number_of_messages = len(users[username]['messages'])
    if number_of_messages >= 5:
        return 'Message can not be send'
    else:
        users[username]['messages'].append(message)
        
    #Save file
    with open(file, 'w') as outfile:
        json.dump(users, outfile)
    
    return 'Message was sent'
