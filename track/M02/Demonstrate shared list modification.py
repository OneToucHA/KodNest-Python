original_scores=[]

for _ in range(3):
    original_scores.append(int(input()))

alias_scores=original_scores

replacement_scores=int(input())
alias_scores[0]=replacement_scores
additional_scores=int(input())
alias_scores.append(additional_scores)

print("original scores",original_scores)
print("alias scores",alias_scores)
print("Shared_Object=",original_scores is alias_scores)