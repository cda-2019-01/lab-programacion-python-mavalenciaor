##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]

tabla_regs = []
letters = []

for i in x:
    for j in i[3].split(","):
        tabla_regs.append([j, i[1]])
        letters.append(j)

letters = sorted(set(letters))

for z in range(len(letters)):
    letters[z] = [letters[z], 0]

for k in tabla_regs:
    for l in letters:
        if (k[0] == l[0]):
            l[1] = l[1] + int(k[1])

for m in letters:
    print("%s,%d" %(m[0], m[1]))

