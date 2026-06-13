"""

Project: Password Strength Tester (Password Strength)
Course: CSE 111 Block-3 of BYU-Idaho
Student: Israel Betancourt
Description: Verifies passwords against dictionaries and common use list,
calculating a good security score from 0 to 5.

"""

# ---1. character lists needed---
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

# ---2. function to search for external files ---
# this function connects your code with 'wordlist.txt' and 'toppasswords.txt'

def word_in_file(word, filename, case_sensitive=False):
    try:
        #open the requested file with the required encoding (utf-8)
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # .strip() removes leading and trailing whitespace, including newlines
                clean_line = line.strip

                if case_sensitive:
                      # Exact comparison (for toppasswords.txt)
                    if word == clean_line:
                        return True
                else:
                    # Comparison ignoring case (for wordlist.txt)
                    if word.lower() == clean_line.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: The file {filename} is not found in the folder.")
    return False

# --- 3. HELP FUNCTIONS FOR COMPLEXITY ---

def word_has_character(word, character_list):
     # Returns True if any character from the list is in the word
     return any(char in character_list for char in word)

def word_complexity(word):
     # Sum a point for each type of character found (0 to 4)
    complexity = 0
    if word_has_character(word, LOWER): complexity += 1
    if word_has_character(word, UPPER): complexity += 1
    if word_has_character(word, DIGITS): complexity += 1
    if word_has_character(word, SPECIAL): complexity += 1
    return complexity

# --- 4. logic for strength (MARIA'S RULES) ---

def password_strength(password, min_length=10, strong_length=16):
     # STEP 1: Search in the dictionary (wordlist.txt) - NOT case-sensitive
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
     # STEP 2: Search in common passwords (toppasswords.txt) - CASE-SENSITIVE
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # STEP 3: Verify minimum length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    # STEP 4: Verify if it's a long and secure password
    if len(password) > strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # STEP 5: If none of the above, calculate by complexity
    return 1 + word_complexity(password)

# --- 5. user interface (main) ---
def main():
    print("--- Welcome to the Password Analyzer ---")

    while True:
        user_input = input("\nEnter a password to test (or 'q' to quit): ")
        
          # If the user enters 'q' or 'Q', we close the program
        if user_input.lower() == 'q':
            print("Exiting the program...")
            break
        
        # Calculate the strength of the password using the defined function
        strength = password_strength(user_input)
        
        # Display the visual result (This helps to give a good impression)
        stars = "★" * strength + "☆" * (5 - strength)
        print(f"Security level: {stars} ({strength}/5)")

# --- 6. ENTRY POINT ---
if __name__ == "__main__":
    main()
