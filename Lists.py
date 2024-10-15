#create a list
numbers = [1,2,5,3,8,]
fruits = ['apple','mango','orange','grapes','pears','banana']
#Use a constructor
'''
numbers2 = list((1,2,4,7))
print(numbers,numbers2)'''

print(fruits)

# get the value
print(fruits[1])

# Get the length
print(len(fruits))

#Append the list
fruits.append("guvava")

print(fruits)

#Remove from list
fruits.remove('pears')
print(fruits)

#Insert into position
fruits.insert(2,"pears")
print(fruits)

#Remove with pop
fruits.pop()
fruits.sort()
print(fruits)

#change the value
fruits[0] = 'bluebarries'