"""
SETS will not list/show duplicate items
"""

groceries = {"cereal", "milk", "beer", "eye of newt", "beer"}

print(groceries)

if "milk" in groceries:
    print("You got milk!")
else:
    print("Oh, yeah! YOU NEED MILK!")

