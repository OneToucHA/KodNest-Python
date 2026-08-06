number_counts=int(input())
positive_count=0
negative_count=0
zero_count=0
total=0
for i in range(number_counts):
    number=int(input())
    total +=number
    if number>0:
        positive_count=positive_count+1
    elif number<0:
        negative_count=negative_count+1
    else:
        zero_count=zero_count+1
print("positive:",positive_count)
print("negative:",negative_count)
print("zero:",zero_count)
print("Total:",total)