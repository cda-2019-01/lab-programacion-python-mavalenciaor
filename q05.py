##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import sys

x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
letters = []
for i in x:
    letters.append(i[0])
uniqueletters = set(letters)

tuples_list = []

for i in sorted(uniqueletters):
    min_val = sys.maxsize
    max_val = - (sys.maxsize - 1)
    for j in x:
        if (i == j[0]):
            val = int(j[1])
            if (val > max_val):
                max_val = val
            if (val < min_val):
                min_val = val
    tuples_list.append((i, max_val, min_val))
for j in tuples_list:
    print("%s,%d,%d" % (j[0], j[1], j[2]))