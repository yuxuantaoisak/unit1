days = ["Fr", "Sa", "Su", "Mo", "Tu", "We", "Th"]
count = 0
out = ""
# december
for i in range(1, 32):

    out += f"{days[count]} {i}    "
    count = count+1

    if count > 6:
        count = 0

print(out)
