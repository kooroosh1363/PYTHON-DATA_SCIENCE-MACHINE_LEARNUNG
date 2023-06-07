# PrettyTable imports prettytable.
from prettytable import PrettyTable
# Use this method to enter a English text
user_input = input("Please enter an English text: ")
# Pretty table for pretty table.
table = PrettyTable(["NAME", "FREQUENCY"])
# Add a row to the user input table.
[table.add_row([char, user_input.count(char)]) for char in set(user_input) if char != ' ']
# Print a table to stdout
print(table)