myname = "hello"
myage = 18
age1 ="30"
is_student = True 
money = 500.75
print(type(myname) , type(myage) , type(is_student) , type(money))

#grade callulate with python
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

# Example usage (remains the same):
student_score = int(input("Enter the student's score: "))
grade = calculate_grade(student_score)
print(f"The student's grade is: {grade}")



