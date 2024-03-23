def equilateral(sides):
    is_triangle = side1 + side2 > side3 and side2 + side3 >side1 and side1 + side3 > side2 and side1 > 0 and side2 > 0 and side3 > 0
    is_equilateral = side1 == side2 == side3
    return is_triangle and is_equilateral


def isosceles(sides):
    side1, side2, side3 = sides
    is_triangle = side1 + side2 > side3 and side2 + side3 >side1 and side1 + side3 > side2 and side1 > 0 and side2 > 0 and side3 > 0
    is_isosceles = side1 == side2 or side1 == side3 or side2 == side3
    return is_triangle and is_isosceles

def scalene(sides):
    side1, side2, side3 = sides
    is_triangle = side1 + side2 > side3 and side2 + side3 >side1 and side1 + side3 > side2 and side1 > 0 and side2 > 0 and side3 > 0
    is_scalene = side1 != side2 and side2 != side3 and side1 != side3
    return is_triangle and is_scalene
