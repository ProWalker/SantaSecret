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
