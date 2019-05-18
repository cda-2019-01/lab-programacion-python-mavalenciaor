##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
final = []
index = 0

for i in x:
    final.append([i[0], 0])
    for j in i[4].split(","):
        final[index][1] = final[index][1] + int(j.split(":")[1])
    index = index + 1

for k in final:
    print("%s,%d" %(k[0],k[1]))
