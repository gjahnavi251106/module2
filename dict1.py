students = {
    "Rishika": 85,
    "Sreedha": 92,
    "Priya": 78,
    "janu": 95,
    "Anusha": 88
}

highest = max(students, key=students.get)

print("Highest Scoring Student:", highest)
print("Marks:", students[highest])