##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]

tabla_regs = []

for i in x:
    tabla_regs.append([i[0], len(i[3].split(",")), len(i[4].split(","))])

for j in tabla_regs:
    print("%s,%d,%d" %(j[0],j[1],j[2]))

