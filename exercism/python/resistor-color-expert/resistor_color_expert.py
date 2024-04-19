COLOR_DICT = {
    "black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,
    "green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9,
}
TOLERANCE = {
    "grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%",
    "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%",
}
def resistor_label(colors):
    ohms = (COLOR_DICT[colors[0]] * 10 + COLOR_DICT[colors[1]]) * (10 **  COLOR_DICT[colors[2]])
    tolerance = TOLERANCE.get(colors[3], "")
    if ohms >= 1000000000:
        prefix = "giga"
        ohms //= 1000000000
    elif ohms >= 1000000:
        prefix = "mega"
        ohms //= 1000000
    elif ohms >= 1000:
        prefix = "kilo"
        ohms //= 1000
    else:
        prefix = ""
    return f"{ohms} {prefix}ohms ±{tolerance}"
