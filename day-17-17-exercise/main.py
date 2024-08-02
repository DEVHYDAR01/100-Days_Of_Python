class User:
    def __init__(self, userid, username):
        print("creating new user.......")
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follower(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "hydar")
user_2 = User("002", "nana")

user_1.follower(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




