def get_token():
    TOKEN = open("/secrets/token", "r").read().split()[0]
    return TOKEN