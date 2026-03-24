"""
📝 Quiz Game
An interactive quiz game with multiple categories and scoring.
Author: Priyanka
"""

def get_questions():
    return [
        {
            "category": "Python",
            "question": "What is the output of print(type(5))?",
            "options": ["A. int", "B. <class 'int'>", "C. integer", "D. number"],
            "answer": "B"
        },
        {
            "category": "Python",
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. func", "C. def", "D. define"],
            "answer": "C"
        },
        {
            "category": "HTML",
            "question": "What does HTML stand for?",
            "options": [
                "A. Hyper Text Markup Language",
                "B. High Tech Modern Language",
                "C. Hyper Transfer Markup Language",
                "D. Home Tool Markup Language"
            ],
            "answer": "A"
        },
        {
            "category": "HTML",
            "question": "Which tag is used for the largest heading?",
            "options": ["A. <heading>", "B. <h6>", "C. <h1>", "D. <head>"],
            "answer": "C"
        },
        {
            "category": "General",
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Processing Unit",
                "B. Computer Personal Unit",
                "C. Central Program Utility",
                "D. Computer Processing Unit"
            ],
            "answer": "A"
        },
        {
            "category": "Python",
            "question": "Which of these is a mutable data type?",
            "options": ["A. tuple", "B. string", "C. list", "D. int"],
            "answer": "C"
        },
        {
            "category": "C Language",
            "question": "Which symbol is used to end a statement in C?",
            "options": ["A. .", "B. :", "C. ;", "D. ,"],
            "answer": "C"
        },
        {
            "category": "General",
            "question": "What is 2^10?",
            "options": ["A. 512", "B. 1024", "C. 2048", "D. 256"],
            "answer": "B"
        },
        {
            "category": "Python",
            "question": "How do you start a comment in Python?",
            "options": ["A. //", "B. /*", "C. #", "D. --"],
            "answer": "C"
        },
        {
            "category": "HTML",
            "question": "Which attribute specifies the URL in a link?",
            "options": ["A. src", "B. link", "C. href", "D. url"],
            "answer": "C"
        }
    ]

def quiz_game():
    print("=" * 40)
    print("   📝 QUIZ GAME")
    print("=" * 40)
    
    questions = get_questions()
    score = 0
    total = len(questions)
    
    print(f"\n📋 {total} questions across multiple categories.")
    print("Type the letter (A/B/C/D) to answer.\n")
    
    for i, q in enumerate(questions, 1):
        print(f"{'─' * 40}")
        print(f"Q{i}. [{q['category']}] {q['question']}")
        for opt in q['options']:
            print(f"   {opt}")
        
        answer = input("\n👉 Your answer: ").strip().upper()
        
        if answer == q['answer']:
            score += 1
            print("✅ Correct! 🎉")
        else:
            print(f"❌ Wrong! The answer was: {q['answer']}")
        print()
    
    print(f"{'=' * 40}")
    print(f"📊 FINAL SCORE: {score}/{total}")
    percentage = (score / total) * 100
    print(f"📈 Percentage: {percentage:.1f}%")
    
    if percentage == 100:
        print("🏆 Perfect score! You're a genius!")
    elif percentage >= 80:
        print("⭐ Excellent! Very impressive!")
    elif percentage >= 60:
        print("👍 Good job! Keep learning!")
    elif percentage >= 40:
        print("📚 Not bad, but room for improvement!")
    else:
        print("💪 Keep studying, you'll get better!")
    print(f"{'=' * 40}")

if __name__ == "__main__":
    quiz_game()
