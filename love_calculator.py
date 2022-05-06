# This is a love calculator program. It takes the names of two people from the User
# It checks the number of times the letters in the word "TRUE" (i.e. "T", "R", "U", "E") is found in both names
# It also found the number of times the letters in the word "LOVE" (i.e. "L", "O", "V", "E") is found in both names
# It then combines these numbers to make a 2-digit number e.g. if the letters in TRUE occurs 3 times and the letters
# in "LOVE" occurs 5 times, it combines the numbers to give "35".

print("Welcome to the Love Calculator!")
# Take 2 different names from the user and convert to a lower case
name1 = (input("What is your name?\n")).lower()
name2 = (input("What is her name? \n")).upper()

# count the number of times the letters in "TRUE" is found in both names
num_of_T = (name1+name2).count("t")
num_of_R = (name1+name2).count("r")
num_of_U = (name1+name2).count("u")
num_of_E = (name1+name2).count("e")
# Print the number of occurrence of the individual letters in "TRUE"
print(f"T occurs {num_of_T}")
print(f"R occurs {num_of_R}")
print(f"U occurs {num_of_U}")
print(f"E occurs {num_of_E}")

# Add the number of the individual letters in "TRUE" and print it
num_True = num_of_T + num_of_R + num_of_U + num_of_E
print((f"Total = {num_True}"))

# count the number of times the letters in "LOVE" is found in both names
num_of_L = (name1+name2).count("l")
num_of_O = (name1+name2).count("o")
num_of_V = (name1+name2).count("v")
num_of_E = (name1+name2).count("e")

# Print the number of occurrence of the individual letters in "LOVE"
print(f"L occurs {num_of_L} times")
print(f"O occurs {num_of_O} times")
print(f"L occurs {num_of_V} times")
print(f"L occurs {num_of_E} times")
# Add the number of the individual letters in "LOVE" and print it
num_Love = num_of_L + num_of_O + num_of_V + num_of_E
print(f"Total = {num_Love}")

# combine the two-digits
is_compatible_num = str(num_True) + str(num_Love)
is_compatible_num = int(is_compatible_num)

# print appropriate sentence depending on the value the 2-digit number
if is_compatible_num < 10 or is_compatible_num > 90:
    print(f"Your score is {is_compatible_num}. You are good for each other 🥰")
elif is_compatible_num >= 40 and is_compatible_num <= 50:
    print(f"Your score is {is_compatible_num}. You are fairly okay for each other. ")
elif is_compatible_num >= 60 and is_compatible_num <= 70:
    print(f"Your score is {is_compatible_num}. You will both make an adorable couple")
else:
    print(f"Your score is {is_compatible_num}.")
