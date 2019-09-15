import os
import sys

class Employee:
   """Employee class"""
   def __init__(self, first, last):
      self.last = last
      self.first = first

   def email(self):
      self.email = "{}.{}@gmail.com".format(self.first,self.last)
      return self.email

emp_1 = Employee('aar', 'kay')

print(emp_1.last)
print(emp_1.first)
print(emp_1.email())
