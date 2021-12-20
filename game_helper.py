import json


def create_pairs(users):
    if len(users) < 2:
        return []
    pairs = []
    first_user = users[0]
    users.append(first_user)
    for i in range(len(users) - 1):
        sender = users[i]
        receiver = users[i + 1]
        pair = (sender, receiver)
        pairs.append(pair)

    return pairs


def get_game_users(game_id):
    with open('users.json', 'r') as users_db:
        users = json.load(users_db)
        return [user for user in users['users'] if user['game_id'] == game_id]
