def create_username(first, last, idnumber):
  '''
  Function takes strings for first name, last name, and idnumber and creates a username from
  the first three characters of each name and the last three characters of the idnumber
  and concatenating them together. The function then returns the username as a string.
  param first: string for first name
  param last: string for last name
  param idnumber: string for idnumber
  return: string of created username
  '''
  # Create username using string slicing
  username = first[:3].lower() + last[:3].lower() + idnumber[-3:].lower()
  # Return string username
  return username


def valid_password(password):
  '''
  Function takes a proposed password and checks if it meets the conditions of being at
  least eight characters long, contain at least one uppercase letter, one lowercase
  letter, and one digit. If the password satisfies all requirements, the function
  returns True. It returns False otherwise.
  param password: string for proposed password
  return: boolean value for if the password meets the requirements
  '''
  # Check length requirement
  length = len(password) >= 8

  # Check for one uppercase letter
  up = not password.islower()

  # Check for one lowercase letter
  low = not password.isupper()

  # Check for digit
  digit = password.isalnum() and not password.isalpha()

  # Return boolean
  return length and up and low and digit



def main():
  # Get name and ID number from user
  print("You will be assigned a username based on the information you provide below.")
  first = input("First Name: ")
  last = input("Last Name: ")
  idnumber = input("ID Number: ")

  # Create username
  username = create_username(first, last, idnumber)

  # Inform user of username
  print(f"You new username will be {username}. Now it is time to pick a password.",
        "\nPlease pick a password that meets the following conditions:",
        "\n\t- At least eight characters in length.",
        "\n\t- Contain at least one uppercase letter.",
        "\n\t- Contain at least one lowercase letter.",
        "\n\t- Contain at least one digit.")
  # Get password
  password = input("Password: ")
  # Keep prompting user for password until conditions have been met
  while not valid_password(password):
    print("That is not a valid password. Please follow the following conditions",
          "\n\t- At least eight characters in length.",
          "\n\t- Contain at least one uppercase letter.",
          "\n\t- Contain at least one lowercase letter.",
          "\n\t- Contain at least one digit.")
    password = input("Password: ")

  # Give confirmation
  print("Your username and password have been set.")



if __name__ == "__main__":
  main()