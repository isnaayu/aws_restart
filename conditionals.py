"""
Working with Conditionals

A section of code that compares two pieces of information is called a conditional statement. You can use conditionals to create different paths through the program. Using comparative operators, you will write a program that makes decisions.
In this lab, you will:
--Use the if statement
--Use the else statement
--Use the elif statement
"""

# Working with the if statement
userReply = input("Do you need to ship a package? (enter yes or no)")

if userReply == "yes":
    print("We can help you ship that package!")

# Working with the else statement
else:
    print("Please come back if you need to ship a package. Thank you")
    
# Working with the elif statement

userReply2 = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply2 == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply2 == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply2 == "copy":
    copies = input("how many copies would you like? (enter number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
