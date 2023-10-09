def blackboxthree(given):
    given = given.lower()
    counts = []
    for x in range(26):
        counts.append(0)
    alpa = 'abcdefghijklmnopqrstuvwxyz'
    output = ""
    for letter in given:
        if letter == " ":
            output += " "
        for i in range(25):

            if letter == alpa[i]:
                counts[i] += 1
                output += str(counts[i])

    return output

a = str(input("Please enter the message: "))
b = blackboxthree(a)
print(b)
