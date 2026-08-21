# === Student Information (First name, Last name, Department) ===
def student_information():
    while True:
        student_first_name = input("Enter your first name: ").strip()
        if student_first_name.isalpha():
            break
        else:
            print("Invalid first name.")

    while True:
        student_last_name = input("Enter your last name: ").strip()
        if student_last_name.isalpha():
            break
        else:
            print("Invalid last name.")

    while True:
        student_department = input("Enter your department: ").strip()
        if student_department.isalpha():
            break
        else:
            print("Invalid department.")

    return student_first_name, student_last_name, student_department


# === Scores ===
def get_score():
    while True:
        student_mathematics_score = input("Mathematics score: ")
        student_english_score = input("English score: ")
        try:
            score_value_m = int(student_mathematics_score)
            score_value_e = int(student_english_score)
        except ValueError:
            print("Enter a valid score")
            continue
        return score_value_m, score_value_e

# === Grade ===
def grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif 0 <= score <= 39:
        return "F"


# === Call-backs ===
first_name, last_name, department = student_information()
math_score, english_score = get_score()

print(f"\nName: {first_name} {last_name}")
print(f"Department: {department}")
print(f"Mathematics: {grade(math_score)}")
print(f"English: {grade(english_score)}")