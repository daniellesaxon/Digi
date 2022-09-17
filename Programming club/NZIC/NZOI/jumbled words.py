while True:
    j = []
    s = input()
    if s == "#":
        break
    s = s.split()
    for i in range (len(s)):
        if len(s[i]) == 3 or len(s[i]) == 1:
            j.append(s[i])
        else:
            shuffle = s[i][1:-1]
            shuffle = shuffle[::-1]
            j.append((f"{s[i][0]}{shuffle}{s[i][-1:]}"))
    final = (" ".join(j))
    print(final)