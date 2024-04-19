COLOR_DICT = {
    "black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,
    "green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9,
}
def label(colors):
    ohms = (COLOR_DICT[colors[0]] * 10 + COLOR_DICT[colors[1]]) * (10 **  COLOR_DICT[colors[2]])
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
    return f"{int(value)} {prefix}ohms"