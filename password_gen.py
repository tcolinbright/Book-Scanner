import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Define the output file name
output_file = "generated_passwords.txt"

# Generate passwords and save them to the file
with open(output_file, "w") as file:
    for i in range(1, 25):
        password = generate_password()
        file.write(f"{password}\n")