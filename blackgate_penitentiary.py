line1 = int(input())
criminales = [];
for i in range(0,line1):
    line = str(input())
    line = line.split()
    criminales.append(line)

criminales.sort(key=lambda x: x[1])

posmin = 0
posmax = 0
linea = ""

list_alturas = [];


for cp in criminales:
    if not(cp[1] in list_alturas):
        list_alturas.append(cp[1])


lineas = []
for altura in list_alturas:
    linea = []
    for x in range(0,len(criminales)):
        if criminales[x][1] == altura:
            linea.append(criminales[x][0])
            
    linea.sort()
    lineas.append(linea)
    
n = 0
for linea in lineas:
    pt = ""
    for name in linea:
        pt = pt + " " + name
        n = n + 1
    pt = pt + " " +  str(n-len(linea)+1) + " "+ str(n)
    print(pt)




