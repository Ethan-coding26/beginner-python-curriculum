# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
first_num = int(input("enter your first test score:"))
second_num = int(input("enter your second test score:"))
if first_num >= 50 and second_num >= 50:
    print ("you passed both!")
else:  
    print ("you failed at least one")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print"You're fully ready !"
# If they brought neither, print "You're not ready."
lunch = input("enter yes/no if you brought lunch:")
water = input("enter yes/no if you brought water:")
if lunch == "yes" and water == "yes":
    print("You're fully ready!")
elif lunch == "yes" or water == "yes":
    print ("You're somewhat ready")
else:
    print("You're not ready")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
num = int(input("enter a number:"))
if num >=1 and num <=10:
    print ("in range")
else:
    print ("out of range")

# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
test_score = int(input("enter your test score:"))
if test_score >=90:
    print("A")
elif test_score >=80:
    print ("B")
elif test_score >=70:
    print ("C")
elif test_score >=60:
    print ("D")
else:
    print("F")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
#   Otherwise, print "Plain pair.
first_num = int(input("enter your first number:"))
second_num = int(input("enter your second number:"))
if (first_num % 5 == 0 and second_num % 2 != 0):
    print("Interesting pair!")
else:
    print("Plain pair")