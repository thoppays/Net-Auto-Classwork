#This is your first Python Subscription
# After each step save your script as "1.py" and run it in a virtual environment
# 1. Write code to print your name to the screen
# 2. Make a variable with your full name and print the variable
# 3. Make another variable with called "age" with your age and print it
# 4. Make another varialbe with called "Age" with your age and print it
# 5. Make another variable that has your age * 17 and print the result
# 6. Print to the screen "XX is a string" using a variable for "XX"
# 6. Use the type function print to the screen "age", "Age" and "Name"
# 7. Print the output of dir() of the name string
# 8. Print a blank line
# 9. Print the output of dir() of age integer
# 10. Create a variable called "info" that can contain 4 different pieces of data
#    - Then use the info variable and function to print "a b c d"
# 11. Print the info variable with "1 2 3 4"
# 12. Make 2 new variables your height and weight
#     - Then print with info your name, age, height and weight
# Good Luck
print ("Saravana Thoppay")
name="TVS"
print (name)
name="Saravana Thoppay"
print (name)
age=46
print (age)
Age="46"
print (Age)
age17=age*17
print (age17)
print ("Age "+ Age + " is a string")
print (type(age))
print (type(Age))
print (type(name))
print (dir(name))
print ("\n")
print (dir(age))
info = "{} {} {} {}"
print(info.format("1","2","3","4"))
height = 5.9
weight = 160
print (info.format(name, age, height, weight))
