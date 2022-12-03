letters = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = 0

def first_part():
    count = 0
    with open("inp.txt", "r") as f:
        inpt = f.read().split('\n')
        for i in inpt:
            a = i[len(i)//2:]
            b = i[:len(i)//2]
            temp = set(a).intersection(set(b))
            for j in temp:
                count += letters.find(j)
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

print(first_part())
print(second_part())
