import numpy as np
found = False
index = 0

with open("inp.txt", "r") as f:
    for line in f:
        q = []
        line = line.replace("\n", "")
        for i in range(len(line)):
            q.append(line[i])
            if(len(q) == 14): #PART ONE JUST WRITE 4
                if np.unique(q).size == len(q):
                    index += i+1
                    found = True
                else:
                    q.pop(0)
            if found:
                found = False
                break
print(index)
