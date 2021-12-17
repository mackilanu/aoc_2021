data = open('data.in', 'r').readlines()

def solve():
    res = 0
    for i in range(len(data)):
        if i > 0:
            if int(data[i]) > int(data[i-1]):
                res += 1
    return res

print("Result: " + str(solve()))
