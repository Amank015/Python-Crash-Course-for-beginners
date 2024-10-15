#create a class
class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} '
    def has_birthday(self):
        self.age += 1
           
        
#Init use object
brad = User('Brad Traversy',"brad@gmail.com",37)
brad.has_birthday()
print(brad.greeting())


class Customer(User):
    def __init__(self,name,email,age):
        self.name  = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self,balance):
        self.balance = balance
   

# Init a customer object
janet = Customer('Janet Johnson',"Janet695@gmail.com",41)

janet.set_balance(500)        
print(janet.greeting())         