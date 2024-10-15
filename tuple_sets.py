#create a tuple 
fruit = ('apple,','mango','orange', 'grapes','bluebarries')
#fruit = tuple('apple','mango','orange','bluebarries','pears') --> using constructor

#single value needs trailing comma
fruit2 = ('Apples',)

#get value
print(fruit[1])

# Cannot change the value
#fruit[0] = 'pears'

# Delete tuple 
del fruit2

# get the length
print(len(fruit))


# create a set

fruits_set = {'apple','pears','bluebarries','mango'}

# check if in set
print('apple' in fruits_set)

#Add to set
fruits_set.add('grapes')
print(fruits_set)

#Remove from set
fruits_set.remove('bluebarries')
print(fruits_set)

#clear a set
fruits_set.clear()
print(fruits_set)

#Delete a set
del fruits_set
print(fruits_set)