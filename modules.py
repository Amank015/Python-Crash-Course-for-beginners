# Create a module

'''
import datetime 
today = datetime.date.today()
print(today)
'''

from datetime import date
import time

from camelcase import CamelCase

# Import custom module
import validator 
from validator import validate_email


today = date.today()
timestamp = time.time()
c = CamelCase()
print(c.hump('hello there world'))
email = 'test@test.com'
if validate_email(email):
    print("Email is valid")
else:
    print("Email is not valid")    
print(timestamp)

