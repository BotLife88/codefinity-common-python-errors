numbers = [10, 20, 30, 40, 50, 60]

# Print all numbers using a loop (currently skips the last number)
for i in range(len(numbers)):
    print(f"Number: {numbers[i]}")

# Get the middle numbers (currently excludes too many elements)
middle_numbers = numbers[1:-1]
print(f"Middle numbers: {middle_numbers}")
