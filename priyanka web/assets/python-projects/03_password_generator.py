"""
🔐 Password Generator
Generate strong, random passwords with customizable options.
Author: Priyanka
"""

import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one character from each selected category
    password = []
    password.append(random.choice(string.ascii_lowercase))
    
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Fill remaining length
    remaining = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining))
    
    # Shuffle to randomize positions
    random.shuffle(password)
    return ''.join(password)

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 1
    
    levels = {0: "Very Weak 🔴", 1: "Weak 🟠", 2: "Fair 🟡", 3: "Good 🟢", 4: "Strong 💪", 5: "Very Strong 🔒"}
    return levels.get(score, "Unknown")

def password_generator():
    print("=" * 40)
    print("   🔐 PASSWORD GENERATOR")
    print("=" * 40)
    
    while True:
        try:
            length = int(input("\n📏 Password length (8-50): "))
            if length < 8:
                print("⚠️ Minimum length is 8. Setting to 8.")
                length = 8
            elif length > 50:
                length = 50
        except ValueError:
            length = 12
            print("Using default length: 12")
        
        upper = input("Include uppercase? (y/n): ").strip().lower() != 'n'
        digits = input("Include numbers? (y/n): ").strip().lower() != 'n'
        special = input("Include symbols? (y/n): ").strip().lower() != 'n'
        
        try:
            count = int(input("How many passwords? (1-10): "))
            count = max(1, min(count, 10))
        except ValueError:
            count = 1
        
        print(f"\n{'─' * 40}")
        print("🔑 Generated Passwords:")
        print(f"{'─' * 40}")
        
        for i in range(count):
            pwd = generate_password(length, upper, digits, special)
            strength = check_strength(pwd)
            print(f"  {i+1}. {pwd}")
            print(f"     Strength: {strength}")
        
        print(f"{'─' * 40}")
        
        again = input("\n🔄 Generate more? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n👋 Stay safe online! 🔒")
            break

if __name__ == "__main__":
    password_generator()
