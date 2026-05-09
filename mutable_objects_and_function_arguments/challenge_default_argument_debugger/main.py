def append_item(value, items=None):
    if items is None:
        items = []
    items.append(value)
    print(f"Current items: {items}")

def add_key_value(key, value, mapping=None):
    if mapping is None:
        mapping = {}
    mapping[key] = value
    print(f"Current mapping: {mapping}")

append_item(1)
append_item(2)
add_key_value('a', 10)
add_key_value('b', 20)