
with open("./Desktop/input.txt") as f:

    data = f.read().strip()
    lines = data.split("\n")


'''
PART 1

sum = 0


for l in lines:

    length = len(l)

    max_first = 0
    max_second = 0

    ind_first = 0

    for i in range(0, length-1):
        
        if (int(l[i]) > max_first):

            max_first = int(l[i])
            ind_first = i

    for i in range(ind_first+1, length):

        if (int(l[i]) > max_second):

            max_second = int(l[i])

    print()
    print(max_first*10 + max_second)

    sum += max_first*10 + max_second

print()
print(sum)
'''

total_sum = 0

for l in lines:

    ind_prev = 0
    sum = ""

    for i in range(11, -1, -1):

        m = 0
        ind_curr = 0

        if (i != 11):
            ind_prev += 1

        for j in range(ind_prev, len(l) - i):

            if (int(l[j]) > m):
                m = int(l[j])
                ind_curr = j

        # print()
        # print("m = {} in range {} to {}".format(m, ind_prev, len(l) - i))
        
        sum += str(m)
        ind_prev = ind_curr
    
    print()
    print(sum)
    total_sum += int(sum)


print()
print(total_sum)



            






