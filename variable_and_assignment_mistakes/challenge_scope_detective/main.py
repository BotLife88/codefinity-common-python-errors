counter = 0
message = "Hello, Detective!"

def increment_counter():
    global counter
    counter += 1

def print_message():
    print(message)

increment_counter()
print(counter)
print_message()