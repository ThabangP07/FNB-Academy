from rectangle import calculate_area, perimeter

length = int(input("Please enter a length: "))
width = int(input("Please enter a width: "))

area = calculate_area(length, width)
perimeter_value = perimeter(length, width)

print(f"The rectangle has an area of {area} in square units")
print(f"The rectangle has a perimeter of {perimeter_value} in units")