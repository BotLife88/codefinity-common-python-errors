def process_numbers(numbers):
    for n in numbers:
        if n > 0:
            print("Positive:", n)
        if n % 2 == 0:
            print("  Even number")
        else:
            print("  Odd number")
        if n == 0:
            print("Zero found")
        else:
            print("Negative:", n)
    print("Done processing numbers.")

process_numbers([3, -1, 0, 4, -5])
