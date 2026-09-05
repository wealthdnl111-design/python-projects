# List of numbers
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    # squares.append(number * number)
    squares = [number * number for number in numbers]
    print(squares)

print("==================================================")

# Another example of list comprehension
numbers_2 = [1, 2, 3, 4, 5]
doubled = [number2 * number2 * 2 for number2 in numbers_2]
print(doubled)

print("==================================================")

# List comprehension using strings
# names = ["Wealth", "Daniel", "Ebube", "Amaka"]
# names_upper = [name.upper() for name in names]
# print(names_upper)
# length = [len(name) for name in names]
# print(length)

# Converting from upper to lower
names = ["WEALTH", "DANIEL", "EBUBE", "AMAKA"]
names_lower = [name.lower() for name in names]
print(names_lower)

# Filtering of words using 'if'
filter_names = [name for name in names if len(name) > 5]
print(filter_names)