x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
sumcol = 0
for i in x:
    sumcol = sumcol + int(i[1])
print(sumcol)
