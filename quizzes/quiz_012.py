def mysteryTwo(a: int, b: int):

    result = a*b+a-b

    return result


out = input("Please enter two numbers split by comma: ")
out = out.split(",")
print(mysteryTwo(a=int(out[0]), b=int(out[1])))
