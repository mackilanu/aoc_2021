data = open('data.in', 'r').readlines()

def solve():
    hor, ver, aim = 0, 0, 0
    for r in data:
        d, a = r.split()
        if d == 'up':
            aim -= int(a)
        elif d == 'down':
            aim += int(a)
        else:
            hor += int(a)
            ver += (aim * int(a))
    return hor * ver

print("Result: " + str(solve()))
