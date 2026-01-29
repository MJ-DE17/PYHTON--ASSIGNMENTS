def generate_logo(thickness):
    c = 'H'
    result = []

    for i in range(thickness):
        result.append((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

    for i in range(thickness+1):
        result.append((c*thickness).center(thickness*2) +
                      (c*thickness).center(thickness*6))

    for i in range((thickness+1)//2):
        result.append((c*thickness*5).center(thickness*6))

    for i in range(thickness+1):
        result.append((c*thickness).center(thickness*2) +
                      (c*thickness).center(thickness*6))

    for i in range(thickness):
        result.append(
            ((c*(thickness-i-1)).rjust(thickness) + c +
             (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
        )

    return result
