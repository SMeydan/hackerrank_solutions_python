import math
ab, bc = int(input()), int(input())
ac = math.sqrt((pow(ab, 2) + pow(bc, 2)))
cosc = pow(bc, 2) / (bc*ac)
angle_radians = math.acos(cosc)
angle_degrees = math.degrees(angle_radians)
print(str(round(angle_degrees)) + u"\u00B0")
