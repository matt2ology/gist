"""
In a dictionary you have words (names) and their associated
definitions; however, in Python they are called Keys
(instead of words) and Values (instead of definition).

In Python you are not only limited to just a definition, like you
would in real dictionary, you can also use numbers.
"""

classmates = {"Tanner":"is cool but smells", "Emma":"She sits behind me", "Lucy":"She asks too many questions"}

# All items
print("\n\tAll items")
print(classmates)

# Single item
print("\n\tSingle item")
print(classmates["Emma"])

# Iterate through items
print("\n\tIterate through items")
for key, value in classmates.items():
    print(key + " " + value)

