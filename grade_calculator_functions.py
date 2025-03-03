# Function to get student score
def get_student_score():
    # Prompt the user to enter their score
    score = float(input("Enter your score: "))
    return score

# Function to calculate grade based on score
def calculate_grade(score):
    # Determine grade based on score using conditional statements
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

# Main program flow
def main():
    score = get_student_score()  # Get the student's score
    grade = calculate_grade(score)  # Calculate the grade based on the score
    print(f"Your Grade is: {grade}")  # Display the grade

# Run the main program
main()