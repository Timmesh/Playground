def authenticate(func):
    def wrapper(user):
        if user.is_authenticated:
            return func(user)
        else:
            return "Access Denied"
    return wrapper

@authenticate
def view_dashboard(user):
    return "Welcome to the dashboard!"

# Simulate an authenticated user
class User:
    def __init__(self, is_authenticated=True):
        self.is_authenticated = is_authenticated

user = User(is_authenticated=True)
print(view_dashboard(user))
# Output: Welcome to the dashboard!

user = User(is_authenticated=False)
print(view_dashboard(user))
# Output: Access Denied
