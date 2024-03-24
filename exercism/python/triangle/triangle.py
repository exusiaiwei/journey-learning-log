def is_valid(sides):
    return all(s != 0 and 2 * s < sum(sides) for s in sides)

def equilateral(sides):
    return is_valid(sides) and len(set(sides)) == 1
def isosceles(sides):
    return is_valid(sides) and len(set(sides)) < 3
def scalene(sides):
    return is_valid(sides) and len(set(sides)) == 3