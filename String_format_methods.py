name = "aman"
age = 21
print(name,age)

#Concatenate
print('hello,my name is '+name+'and I am '+str(age))

#String Formatting

#Arguments by position
print('My name is {name} and I am {age}'.format(name=name,age=age))

#F-strings (3.6+version)
print(f'hello , my name is {name} I am {age}')

#string methods

s = "coderaman"

#1.Capitialize string -- make capital only our string
print(s.capitalize())

#2.upper --> make all uppercase
print(s.upper())

#3.lower --> make all lower
print(s.lower())

#4.len --> find the length
print(len(s))

#5.Replace --> replace one to another
print(s.replace("coder aman","khan bhai"))

#6.Count --> count that to any alphabet is in the string
sub = 'm' 
print(s.count(sub))

#7.Start with --> check the starting is true or not
print(s.startswith('coder'))

#8. Ends with --> check the ending is true or not
print(s.endswith('aman'))

#9.Split into a list split()
print(s.split())

#10.find --> find the position of each character
print(s.find('a'))

#11.isalnum --> find the all alphanumeric
print(s.isalnum())

#12. isalpha --> find the all alphabetic
print(s.isalpha())

#13. isnumeric --> find the all numeric
print(s.isnumeric())
