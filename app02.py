

myname = "hello"
myage = 18
age1 = "30"
is_student = True
money = 500.75
print(type(myname), type(myage), type(is_student), type(money))

# grade callulate with python
# def calculate_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"


def calculate_grade(score):
    # Using nested ternary operators
    return "A" if score >= 90 else \
           "B" if score >= 80 else \
           "C" if score >= 70 else \
           "D" if score >= 60 else \
           "F"


# Loop to continuously calculate grades
while True:
    try:
        student_score_input = input(
            "Enter the student's score (or type 'quit' to exit): ")

        if student_score_input.lower() == 'quit':
            print("Exiting the grade calculator. Goodbye!")
            break  # Exit the loop if the user types 'quit'

        student_score = int(student_score_input)  # Convert input to integer

        # Basic validation for score range (optional but good practice)
        if 0 <= student_score <= 100:
            grade = calculate_grade(student_score)
            print(f"The student's grade is: {grade}")
        else:
            print("Invalid score. Please enter a score between 0 and 100.")

    except ValueError:
        # Handle cases where the input is not a valid number (and not 'quit')
        print("Invalid input. Please enter a number for the score or 'quit'.")

    print("-" * 20)  # Separator for clarity
