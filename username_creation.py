# Get first name
first_name = input("First Name: ")

# Get last name
last_name = input("Last Name: ")

# Get ID number
id = input("ID Number: ")

# Create username
username = first_name[:3] + last_name[:3] + id[-3:]

# Display username
print(username)