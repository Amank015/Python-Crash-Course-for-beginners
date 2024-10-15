#create a dict

person = {
    'firstName':"aman",
    'lastName':"Khan",
    'age':30
}

#Use a constructor

person2 = dict(first_Name='Rehan',last_Name="khan")

print(person,person2)


#Get a value
print(person['firstName'])
print(person.get('lastName'))

#Add key/value
person['phone'] = "930-193-5288"
print(person)

#Get items key
print(person.keys())

#Gey dict items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = "Banmore"
print(person2)

#Remove items
del(person['age'])
person.pop('phone')
person.popitem()
print(person)


#clear
person.clear()

#Get the length
print(len(person))
print(len(person2))
#

# List of dict

people = [
    {'Name':"Arun",'age':23},
    {"Name":"Ayush",'age':22}
]
print(people[1]['Name'])