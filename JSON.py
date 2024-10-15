import json

# sample json

useJSON = '{"first_Name": "John", "last_Name": "Doe", "age" : "39", "Email":"john585@gmail.com"}' 

# Parse to dict
user = json.loads(useJSON)

print(user)
print(user['first_Name'])


car = {'make':'Ford','model':'Mustang','year':1970}

carJSON = json.dumps(car)

print(carJSON)