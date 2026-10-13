def calculate_grade(marks):
    try:
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "F"
        print("Grade:", grade)
    except (ValueError, TypeError) as e:
        print("Invalid marks:", e)
calculate_grade(98)