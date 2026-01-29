def get_formatted_numbers(number):
    width = len(bin(number)[2:])
    result = []

    for i in range(1, number + 1):
        d = "{:>{w}}".format(i, w=width)
        o = "{:>{w}o}".format(i, w=width)
        h = "{:>{w}X}".format(i, w=width)
        b = "{:>{w}b}".format(i, w=width)
        result.append(f"{d} {o} {h} {b}")

    return result
