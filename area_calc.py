import math

def paint_calc(height, width, coverage):
    number_of_cans = height * width / coverage
    return math.ceil(number_of_cans)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(paint_calc(height=test_h, width=test_w, coverage=coverage))