tea = {
    "G":0,
    "C":0,
    "E":0,
    "P":0,
    "L":0,
    "S":0
}
teas = "a"
while teas != "D":
    teas, num = input().split()
    tea.update({teas:num})
    print(tea)
    
print (tea["G", "C", "E","P", "L", "S"])    