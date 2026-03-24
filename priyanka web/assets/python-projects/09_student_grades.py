"""
🎓 Student Grade Manager
Manage student records, calculate grades, and generate report cards.
Author: Priyanka
"""

def get_grade(percentage):
    if percentage >= 90:
        return 'A+', '🏆 Outstanding!'
    elif percentage >= 80:
        return 'A', '⭐ Excellent!'
    elif percentage >= 70:
        return 'B+', '👍 Very Good!'
    elif percentage >= 60:
        return 'B', '✅ Good'
    elif percentage >= 50:
        return 'C', '📚 Average'
    elif percentage >= 35:
        return 'D', '⚠️ Below Average'
    else:
        return 'F', '❌ Fail'

def add_student(students):
    name = input("\n👤 Student name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    subjects = {}
    print("📝 Enter marks for each subject (type 'done' to finish):")
    
    while True:
        subject = input("   Subject name: ").strip()
        if subject.lower() == 'done':
            break
        if not subject:
            continue
        
        try:
            marks = float(input(f"   Marks in {subject} (0-100): "))
            marks = max(0, min(100, marks))
            subjects[subject] = marks
        except ValueError:
            print("   ❌ Invalid marks!")
    
    if subjects:
        students[name] = subjects
        print(f"✅ Added {name} with {len(subjects)} subjects!")
    else:
        print("❌ No subjects added!")

def view_report(students):
    if not students:
        print("\n📭 No students added yet!")
        return
    
    print(f"\n{'=' * 55}")
    print("   🎓 STUDENT REPORT CARDS")
    print(f"{'=' * 55}")
    
    for name, subjects in students.items():
        total = sum(subjects.values())
        count = len(subjects)
        avg = total / count
        grade, remark = get_grade(avg)
        
        print(f"\n┌{'─' * 50}┐")
        print(f"│  👤 Student: {name:<36}│")
        print(f"├{'─' * 50}┤")
        
        for subj, marks in subjects.items():
            subj_grade, _ = get_grade(marks)
            bar = "█" * int(marks / 5)
            print(f"│  {subj:<15} {marks:>6.1f}  [{subj_grade}]  {bar:<20}│")
        
        print(f"├{'─' * 50}┤")
        print(f"│  📊 Total: {total:.1f}/{count * 100}                          │")
        print(f"│  📈 Average: {avg:.1f}%                             │")
        print(f"│  🎖️ Grade: {grade}  {remark:<28}│")
        print(f"└{'─' * 50}┘")

def class_statistics(students):
    if not students:
        print("\n📭 No students!")
        return
    
    averages = []
    for name, subjects in students.items():
        avg = sum(subjects.values()) / len(subjects)
        averages.append((name, avg))
    
    averages.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\n{'=' * 40}")
    print("   📊 CLASS STATISTICS")
    print(f"{'=' * 40}")
    print(f"\n   Total students: {len(students)}")
    print(f"   Class average:  {sum(a for _, a in averages) / len(averages):.1f}%")
    print(f"   Highest:        {averages[0][0]} ({averages[0][1]:.1f}%)")
    print(f"   Lowest:         {averages[-1][0]} ({averages[-1][1]:.1f}%)")
    
    print(f"\n   🏆 Rankings:")
    for i, (name, avg) in enumerate(averages, 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f" {i}."
        print(f"      {medal} {name}: {avg:.1f}%")

def grade_manager():
    print("=" * 40)
    print("   🎓 STUDENT GRADE MANAGER")
    print("=" * 40)
    
    students = {}
    
    while True:
        print("\n📂 Menu:")
        print("1. Add student")
        print("2. View report cards")
        print("3. Class statistics")
        print("4. Exit")
        
        choice = input("\n👉 Choose (1-4): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_report(students)
        elif choice == '3':
            class_statistics(students)
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    grade_manager()
