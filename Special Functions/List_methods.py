# Using Python objects to manipulate a list

# Declare an array named 'numbers' and assign it a list of numbers
numbers = [2, 3, 4, 5, 6, 6, 7]

# Add an object (number) at the end of the list using the 'append' method
numbers.append(8)
print(numbers)  # Output: [2, 3, 4, 5, 6, 6, 7, 8]

# Insert a number (-9) at the beginning of the list using the 'insert' method
numbers.insert(0, -9)
print(numbers)  # Output: [-9, 2, 3, 4, 5, 6, 6, 7, 8]

# Remove the first occurrence of the number 6 from the list using the 'remove' method
numbers.remove(6)
print(numbers)  # Output: [-9, 2, 3, 4, 5, 6, 7, 8]

# Clear all items in the list using the 'clear' method
numbers.clear()
print(numbers)  # Output: []

#check presence of a num in list
num=[32,43,54,45,4,665,65,65]
print(32 in num)

#prints number of elements in list
print(len(num))