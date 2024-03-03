import hashlib
import itertools

# Load words from the dictionary file
with open('dictionary.txt', 'r', encoding='latin-1') as file:
    dictionary_words = file.read().splitlines()

# Load hashed passwords
with open('password_sha1_RB.txt', 'r') as file:
    hashed_passwords = set(file.read().splitlines())

# Function to generate SHA-1 hash
def generate_sha1_hash(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

# Generator function to create password variants
def create_password_variants(dictionary_words):
    # Single word, two-word, and three-word combinations
    for r in range(1, 4):
        for combo in itertools.product(dictionary_words, repeat=r):
            yield ''.join(combo)

# Cracked passwords set
cracked_passwords = set()

# Crack passwords
for pwd in create_password_variants(dictionary_words):
    print(f"Checking: {pwd}", end='\r')  # Update the password being checked on the same line
    hashed_pwd = generate_sha1_hash(pwd)
    if hashed_pwd in hashed_passwords and hashed_pwd not in cracked_passwords:
        cracked_passwords.add(hashed_pwd)
        print(f"Cracked: {pwd} -> {hashed_pwd}  ")
        hashed_passwords.remove(hashed_pwd)  # Remove the cracked hash

# Optional: Print total number of cracked passwords
print(f"\nTotal Cracked Passwords: {len(cracked_passwords)}")