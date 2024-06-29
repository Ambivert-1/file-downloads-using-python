from collections import defaultdict
def count_characters(text):
    char_count=defaultdict(int)
    for char in text:
        char_count[char] += 1

    return char_count

# Ask the user for input
text_input = input("Enter some text: ")

# Call the function with user input
result = count_characters(text_input)

# Print the result
print("Character and their frequency:")
for char, count in result.items():
    print(f"{char}: {count}")

    