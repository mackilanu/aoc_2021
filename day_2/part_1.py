data = open('data.in', 'r').readlines()

def solve():
    hor, ver = 0, 0
    for r in data:
        d, a = r.split()
        if d == 'forward':
            hor += int(a)
        elif d == 'up':
            ver -= int(a)
        else:
            ver += int(a)
    return hor * ver

print("Result: " + str(solve()))
