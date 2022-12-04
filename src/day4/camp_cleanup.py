def first_part():
    counter = 0
    with open("inp.txt", "r") as f:
        for line in f:
            line = line.replace("-", ",").split(",")
            a, b, c, d = int(line[0]), int(line[1]), int(line[2]), int(line[3])
            if ((a >= c and b <= d) or (a <= c and b >= d)):
                counter += 1
                continue
            if ((c >= a and d <= b) or (c <= a and d >= b)):
                counter += 1
    return counter

def second_part():
    counter = 0
    with open("inp.txt", "r") as g:
        for line in g:
            line = line.replace("-", ",").split(",")
            a, b, c, d = int(line[0]), int(line[1]), int(line[2]), int(line[3])
            if ((a >= c and a <= d) or (b >= c and b <= d)):
                counter += 1
                continue
            if((a <= c and b >= d) or (a >= c and b <= d)):
                counter +=1
    return counter

print(first_part())
print(second_part())
