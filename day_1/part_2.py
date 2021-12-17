data = open('data.in', 'r').readlines()

def solve():
    res, prev = -1, 0
    for i in range(len(data) - 2):
        t = 0
        for j in range(3):
            t += int(data[i+j])
        if t > prev:
            res += 1
        prev = t
    return res

print("Result: " + str(solve()))
