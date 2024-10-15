#Create a functions

def Hello(name="Aman"):
    print(f"Hello {name}")

Hello()

#Return a value
def GetSum(num1,num2):
    total = num1+num2
    return total

num = GetSum(4,5)
print(num)

#Lambda Function
getsum = lambda num1,num2 : num1+num2
print(getsum(10,50))