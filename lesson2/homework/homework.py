# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines
first_number = input("What is the first number?")
second_number = input("What is the second number?") 
print("The quotient is: ", int(first_number) // int(second_number))
print("The remainder is: ", int(first_number) % int(second_number))

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
favorite_animal = input("What is your favorite animal?")
favorite_color = input("What is your favorite color?")
print("A " + favorite_color + " " + favorite_animal + " would be awesome!")

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
print("The even numbers from 0 to 10 are:")
for number in range(0, 11, 2):
    print(number)

# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
print ("How many push-ups can you do?")
pushups = input()
print("In a week, you could do " + str(int(pushups) * 7) + " push-ups!")

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
print("The squares of the numbers from 1 to 6 are:")
for squ_num in range(1, 7, 1):
    print(squ_num ** 2) 
