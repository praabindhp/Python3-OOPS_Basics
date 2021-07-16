# Super Keyword

class User:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show_user(self):
        print("The User : %s \nThe Age : %s" % (self.name, self.age))

    # Function Overriding
    
    def show_info(self):
        print("This Is A Child Method")

class FacebookUser(User):
    
    def __init__(self, name, age):
        # self.name = name
        # self.age = age
        super().__init__(name, age)

FB_User = FacebookUser('Praabindh Pradeep', 20)
FB_User.show_user()