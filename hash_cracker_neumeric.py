import hashlib

# Load hashed passwords
with open('password_sha1_RB.txt', 'r') as file:
    hashed_passwords = set(file.read().splitlines())

# Function to generate SHA-1 hash
def generate_sha1_hash(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

# Function to generate numeric patterns
def generate_numeric_patterns(max_digits=10):
    for length in range(1, max_digits + 1):
        for number in range(10**length):
            yield str(number).zfill(length)

# Cracked passwords set
cracked_passwords = set()

# Crack passwords
for pwd in generate_numeric_patterns():
    print(f"Checking: {pwd}", end='\r')  # Update the password being checked on the same line
    hashed_pwd = generate_sha1_hash(pwd)
    if hashed_pwd in hashed_passwords and hashed_pwd not in cracked_passwords:
        cracked_passwords.add(hashed_pwd)
        print(f"Cracked: {pwd} -> {hashed_pwd}  ")
        hashed_passwords.remove(hashed_pwd)  # Remove the cracked hash

# Optional: Print total number of cracked passwords
print(f"\nTotal Cracked Passwords: {len(cracked_passwords)}")
