"""
✊✋✌️ Rock Paper Scissors
Play against the computer with score tracking and statistics.
Author: Priyanka
"""

import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    return 'player' if wins[player] == computer else 'computer'

def display_choices(player, computer):
    emojis = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
    print(f"\n   You: {emojis[player]}  {player.upper()}")
    print(f"   CPU: {emojis[computer]}  {computer.upper()}")

def rock_paper_scissors():
    print("=" * 40)
    print("   ✊✋✌️ ROCK PAPER SCISSORS")
    print("=" * 40)
    
    stats = {'wins': 0, 'losses': 0, 'ties': 0, 'rounds': 0}
    
    print("\nBest of luck! Type 'quit' to exit.\n")
    
    while True:
        choice = input("🎮 Choose (rock/paper/scissors): ").strip().lower()
        
        if choice == 'quit':
            break
        
        if choice not in ['rock', 'paper', 'scissors']:
            # Allow shortcuts
            shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
            choice = shortcuts.get(choice)
            if not choice:
                print("❌ Invalid! Use rock, paper, scissors (or r, p, s)")
                continue
        
        computer = get_computer_choice()
        stats['rounds'] += 1
        
        display_choices(choice, computer)
        
        result = determine_winner(choice, computer)
        
        if result == 'tie':
            stats['ties'] += 1
            print("🤝 It's a tie!")
        elif result == 'player':
            stats['wins'] += 1
            print("🎉 You win this round!")
        else:
            stats['losses'] += 1
            print("💻 Computer wins this round!")
        
        print(f"   📊 Score: You {stats['wins']} — {stats['losses']} CPU  (Ties: {stats['ties']})")
    
    # Final stats
    print(f"\n{'=' * 40}")
    print("📊 FINAL STATISTICS")
    print(f"{'=' * 40}")
    print(f"   Rounds played: {stats['rounds']}")
    print(f"   Wins:   {stats['wins']} 🏆")
    print(f"   Losses: {stats['losses']} 💔")
    print(f"   Ties:   {stats['ties']} 🤝")
    
    if stats['rounds'] > 0:
        win_rate = (stats['wins'] / stats['rounds']) * 100
        print(f"   Win rate: {win_rate:.1f}%")
    
    print(f"\n👋 Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors()
