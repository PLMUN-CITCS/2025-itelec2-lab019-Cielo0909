def get_student_score():
    score = float(input("Enter your score: "))
    return score
def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
def main():
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")  

main()