import random

def crear_tablero_vacio():
    tablero = []
    fila = ["__"]*8
    for f in range(8):
        tablero.append(fila.copy())
    return tablero
    

def fichas(tablero, cantidad_maxima, pieza):
    
    for f in range(random.randrange(cantidad_maxima+1)):
        fi, co = random.randrange(8), random.randrange(8)
        tablero[fi][co]=pieza
    return tablero

def mostrar_tablero(tablero):
    for f in tablero:
        print(f)

def calcular_puntaje(tablero, color):
    suma_valores = 0
    for fila in tablero:
        for casilla in fila:
            if casilla[1] == color:
                suma_valores += valor_piezas[casilla[0]]
    return suma_valores
        
        
def hay_jaque(tablero,fila, columna, color):
    cuantos = 0
    for fi in range(fila-1,fila+2):
        for co in range(columna-1, columna+2):
            if tablero[fi][co][1] == color:
                cuantos +=1
    return cuantos
                
            

valor_piezas = {"p":1, "c":3, "a":3, "t":5, "d":9, "R":4}

tablero = crear_tablero_vacio()

#Peones
tablero=fichas(tablero,8,"pB")
tablero=fichas(tablero,8,"pN")

#Caballos
tablero=fichas(tablero,2,"cB")
tablero=fichas(tablero,2,"cN")

#Alfiles
tablero=fichas(tablero,2,"aB")
tablero=fichas(tablero,2,"aN")

#Torres
tablero=fichas(tablero,2,"tB")
tablero=fichas(tablero,2,"tN")

#Damas
tablero=fichas(tablero,1,"dB")
tablero=fichas(tablero,1,"dN")

#El Rey negro simpre en la misma posicion, al igual que el blanco
tablero[1][4]="RN"
tablero[6][4]="RB"

puntaje_blancas = calcular_puntaje(tablero,"B")
puntaje_negras = calcular_puntaje(tablero,"N")
print("Puntaje de las Blancas:", puntaje_blancas)
print("Puntaje de las Negras:", puntaje_negras)
print()

#Verifico cuantas piesas Blancas rodean al Rey Negro
jaque_de_blancas = hay_jaque(tablero,1,4,"B")

#Verifico cuantas piesas Negras rodean al Rey Blanco
jaque_de_negras = hay_jaque(tablero,6,4,"N")

if jaque_de_blancas >= 3:
    print("El Rey Negro está en jaque")

if jaque_de_negras >= 3:
    print("El Rey Blanco está en jaque")
    
print()
print()

mostrar_tablero(tablero)
