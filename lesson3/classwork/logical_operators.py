age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes":
    print("You can enter the movie theater.") # AND: both conditions must be true
else:
    print("You cannot enter the movie theater.")

print("Entry check complete.")

has_pass = input("Do you have a bus pass? (yes/no) ")
has_coin = input("Do you have a coin? (yes/no) ")
if has_pass == "yes" or has_coin == "yes": # OR: at least one condition must be true
    print("You can ride the bus.")
else:
    print("You cannot ride the bus.")

print("Bus ride check complete.")

homework_done = input("Have you done your homework? (yes/no) ")

if not homework_done == "yes":
    print("You need to do your homework.")
else:
    print("Good job on completing your homework!")