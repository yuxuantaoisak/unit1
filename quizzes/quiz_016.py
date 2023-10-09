def avelen(word: list):

    word = word.split(",")

    sum = 0
    for i in range(len(word)):
        position = word[i].strip()
        sum += len(position)
        ave = sum/len(word)

    if len(word) == 0:
        return 0
    else:
        return ave

a = input("Please enter a list of words split by comma: ")
print(avelen(a))