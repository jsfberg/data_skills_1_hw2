# PPHA 30535
# Spring 2022
# Homework 2

# RIMJHIM AGRAWAL
# RIMJHIMCODES

# Due date: Sunday April 17th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

def sumvsten(a,b):
    n = a+b
    if (n==10):
        return "just right"
    elif (n>10):
        return "big"
    else:
        return "small"
        
answer = [sumvsten(tup[0],tup[1]) for tup in start_list]

# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

def my_func(a):
    b = 30
    return a + b
x = my_func()

# We prefer using arguments over global variables in functions because in 
# larger codes it is easy to lose track of global variables


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random
  
import random
import string

def password(length, special_chars = True):
    if (length<=16 and length >= 8):
        if special_chars == True:
            char_set = string.ascii_letters +string.digits + string.punctuation
            pwd = ''.join(random.choice(char_set) for i in range(length))
        else:
            char_set = string.ascii_letters +string.digits
            pwd = ''.join(random.choice(char_set) for i in range(length))
    else:
        return "Password length invalid. Try again."
    return pwd
  
password(9)
password(16, special_chars=False)
password(7)
    
# Ref: https://pynative.com/python-generate-random-string/
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 1, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes any number of these instances and 
# returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class COVID_data():
    def __init__(self, name, vac, doses, covid):
        self.name = name
        self.vac = vac
        self.doses = doses
        self.covid = covid
    def __get_record__(self):
        if (self.covid == True):
            return self.name , "has" , self.doses , "of" , self.vac , "and has had COVID" 
        else:
            return self.name , "has" , self.doses , "of" , self.vac , "and has never had COVID"
    def __same_shot__(self, __init__):
        if self.vac == __init__.vac:
            return self.name, "and", __init__.name , "got the same vaccine"
        else:
            return self.name, "and", __init__.name ,"got different vaccnines"
        
def all_data(*narg):
    comp = [[arg.name, arg.vac, arg.doses, arg.covid] for arg in narg]
    return comp
    
inst1 = COVID_data("Aaron", "Moderna", 1, False)
inst2 = COVID_data("Ashu", "Pfizer", 2, False)
inst3 = COVID_data("Alison", "none", 0, True)
inst4 = COVID_data("Asma", "Pfizer", 1, True)
inst1.__get_record__()
inst2.__same_shot__(inst3)
all_data(inst1, inst4)

# Ref: https://www.geeksforgeeks.org/args-kwargs-python/
# Ref: https://stackoverflow.com/questions/55045982/quick-way-to-convert-all-instance-variables-in-a-class-to-a-list-python