def rectangle_area(width, height):
    area = width * height
    return area

def print_summary():
    width = 5
    height = 10
    area = rectangle_area(width, height)
    print("Rectangle: width={}, height={}, area={}".format(width, height, area))

print_summary()