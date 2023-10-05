def banner_maker(msg: str, space: int, symbol: str) -> str:
    # predefine variables we will need
    width = len(msg) + 2 * space + 2
    height = 5
    banner = ""
    end_code = "\033[00m"
    green = "\33[0;92m"
    # border-line
    border_line = f"{symbol}" * width
    # middle-line
    middle_line = f"{symbol}" + " " * (width - 2) + f"{symbol}"
    # msg_line
    spaces = " " * space
    msg_line = f"{symbol}{spaces}{green}{msg}{end_code}{spaces}{symbol}"
    banner = f"{border_line}\n{middle_line}\n{msg_line}\n{middle_line}\n{border_line}"

    return banner


def print_menu(menu):
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")


def validate_int_user(msg, menu):
    option = input(msg)
    while not option.isdigit():
        print("Error")
        print_menu(menu)
        option = input(msg)
    return int(option)
