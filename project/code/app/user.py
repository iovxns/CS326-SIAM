def register(username, password):
    if username == "" or password == "":
        return False
    return True


def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

def update_profile(name):
    if len(name) < 2:
        return False
    return True