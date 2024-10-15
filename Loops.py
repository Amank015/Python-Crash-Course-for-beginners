people = ["Aman","Rehan","Abhishek","Ayush","Arun"]

# simple for loop
'''
for person in people:
    print(f'Current person: {person}')
'''
    
# Break 
'''
for person in people:
    if person == "Rehan":
        break
    print(f'current person: {person}')    
'''
    
# Continue
'''
for person in people:
    if person == "Rehan":
        continue
    print(f'current person: {person}')        
    
'''

#range in for loop
for i in range(len(people)):
    print(people[i])
    
for i in range(0,11):
    print(f'Number:{i}')
        
# while loop

count = 0
while count <=20:
    print(f'count:{count}')
    count+=1            
    
x = input()
for i in range(1,11):
    print(i*x)    