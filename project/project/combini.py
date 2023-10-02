def banner_maker(msg:str, space:int, symbol:str)->str:
    # predefine variables we will need
    width = len(msg) + 2*space + 2
    height = 5
    banner = ""
    end_code = "\033[00m"
    green = "\33[0;92m"
    # border-line
    border_line = f"{symbol}"*width
    #middle-line
    middle_line = f"{symbol}" + " "*(width-2) + f"{symbol}"
    #msg_line
    spaces = " "*space
    msg_line = f"{symbol}{spaces}{green}{msg}{end_code}{spaces}{symbol}"

    banner = f"{border_line}\n{middle_line}\n{msg_line}\n{middle_line}\n{border_line}"

    return banner

welcome = banner_maker(msg="Welcome to Conbini", space=25, symbol="$")
print(welcome)
logo = """
         _.-.
       ,'/ //\
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  Combini
"""
print(logo)
#               Menu

items = []
prices = []
with open("database_combini.csv", mode="r") as myfile:
    data=myfile.readlines()
for element in data:
    clear_element=element.strip()
    name,price=clear_element.split(',')
    items.append(name)
    prices.append(int(price))
#                Menu
#1. Onigiri.....................¥500
#2. Bread.......................¥200
print("Menu".center(50))
for it in range(len(items)):
    print(f"{it+1}. {items[it].title().ljust(50,'.')}¥{prices[it]}")

order = []
ordering = True
total = 0
while ordering:
    selection = input(f"Please enter an item (1-{len(items)}):")
    available = ""
    for i in range(len(items)):
        available += str(i+1)

    while not (selection.isdigit() and selection in available):
        selection = input(f"Error, Please enter an item (1-{len(items)}):")
    # add the item and add the price to the total
    order.append(int(selection)-1)
    total += prices[int(selection)-1]

    for it in range(len(items)):
        count = 0
        for o in order:
            if o==it:
                count += 1
        if count > 0:
            total_price = prices[it]*count
            print(f"{items[it].title().ljust(20)}x{count}=¥{total_price}")

    answer = input("In this the last item?(Y/N)")
    while not answer in "yYnN":
        answer = input("Error. Last item?(Y/N)")

    if answer in "yY":
        ordering = False

#print the total, plus tax (10%) inside the frame
print(banner_maker(msg=f"You pay ¥{(total*1.1):.2f}", space=25, symbol="$"))

with open("../sales.csv", mode="a") as myfile: #a means create andadd at the bottom
    myfile.writelines(f"Sale for ¥{(total*1.1):.2f}\n")

#planning, design, development(coding), each 6?