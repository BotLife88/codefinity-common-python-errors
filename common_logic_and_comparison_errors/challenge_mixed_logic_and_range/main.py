def filter_and_label(numbers):
    result = []
    for n in numbers:
        if n >= 10 and n <= 20:
            label = "in range"
        else:
            label = "out of range"
        result.append((n, label))
    return result

# Example calls
print(filter_and_label([9, 10, 15, 20, 21]))
print(filter_and_label([10, 11, 19, 20]))
