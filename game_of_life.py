import numpy as np

import hashlib


class tablero_antiguo:
    def  __init__(self,tablero,g):
        self.__tablero = tablero
        self.__g = g 
        #print(self.__tablero)
        
    def __str__(self):
        return str(self.__tablero)
    
    def get_tablero(self):
        return self.__tablero
    
    def get_g(self):
        return self.__g

def gen_hash(my_string):
    sha = hashlib.sha1(my_string)
    return sha.hexdigest()


def vecindario(b):
    """Array de células vivas en el vecindario."""
    vecindario = (
        np.roll(np.roll(b, 1, 1), 1, 0) +  # Abajo-derecha
        np.roll(b, 1, 0) +  # Abajo
        np.roll(np.roll(b, -1, 1), 1, 0) +  # Abajo-izquierda
        np.roll(b, -1, 1) +  # Izquierda
        np.roll(np.roll(b, -1, 1), -1, 0) +  # Arriba-izquierda
        np.roll(b, -1, 0) +  # Arriba
        np.roll(np.roll(b, 1, 1), -1, 0) +  # Arriba-derecha
        np.roll(b, 1, 1)  # Derecha
    )
    return vecindario


def paso(b):
    """Paso en el juego de la vida de Conway."""
    v = vecindario(b)
    buffer_b = b.copy()  # Hacemos una copia de la matriz
    for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if v[i, j] == 3 or (v[i, j] == 2 and buffer_b[i, j]):
                buffer_b[i, j] = 1
            else:
                buffer_b[i, j] = 0
    
    return buffer_b

def printer(tablero):
    for fila in tablero:
        linea = ''
        for item in fila:
            if item == 0:
                linea = linea + '-'
                continue
            linea = linea + '*'
        print(linea)
        
def find_table(dic,dg):
    valores = dic.values()
    for val in valores:
        if val.get_g() == dg:
            return val.get_tablero()
        
        
       



# Parámetros del problema
line = input()
line = line.split()
GENERACIONES = int(line[2])
N = int(line[0])
M = int(line[1])

# Construimos el tablero
tablero = np.zeros((N, M), dtype=int)

for n in range(N):
    linea = input()
    for m in range(M):
        if linea[m] == '*':
            tablero[n][m] = 1;
            
dic = {}
for g in range(GENERACIONES):
    tablero = paso(tablero)
    new_hash = hash(str(tablero))
    if  new_hash in dic.keys():
        item = dic.get(new_hash)
        l_bucle = g - item.get_g()
        restantes = GENERACIONES - g
        bucles_que_caben = int(restantes/l_bucle)
        iteraciones_finales = restantes - bucles_que_caben*l_bucle - 1
        #print(iteraciones_finales)
        tablero = find_table(dic,iteraciones_finales)
        break
    dic[new_hash] = tablero_antiguo(tablero,g)
    
printer(tablero)


