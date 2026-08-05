#Enter number and word
n=int(input("Enter the number: "))
word=input("Enter the word: ")
#print numbers
print("Numbers:")
for i in range(1,n+1):
    print(i)
#print characters
print("characters:")
for j in word:
    print(j) #To print in the same line use end=""
