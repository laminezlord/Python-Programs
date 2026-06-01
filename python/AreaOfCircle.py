def area_of_circle(radius):
    pi = 3.14159 # local variable
    area = pi * radius ** 2
    return area

radius = 5 # global variable
print(f"The area of a circle with radius {radius} is: {area_of_circle(radius)}")