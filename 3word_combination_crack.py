import hashlib
import itertools
import codecs

# Function to generate SHA-1 hash
def generate_sha1_hash(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

# Load words from the dictionary file, handling BOM if present
with codecs.open('dictionary.txt', 'r', encoding='utf-8-sig') as file:
    dictionary_words = file.read().splitlines()

# Load hashed passwords
with open('password_sha1_RB.txt', 'r') as file:
    hashed_passwords = set(file.read().splitlines())

# Cracked passwords set
cracked_passwords = set()

# Crack passwords
for word_combo in itertools.product(dictionary_words, repeat=3):
    combined_word = ''.join(word_combo)
    hashed_combined_word = generate_sha1_hash(combined_word)

    # Live checking status
    print(f"Checking: {combined_word} -> {hashed_combined_word}", end='\r')

    if hashed_combined_word in hashed_passwords and hashed_combined_word not in cracked_passwords:
        cracked_passwords.add(hashed_combined_word)
        print(f"\nCracked: {combined_word} -> {hashed_combined_word}")

# Print total number of cracked passwords
print(f"\nTotal Cracked Passwords: {len(cracked_passwords)}")
