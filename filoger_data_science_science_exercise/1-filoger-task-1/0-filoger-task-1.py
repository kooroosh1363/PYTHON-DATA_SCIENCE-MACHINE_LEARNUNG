# Counts the number of characters in a text
def counts_char(txt):
    # Returns a dict of chars from txt.
    chars = {}
    for char in txt:
        if char != ' ':
            # Returns a chars dict.
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

# Use this method to enter a English text
user_input = input("Please enter an English text: ")
# Count the number of characters in the input.
character_counts = counts_char(user_input)

# Pretty - prints a request.
print("+-------+-----------+")
print("| NAME  | FREQUENCY |")
print("+=======+===========+")
# Prints a list of characters.
for char, count in character_counts.items():
    print(f"|{char}\t| {count:9d} |")
    print("+-------+-----------+")