class User:
    def __init__(self,name,is_logged_in=False):
        self.name = name


def mydecorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function()
    return wrapper

@mydecorator
def create_blog_post(user):
    print(f"this is {user.name} logged i    n")

new_user = User("shaheen")
new_user.is_logged_in = True
create_blog_post(new_user)