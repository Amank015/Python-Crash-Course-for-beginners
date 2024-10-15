car = ["Swift","Fortuner","BMW","RoyalRoyee","Marcedes"]


# using a constructor
name = list(["Aman","Rehan","Shohib","Aslam"])

print(car,name)


car.append("Thar")
car.sort()
car.remove("RoyalRoyee")
car.extend("BMW")  # Using to string into a separate character
name = car.copy()
print(name)
