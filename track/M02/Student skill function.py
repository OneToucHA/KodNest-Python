skills=[]
for i in range(5):
    skill=input()
    skills.append(skill)

skill_record=tuple(skills)

print("skill_Record:",skill_record)
print("First Three:",skill_record[0:3])
print("Last Two:",skill_record[-2:])
print("Alternative Skills:",skill_record[::2])
print("Reversed Skills:",skill_record[::-1])