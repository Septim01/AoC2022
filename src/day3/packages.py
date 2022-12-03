letters = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = 0

def first_part(line):
    found = False
    count = 0
    if line.find('\n'):
        line = line[0:len(line) - 1]
    size = len(line)
    for i in range(0, size):
        if i < size / 2:
            a.append(line[i])
            continue
        b.append(line[i])
    for x in a:
        if found:
            break
        for y in b:
            if x == y:
                count += letters.find(x)
                found = True
                break
    found = False
    return count


def second_part():
    count = 0
    with open("inp.txt", "r") as g:
        inpt = g.read().split('\n')
        for i in range(0, len(inpt), 3):
            temp = set(inpt[i]).intersection(set(inpt[i + 1])).intersection(set(inpt[i + 2]))
            for j in temp:
                count += letters.find(j)
    return count
with open("inp.txt", "r") as f:
    for line in f:
        a = []
        b = []
        x += first_part(line)
print(x)
print(second_part())
