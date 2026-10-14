# ask user for their name
name = input("Whats your name? ")

#remove whitespaces from str
name = name.strip()

#Capitalize Users name
name = name.title()

# split user's name in to first and last name
first, last = name.split(" ")

# say hello to user
print(f"Hello, {first}") 



# Better way for same code
# name = input("Whats your name? ").strip().title()
