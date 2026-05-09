def add_item_to_lists(target_list, other_list, item):
    # Your code here
    if target_list == other_list:
        target_list = list(target_list)
    target_list.append(item)
    print(f"Target list: {target_list}")
    print(f"Other list: {other_list}")

a = [1, 2, 3]
b = a
add_item_to_lists(a, b, 99)
