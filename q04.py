##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
months = []
for i in x:
    months.append(int(i[2].split("-")[1]))
    #months.append(i[2].split("-")[1])
uniquemonths = set(months)
[(m, months.count(m)) for m in uniquemonths]
regs_por_mes = [(m, months.count(m)) for m in sorted(uniquemonths)]
for i in regs_por_mes:
    if i[0] < 10:
        print("0%s,%d" % (i[0], i[1]))
    else:
        print("%s,%d" % (i[0], i[1]))