'''
# PART 1

txt = input()
txt = txt.split(",")

sum = 0

for i in txt:

    x = i.split("-")

    y, z = int(x[0]), int(x[1])

    for j in range(y,z+1):

        if (len(str(j)) % 2 != 0):
            continue
        else:
            temp = str(j)
            l = len(str(j))//2
            # 2pt

            pt_l, pt_r = 0, l

            flag = True

            for k in range(0, l):
                if temp[pt_l] != temp[pt_r]:
                    flag = False
                    break
                else:
                    pt_l += 1
                    pt_r += 1
            
            if (flag):
                sum += j


print()
print(sum)

'''

txt = input()
txt = txt.split(",")

sum = 0

for i in txt:

    x = i.split("-")

    y, z = int(x[0]), int(x[1])

    for j in range(y,z+1):

        jj = str(j)
        jj_l = len(jj)

        for k in range(1, jj_l // 2 + 1):

            if jj_l % k == 0:

                match = True

                for kk in range(k, jj_l, k):

                    if (jj[0:k] != jj[kk:kk+k] and kk != 0):

                        match = False
                        break

                if (match == True):

                    print()
                    print(j)
                    sum += j
                    break


print()
print(sum)