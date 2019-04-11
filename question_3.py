'''Question 3'''
import re

EMAIL = re.compile(r'^[a-zA-Z]+[a-zA-Z0-9]*@[\.[a-zA-Z0-9]*[\.[a-zA-Z]+$')

email = input()

if not EMAIL.match(email):
    print("Invalid")
else:
    print("Valid")