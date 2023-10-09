def open_doors(num_stu):

    switch = [0, 0, 0, 0, 0]

    for i in range(1, num_stu + 1):
        for d in range(i - 1, 5, i):
            switch[d] = 1 - switch[d]
    return switch

result = sum(open_doors(5))
print(result)