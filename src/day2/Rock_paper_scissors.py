tmp = []
win, draw, loss, x, y = 6, 3, 0, 0, 0

def compare_first_part(arr):
    score = 0
    if arr[0] == "A":
        if arr[1] == "X":
            score += draw + 1
        elif arr[1] == "Y":
            score += win + 2
        elif arr[1] == "Z":
            score += loss + 3
    elif arr[0] == "B":
        if arr[1] == "X":
            score += loss + 1
        elif arr[1] == "Y":
            score += draw + 2
        elif arr[1] == "Z":
            score += win + 3
    elif arr[0] == "C":
        if arr[1] == "X":
            score += win + 1
        elif arr[1] == "Y":
            score += loss + 2
        elif arr[1] == "Z":
            score += draw + 3
    return score


def compare_second_part(arr):
    score = 0
    if arr[0] == "A":
        if arr[1] == "X":
            score += loss + 3
        elif arr[1] == "Y":
            score += draw + 1
        elif arr[1] == "Z":
            score += win + 2
    elif arr[0] == "B":
        if arr[1] == "X":
            score += loss + 1
        elif arr[1] == "Y":
            score += draw + 2
        elif arr[1] == "Z":
            score += win + 3
    elif arr[0] == "C":
        if arr[1] == "X":
            score += loss + 2
        elif arr[1] == "Y":
            score += draw + 3
        elif arr[1] == "Z":
            score += win + 1
    return score

with open("inp.txt", "r") as f:
    for line in f:
        tmp.append(line[0])
        tmp.append(line[2])
        x += compare_first_part(tmp)
        y += compare_second_part(tmp)
        tmp = []

print(x, y)
