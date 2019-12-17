#This is your first Python Subscription
# After each step save your script as "3.py" and run it in a virtual environment
# 1. Using input collect the following pieces of information
#     - Your first name
#     - Your family Name
#     - Your age
#     - Your country of residence
# 2. Using @operators print out the following sentence *<first name> <last name> is <age> years old and lives in <country>*
#     - substitute the values you collected into the sentence dynamically
# 3. Use the .format function to print out the same sentence and variables dynamically
# 4. Use an f string to print out the same sentence and variables
# 5. Bonus change the first_name and last_name to upper case
# Good Luck

firstnm = input("Enter your first name: ")
familynm = input("Enter your family name: ")
age = input("Enter your age: ")
countrynm = input("Enter your country name: ")

print ("%s %s is %s years old and lives in %s" %(firstnm, familynm, age, countrynm))

print ("{} {} is {} years old and lives in {}".format(firstnm, familynm, age, countrynm))

print (f'{firstnm} {familynm} is {age} years old and lives in {countrynm}')

print (f'{firstnm.upper()} {familynm.upper()} is {age} years old and lives in {countrynm}')

