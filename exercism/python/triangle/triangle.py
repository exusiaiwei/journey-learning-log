def is_valid(sides):
    side1 = sides[0]
    side2 = sides[1] 
    side3 = sides[2]

    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2: 
        if side1 > 0 and side2 > 0 and side3 > 0:
            return True
    return False

def equilateral(sides):
    return is_valid(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_valid(sides) and len(set(sides)) < 3

def scalene(sides):
    return is_valid(sides) and len(set(sides)) == 3
