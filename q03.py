##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
letters = []
for i in x:
    letters.append(i[0])
uniqueletters = set(letters)
sum_registros = [[l, 0] for l in sorted(uniqueletters)]

for i in x:
    for j in sum_registros:
        if i[0] == j[0]:
            j[1] = j[1] + int(i[1])
            break

for j in sum_registros:
    print("%s,%s" % (j[0], j[1]))