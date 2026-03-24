"""
🎮 Hangman Game
Classic word guessing game with category selection and visual hangman.
Author: Priyanka
"""

import random

CATEGORIES = {
    "Animals": ["elephant", "giraffe", "dolphin", "penguin", "butterfly", "crocodile", "kangaroo"],
    "Fruits": ["strawberry", "pineapple", "watermelon", "blueberry", "pomegranate", "raspberry"],
    "Technology": ["python", "javascript", "computer", "keyboard", "algorithm", "database", "software"],
    "Countries": ["australia", "brazil", "canada", "germany", "japan", "india", "france"]
}

HANGMAN_STAGES = [
    """
     ┌───┐
     │   │
         │
         │
         │
    ─────┴──
    """,
    """
     ┌───┐
     │   │
     O   │
         │
         │
    ─────┴──
    """,
    """
     ┌───┐
     │   │
     O   │
     │   │
         │
    ─────┴──
    """,
    """
     ┌───┐
     │   │
     O   │
    /│   │
         │
    ─────┴──
    """,
    """
     ┌───┐
     │   │
     O   │
    /│\\  │
         │
    ─────┴──
    """,
    """
     ┌───┐
     │   │
     O   │
    /│\\  │
    /    │
    ─────┴──
    """,
    """
     ┌───┐
     │   │
     O   │
    /│\\  │
    / \\  │
    ─────┴──
    """
]

def display_word(word, guessed):
    return ' '.join(c if c in guessed else '_' for c in word)

def hangman():
    print("=" * 40)
    print("   🎮 HANGMAN GAME")
    print("=" * 40)
    
    while True:
        # Category selection
        print("\n📚 Categories:")
        cats = list(CATEGORIES.keys())
        for i, cat in enumerate(cats, 1):
            print(f"   {i}. {cat}")
        
        try:
            cat_choice = int(input("\n👉 Pick a category (1-4): "))
            category = cats[cat_choice - 1]
        except (ValueError, IndexError):
            category = random.choice(cats)
            print(f"   Using random category: {category}")
        
        word = random.choice(CATEGORIES[category]).lower()
        guessed = set()
        wrong_guesses = 0
        max_wrong = 6
        
        print(f"\n🎯 Category: {category}")
        print(f"📏 Word has {len(word)} letters\n")
        
        while wrong_guesses < max_wrong:
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"   Word: {display_word(word, guessed)}")
            print(f"   ❌ Wrong guesses: {wrong_guesses}/{max_wrong}")
            print(f"   🔤 Used letters: {', '.join(sorted(guessed)) if guessed else 'None'}")
            
            guess = input("\n   Guess a letter: ").strip().lower()
            
            if not guess or len(guess) != 1 or not guess.isalpha():
                print("   ⚠️ Enter a single letter!")
                continue
            
            if guess in guessed:
                print("   ⚠️ Already guessed that letter!")
                continue
            
            guessed.add(guess)
            
            if guess in word:
                print(f"   ✅ '{guess}' is in the word!")
                if all(c in guessed for c in word):
                    print(f"\n🎉 Congratulations! The word was: {word.upper()}")
                    print("🏆 You won!")
                    break
            else:
                wrong_guesses += 1
                print(f"   ❌ '{guess}' is not in the word!")
        else:
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"\n😢 Game Over! The word was: {word.upper()}")
        
        again = input("\n🔄 Play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n👋 Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    hangman()
