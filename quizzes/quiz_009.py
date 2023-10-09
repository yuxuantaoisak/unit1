def powersten(original):

    units = ["Tera", "Giga", "Mega", "kilo", "unit", "mili", "micro", "nano", "pico"]
    powers = [12, 9, 6, 3, 0, -3, -6, -9, -12]
    output = ""
    for i in range(len(units)):

        if powers[i] >= 0:
            positive = '000 ' * int(powers[i]/3)
            extra = 5 - int(powers[i]/3)
            output += f"{original} {positive}{units[i].rjust(20-powers[i]+extra)}\n"

        elif powers[i] == -6:
            negative_zeros = '000 ' * int(-powers[i] / 3 - 1)
            negative_digits = '00'
            extra = 6 + int(powers[i] / 3)
            output += f"0.{negative_zeros}{negative_digits}{original} {units[i].rjust(20 + powers[i] + extra)}\n"

        else:
            negative_zeros = '000 ' * int(-powers[i]/3-1)
            negative_digits = '00'
            extra = 5 + int(powers[i]/3)
            output += f"0.{negative_zeros}{negative_digits}{original} {units[i].rjust(20+powers[i]+extra)}\n"

    return output


a = int(input("Please enter a number: "))
print(powersten(a))