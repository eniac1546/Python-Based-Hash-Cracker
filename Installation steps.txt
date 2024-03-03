# Hash Cracking Project

## Overview
This project demonstrates the capability of cracking SHA-1 hashed passwords using a combination of Python scripting and Hashcat. It aims to showcase the methods and tools used in ethical hacking to understand and improve password encryption techniques.

## Features
- Python script for generating password variants from a dictionary.
- Utilization of Hashcat for efficient brute-force attacks.
- Capable of cracking various patterns including numeric, alphanumeric, and dictionary-based passwords.

## Prerequisites
- Python 3.x
- Hashcat
- Crunch
- Access to a command-line interface

## Installation & Setup
2. **Navigate to the Project Directory**:  
   `cd hash_cracking_project`
3. **Install Python Dependencies** (if any):  
   `pip install -r requirements.txt`

## Usage
1. **Load your dictionary file** into the project directory.
2. **Place the SHA-1 hash file** you want to crack in the project directory.
3. **Run the Python Script**:  
   `python3 hash_cracker.py`
4. **For Hashcat execution**, use the appropriate command based on your hash type and wordlist.

5. ** Run the hash_cracker.py to crack the hash values of the single word and doublw word combination

6. ** Run the hash_cracker_neumeric.py to crack the numeric password hashes.

7. ** Run the 3word_combination_crack.py to crack the word+word+word combination
alternately 
Use hashcat to crack the 3word comnbination
commands
-----hashcat -a 1 dictionary.txt  dictionary.txt  --stdout > new_wrd.txt    /// to create the two word wordlist and then combine it with the dictionary to perform the 3 word combination hash attack.
-----hashcat -m 100 -a 1 password_sha1_RB.txt dictionary.txt new_wrd.txt -o cracked_passwords.txt --force   ///// to crack the hash with 3 word combination

8. ** To crack the alpha numeric hash
Use Crunch to generate the numeric keyspace "crunch 1 4 0123456789 -o nubers.txt > dev/null 2>&1"   ///// command to creat the keyspace 

use hashcat to perform the attack "hashcat -m 100 -a 1 password_sha1_RB.txt.txt dictionary.txt nubers.txt -o cracked.txt --force"

all the descriptions are there in the report, check it for more details.
