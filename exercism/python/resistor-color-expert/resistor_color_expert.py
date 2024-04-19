COLOR_DICT = {
    "black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,
    "green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9,
}
TOLERANCE = {
    "grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%",
    "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%",
}
def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    if len(colors) == 4:
        ohms = (COLOR_DICT[colors[0]] * 10 + COLOR_DICT[colors[1]]) * (10 **  COLOR_DICT[colors[2]])
        tolerance = TOLERANCE.get(colors[3], "")
    if len(colors) == 5:
        ohms = (COLOR_DICT[colors[0]] * 100 + COLOR_DICT[colors[1]] * 10 + COLOR_DICT[colors[2]]) * (10 **  COLOR_DICT[colors[3]])
        tolerance = TOLERANCE.get(colors[4], "")
    if ohms >= 1e9:
        prefix = "giga"
        value = ohms / 1e9
    elif ohms >= 1e6:
        prefix = "mega"
        value = ohms / 1e6
    elif ohms >= 1e3:
        prefix = "kilo"
        value = ohms / 1e3
    else:
        prefix = ""
        value = ohms
    if value == int(value):
        return f"{int(value)} {prefix}ohms ±{tolerance}"
    else:
        return f"{value} {prefix}ohms ±{tolerance}"
