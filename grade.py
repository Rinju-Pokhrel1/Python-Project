
# Function to get the average score of a student
def get_average_score(scores):
    # Compute the sum of scores
    total = sum(scores)

    # Get the number of subjects
    subject_count = len(scores)
    
    # Compute the average score
    average_score = total / subject_count
    
    return average_score

# Function to compute the grade based on the average score
def compute_grade(average_score):
    if average_score >= 80.0:
        grade = "A"
    elif average_score >= 60.0:
        grade = "B"
    elif average_score >= 50.0:
        grade = "C"
    else:
        grade = "F"
    
    return grade

# Student scores
student_scores = [55, 64, 75, 80, 65]

# Compute the average score
average_score = get_average_score(student_scores)

# Compute the grade
grade = compute_grade(average_score)

# Print the results
print(f"Average Score: {average_score}")
print(f"Grade: {grade}")
