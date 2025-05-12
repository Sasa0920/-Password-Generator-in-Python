#step 1 : get relevant data from users
#step 2 : create the password
#step 3: check the password strength
#step 4: display the password to the user

import random

def get_user_data():
  print("Welcome all! Let's create a password for you.")
  name = input("Please enter your name : ")
  length = int(input("Please enter the length of the password you want : "))
  while length<8:
    print("password length should be at least 8 characters.Please try again.")
    length = int(input("Please enter the length of the password you want : "))
 
  print("Great! let's create your password.")

  numbers= int(input("how many numbers do you want to include in your password? (0-9) : "))
  characters = int(input("how many special characters do you want to include in your password? (e.g. !@#$%^&*) : "))
  upper_case = int(input("how many upper case letters do you want to include in your password? (A-Z) : "))
  lower_case = int(input("how many lower case letters do you want to include in your password? (a-z) : "))

  if length < numbers+characters+upper_case+lower_case:
    print("Invalid input. please try again")
    return get_user_data()

  password = create_password(length, numbers, characters, upper_case, lower_case)
  strength = check_password_strength(password)
  display_password(name, password, strength)

def create_password(length, numbers, characters, upper_case, lower_case):
  password=[] # by using this we can collect all the characters

  #for _ in range(numbers):
  #  digit = random.randint(0,9)
  #  password.append(str(digit))
  password += [str(random.randint(0,9)) for _ in range(numbers)] # Repeat this block numbers times, i dont care which time it is.
  password += [random.choice("!@#$%^&*") for _ in range(characters)]
  password += [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(upper_case)]
  password += [random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(lower_case)]
  
  remains = length-len(password)
  password += [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*") for _ in range(remains)]

  random.shuffle(password) #make sure the password looks random,not grouped

  return ''.join(password) #converts the list of characters into a single string

def check_password_strength(password):
  if len(password) < 8:
    return "Weak"
  elif len(password)<=12:
    return "Medium"
  else:
    return "Strong"
  
def display_password(name, password, strength):
  print(f"Hey {name} , your password is : {password}")
  print(f"Password strength is : {strength}")

get_user_data()



