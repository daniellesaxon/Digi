problems = {
    "L":120,
    "S":150,
    "B":150,
    "N":40,
    "C":160,
    "D":100,
    "R":100,
    "O":100,
}
all = {}

while True:
    p = {}
    fn = input()
    if fn !="#":
        all[fn] = 0
    if fn == "#":
        break
    while True:
        i = input()
        if i == "00A":
            break
        s, c = i.split()
        if c in problems:
            x = int(problems.get(c)) 
            if s not in p:
                p[s] = x
            else:
                p[s] = p[s] +x

            if p[s] >= 200:
                if fn in all:
                    all[fn] +=1
                else:
                    all[fn] = 1
for item in all:
    x = int(all.get(item))
    print(f"{item} {x}")