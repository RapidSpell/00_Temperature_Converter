def round_ans(val):
    """
    Rounds temperature to nearest degree
    :param val: number to be rounded
    :return: number rounded to the nearest degree
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from Fahrenheit to Celsius
    :param to_convert: temperature to be converted in Fahrenheit
    :return:  converted temperature in Celsius
    """
    answer = (to_convert - 32) * 5 / 9
    return round(answer)


def to_fahrenheit(to_convert):
    """
    Converts from Celsius to Fahrenheit
    :param to_convert: temperature to be converted in Celsius
    :return: converted temperature in Fahrenheit
    """
    answer = to_convert * 1.8 + 32
    return round(answer)


# Main Routine / Testing starts here
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]
#
# for item in to_f_test:
#     ans = to_fahrenheit(item)
#     print(f"{item} C is {ans} F")
#
# print()
#
# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item} F is {ans} C")
