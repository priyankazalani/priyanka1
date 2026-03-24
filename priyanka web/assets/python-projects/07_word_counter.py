"""
📝 Word Counter & Text Analyzer
Analyze text for word count, character count, most common words, and more.
Author: Priyanka
"""

from collections import Counter
import string

def analyze_text(text):
    # Basic counts
    char_count = len(text)
    char_no_space = len(text.replace(' ', ''))
    words = text.split()
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    line_count = text.count('\n') + 1
    
    # Word frequency
    clean_words = []
    for word in words:
        cleaned = word.strip(string.punctuation).lower()
        if cleaned:
            clean_words.append(cleaned)
    
    word_freq = Counter(clean_words)
    most_common = word_freq.most_common(5)
    
    # Average word length
    avg_word_len = sum(len(w) for w in clean_words) / max(len(clean_words), 1)
    
    # Longest and shortest word
    longest = max(clean_words, key=len) if clean_words else "N/A"
    shortest = min(clean_words, key=len) if clean_words else "N/A"
    
    return {
        'char_count': char_count,
        'char_no_space': char_no_space,
        'word_count': word_count,
        'sentence_count': max(sentence_count, 1),
        'line_count': line_count,
        'most_common': most_common,
        'avg_word_len': avg_word_len,
        'longest': longest,
        'shortest': shortest,
        'unique_words': len(set(clean_words))
    }

def display_results(stats):
    print(f"\n{'=' * 45}")
    print("   📊 TEXT ANALYSIS RESULTS")
    print(f"{'=' * 45}")
    print(f"   📝 Characters (total):    {stats['char_count']}")
    print(f"   📝 Characters (no space): {stats['char_no_space']}")
    print(f"   📖 Words:                 {stats['word_count']}")
    print(f"   💬 Sentences:             {stats['sentence_count']}")
    print(f"   📄 Lines:                 {stats['line_count']}")
    print(f"   🔤 Unique words:          {stats['unique_words']}")
    print(f"   📏 Avg word length:       {stats['avg_word_len']:.1f}")
    print(f"   📐 Longest word:          {stats['longest']}")
    print(f"   📎 Shortest word:         {stats['shortest']}")
    
    print(f"\n   🏆 Top 5 Most Used Words:")
    for word, count in stats['most_common']:
        bar = "█" * min(count, 20)
        print(f"      {word:<15} {bar} ({count})")
    
    print(f"{'=' * 45}")

def word_counter():
    print("=" * 40)
    print("   📝 WORD COUNTER & TEXT ANALYZER")
    print("=" * 40)
    
    while True:
        print("\n📂 Options:")
        print("1. Analyze typed text")
        print("2. Analyze from file")
        print("3. Exit")
        
        choice = input("\n👉 Choose (1-3): ").strip()
        
        if choice == '1':
            print("\n✍️ Type your text (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == '':
                    break
                lines.append(line)
            
            text = '\n'.join(lines)
            if text.strip():
                stats = analyze_text(text)
                display_results(stats)
            else:
                print("❌ No text entered!")
        
        elif choice == '2':
            filepath = input("\n📁 Enter file path: ").strip()
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                if text.strip():
                    stats = analyze_text(text)
                    display_results(stats)
                else:
                    print("❌ File is empty!")
            except FileNotFoundError:
                print("❌ File not found!")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    word_counter()
