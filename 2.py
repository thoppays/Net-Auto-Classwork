# Lab 2
# After each step save your script as "2.py" and run it in a virtual environment
# 1. Make a string variable with the Months of the year,
#    - Insert carriage returns after each month
#    - Print the variable to ensure the output is correct
# 2. Make a string variable that contains a short paragraph
#    - Indent the fisrt line with a tab
#    - Print the paragraph to the screen and verify output
# 3. Print the value between the stars *Jed's mom said "Hello World!"*
# 4. Have the scrip prompt and collect the 4 following values:
#    - Your favorite color
#    - Your favorite food
#    - Your favorite drink
#    - Your favorite animal
# 5. Print these 4 variables to the screen
# Good Luck

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec\n"
print (months)

para = "\tFoxes are swift and agile runners which live in family groups. \
A female fox is called a vixen, and a male is called a dog. Foxes' \
tails are multi-purpose organs. Their bushy tail helps them keep warm \
 while they are sleeping in cold weather."
print (para)

# 3
print ("Jed's mom said \"Hello World!\"")
# 4
color = input("Enter your favorite color: ")
food = input("Enter your favorite food: ")
drink = input("Enter your favorite drink: ")
animal = input("Enter your favorite animal: ")
answers = "{} {} {} {}"

print (answers.format(color, food, drink, animal))