limit=int(input())
Target=int(input())

count=0
total=0
found=False

for i in range(1,limit+1):
    if i%3==0:
        count=count+1
        total=total+i
        if i==Target:
            found=True
print("Count:",count)
print("Sum:",total)

if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")
        