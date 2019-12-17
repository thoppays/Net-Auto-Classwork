#This is your first Python Subscription
# After each step save your script as "5.py" and run it in a virtual environment
# 1. Create a list with the following values in this order
#    - cats
#    - dogs
#    - 17
#    - [1,2,3]
# 2. From this list print to the screen the second value (dogs)
# 3. From this list print to the screen the second value of the 4th object (2)
# 4. Append to the end of the list a new value of "cisco" and then print the list
# 5. Remove dogs from the list
# 6. Create a new blank dictionary
# 7. Populate the dictionary with the following key/value pairs
#    - drink:coke
#    - entree:burger
#    - side:fries
#    - dessert:cake
# 8. Print the dictionary to verify it is correct
# 9. Print to the screen the value that goes with the entree key
# Good Luck

# 1.
mylist = ['cats', 'dogs', 17, [1,2,3]]

# 2,
print (mylist[1])

# 3.
print (mylist[3][1])

# 4. 
mylist.append('cisco')
print (mylist)

# 5.
mylist.remove('dogs')
print (mylist)

# 6. 
mydit = {}

# 7.
mydict = {'drink':'coke', 'entree':'burger', 'side':'fries', 'dessert': 'cake'}

# 8.
print (mydict)

# 9.
print (mydict['entree'])