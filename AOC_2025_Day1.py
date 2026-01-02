
# could prolly sim every iteration as well

# PART 1

curr = 50

lines = []
temp = 0

for i in range(4042):
    l = input()

    x = -1 if l[0] == "L" else 1 
    y = int(l[1:])

    curr += ((x*y))
    curr %= 100

    if (curr == 0):
        temp += 1


print()
print(temp)

    

# PART 2

curr = 50

lines = []
temp = 0

for i in range(2):

    l = input()

    x = -1 if l[0] == "L" else 1 
    y = int(l[1:])
    z = x*y 

    prev_curr = curr

    zz = (prev_curr + z) // 100 - prev_curr // 100 #yeah idk
    temp += abs(zz)

    curr += z
    curr %= 100
    
    if (curr == 0):
        temp += 1

    
print()
print(temp)
