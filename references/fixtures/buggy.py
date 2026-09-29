def find_user(users, name):
    for u in users:
        if u["name"] == name:
            return u
    return None


def notify(user):
    print(f"Sending email to {user['email']}")


users = [{"name": "alice", "email": "a@x.com"}, {"name": "bob", "email": "b@x.com"}]
notify(find_user(users, "carol"))
