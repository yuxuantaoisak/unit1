def multable(num):
    out = ""
    for i in range(1,10):
        if num*i >= 10:
            out += f"{num}  x  {i}  = {num*i}\n"
        else:
            out += f"{num}  x  {i}  =  {num*i}\n"

    return out

a = int(input("Please enter a number for the multiplication table: "))
print(multable(a))