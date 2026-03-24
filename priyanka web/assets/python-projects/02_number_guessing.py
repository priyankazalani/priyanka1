"""
🎯 Number Guessing Game
Guess a random number between 1 and 100 with hints!
Author: Priyanka
"""

import random

def number_guessing_game():
    print("=" * 40)
    print("   🎯 NUMBER GUESSING GAME")
    print("=" * 40)
    
    while True:
        secret = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        
        print(f"\n🔮 I'm thinking of a number between 1 and 100.")
        print(f"   You have {max_attempts} attempts. Good luck!\n")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
            except ValueError:
                print("❌ Please enter a valid number!")
                continue
            
            attempts += 1
            
            if guess == secret:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                if attempts <= 3:
                    print("🏆 You're a mind reader!")
                elif attempts <= 6:
                    print("⭐ Great job!")
                else:
                    print("👍 You made it!")
                break
            elif guess < secret:
                remaining = max_attempts - attempts
                print(f"📈 Too low! ({remaining} attempts left)")
            else:
                remaining = max_attempts - attempts
                print(f"📉 Too high! ({remaining} attempts left)")
        else:
            print(f"\n😢 Out of attempts! The number was {secret}.")
        
        play_again = input("\n🔄 Play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    number_guessing_game()
