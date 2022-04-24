import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#lists of characters, numbers, and letters for password generator

print('Hello Welcolme to the password genrerator.')

q_letters= int(input("How many letters would you like in your password?\n")) 
q_special_characters = int(input(f"How many symbols would you like?\n"))
q_numbers = int(input(f"How many numbers would you like?\n"))
#ask user for input on prefered password length

password = ""
#this is where the password will be stored

for x in range(1, q_letters + 1):
    password += random.choice(Letters)
#for loop that grabs a random letter the amount of times a user prefers
# ex. if a user wants three letters the loop will randomize three letters and store it into the variable password

for x in range(1, q_special_characters + 1):
    password += random.choice(special_characters)
#for loop that grabs random symbols the amount of times a user prefers

for x in range(1, q_numbers + 1):
    password += random.choice(Numbers)
#for loop that grabs a random number the amount of time a user prefers

shuffled_password = list(password)

random.shuffle(shuffled_password)
#turn the variable password to a list and use random.shuffle() to shuffle the password
print(''.join(shuffled_password))
#return to user the final shuffled password