mathematics_score = 94
english_score = 87
science_score = 79
scores = [mathematics_score, english_score, science_score]
average = sum(scores) / len(scores)
name = input("Enter your full name: ")

print("Name:", name)
print("Mathematics:", mathematics_score)
print("English:", english_score)
print("Average:", float(average))