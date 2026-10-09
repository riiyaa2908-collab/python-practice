# Text Analyzer

filename = input("Enter the name of the text file: ")

with open(filename, "r") as file:
    text = file.read()

# Convert text to lowercase
text = text.lower()

# Remove common punctuation
for symbol in ",.!?;:":
    text = text.replace(symbol, "")

# Split text into words
words = text.split()

# Count total words
print("Total words:", len(words))

# Count frequency of each word
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display word frequency
print("\nWord frequency:")

for word, count in word_count.items():
    print(f"{word}: {count}")
