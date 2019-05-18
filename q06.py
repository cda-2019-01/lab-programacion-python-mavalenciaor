##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
import sys

x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
a = []
c = []
for i in x:
    a.append(i[4].split(","))
for j in a:
    for k in j:
        b = k.split(":")
        c.append([b[0], b[1]])
#print(c)

tuples_list = []
keys = [l[0] for l in c]

uniquekeys = set(keys)
tuples_list = []

for i in sorted(uniquekeys):
    min_val = sys.maxsize
    max_val = - (sys.maxsize - 1)
    for j in c:
        if (i == j[0]):
            val = int(j[1])
            if (val > max_val):
                max_val = val
            if (val < min_val):
                min_val = val
    tuples_list.append((i, max_val, min_val))
for k in tuples_list:
    print("%s,%d,%d" %(k[0],k[2],k[1]))