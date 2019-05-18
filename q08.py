##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
d = set([i[1] for i in x])
e = []

for i in sorted(d):
    e.append([i, []])

tuples_list = []

for j in e:
    for k in x:
        if (j[0] == k[1]):
            #if (k[0] not in j[1]):
            j[1].append(k[0])
    tuples_list.append((j[0], j[1]))

aux_tuples_list = []
for i in tuples_list:
    aux_tuples_list.append((i[0], sorted(i[1])))

for l in aux_tuples_list:
    print(l)
