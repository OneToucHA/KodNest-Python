# Read the number of words
n = int(input())

# Dictionary to store each word and its frequency
word_frequency = {}

# Read and count the words
for _ in range(n):
    word = input().strip()
    # Update the frequency of the word
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Print each unique word and its frequency
for word, count in word_frequency.items():
    # Print the word and count separated by a space
    print(f"{word} {count}")