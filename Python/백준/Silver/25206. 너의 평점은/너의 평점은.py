sum_score = 0
sum_credit = 0

for _ in range(20):
    line = input().split()
    if not line: break
    name, credit, grade = line
    credit = float(credit)
    
    if grade == "P":
        continue
        
    grade_point = 0
    if grade == "A+": grade_point = 4.5
    elif grade == "A0": grade_point = 4.0
    elif grade == "B+": grade_point = 3.5
    elif grade == "B0": grade_point = 3.0
    elif grade == "C+": grade_point = 2.5
    elif grade == "C0": grade_point = 2.0
    elif grade == "D+": grade_point = 1.5
    elif grade == "D0": grade_point = 1.0
    elif grade == "F": grade_point = 0.0
    
    sum_score += (credit * grade_point)
    sum_credit += credit

print(sum_score / sum_credit)