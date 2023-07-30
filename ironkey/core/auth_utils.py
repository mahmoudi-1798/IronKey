
def require_authentication(func):
    def wrapper(self, *args, **kwargs):
        if self.auth():
            return func(self, *args, **kwargs)
        else:
            print("Authentication failed. Incorrect username or password.")
    return wrapper