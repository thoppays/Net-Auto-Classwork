#This is your first Python Subscription
# After each step save your script as "6.py" and run it in a virtual environment
# 1. Create a list with the following values in this order
#    - cats
#    - dogs
#    - 17
#    - [1,2,3]
# 2. Use a for loop to print the contents of the list
# 3. Create a variable that is set to 17
# 4. Use if/elif/else to determine if the number is > 20, >10 or 10 or less
# 5. Print to the screen what range the number falls within
# 6. change the variable to a number greater than 20 and make sure it works
# 7. Use a while loop to go thru and print the contents of you list, make the index number the counter
# Good Luck

# 1.
mylist = ['cats', 'dogs', 17, [1,2,3]]

# 2. 
for i in mylist:
    print (i)

# 3.
x = 17

# 4.
if x > 20:
    print (f'{x} is greater than 20')
elif x > 10:
    print (f'{x} is greater than 10')
elif x <= 10:
    print (f'{x} is equal to less than 10')
else:
    pass

# 6.
x = 100
if x > 20:
    print (f'{x} is greater than 20')
elif x > 10:
    print (f'{x} is greater than 10')
elif x <= 10:
    print (f'{x} is equal to less than 10')
else:
    pass

# 7.
ind = 0
while ind < len(mylist):
    print (mylist[ind])
    ind += 1