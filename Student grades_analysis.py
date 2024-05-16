def analyze_grades(students, threshold):
    # Initialize dictionaries and variables to store the results
    average_grades = {}
    highest_average = 0
    highest_average_student = ""
    
    # Calculate the average grade for each student
    for student, grades in students.items():
        avg_grade = sum(grades) / len(grades)
        average_grades[student] = avg_grade
        
        # Check for the highest average grade
        if avg_grade > highest_average:
            highest_average = avg_grade
            highest_average_student = student
    
    # Print the average grade for each student
    print("Average grades per student:")
    for student, avg_grade in average_grades.items():
        print(f"{student}: {avg_grade:.2f}")
    
    # Print the student with the highest average grade
    print("\nHighest Average Grade:")
    print(f"{highest_average_student}: {highest_average:.2f}")
    
    # Print the names of students with average grades above the threshold
    print("\nStudents with average grades above", threshold, ":")
    for student, avg_grade in average_grades.items():
        if avg_grade > threshold:
            print(student)

# Sample input
students = {
    "Mark": [88, 76, 92, 85],
    "James": [70, 80, 79, 92],
    "John": [80, 70, 65, 90],
    "Kimberly": [92, 76, 88, 90]
}

# Threshold for average grades
threshold = 85

# Run the analysis
analyze_grades(students, threshold)
