##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
letters = []
for i in x:
    letters.append(i[0])
uniqueletters = set(letters)
cant_registros = [(l, letters.count(l)) for l in sorted(uniqueletters)]
for j in cant_registros:
    print("%s,%s" % (j[0],j[1]))