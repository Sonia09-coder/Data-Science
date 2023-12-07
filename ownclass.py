#in PascalCase the first letter of all words is capitalized, in camelCase the first letter is small, snake_case as the syntax tells itself
class User:
    
    def __init__(self,user_id,username,followers):    #constructor is being created
        print("New user being created")
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
    
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User("000","Sonia",0)
# user_1.id="001"
# user_1.username="Sonia"

print(user_1.username)
print(user_1.id)
print(user_1.followers)

user_2=User("111","Angela",0)
# user_2.username="Angela"
# user_2.id="001"
print(user_2.username)
print(user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)