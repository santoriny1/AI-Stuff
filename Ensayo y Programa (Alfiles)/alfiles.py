#Simulacion de movimientos que dan solución al problema de los alfiles

#Piezas negras = 1, alfiles blancos = 2, espacios del tablero vacios = 0
tablero = [ [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 2, 2]
            ]
#Funcion que imprime el tablero
def imprimir(movimiento):
    for r in movimiento:
        print (r)

print("TABLERO")
imprimir(tablero)        

print("Primer movimiento ambos lados")
tablero[3][2]=2
tablero[1][1]=1
tablero[4][1]=0
tablero[0][2]=0
imprimir(tablero)

print("Segundo movimiento ambos lados")
tablero[1][3]=2
tablero[3][0]=1
tablero[4][0]=0
tablero[0][3]=0
imprimir(tablero)

print("Tercer movimiento ambos lados")
tablero[3][1]=2
tablero[1][2]=1
tablero[4][2]=0
tablero[0][1]=0
imprimir(tablero)

print("Cuarto movimiento ambos lados")
tablero[1][0]=2
tablero[3][3]=1
tablero[3][2]=0
tablero[1][1]=0
imprimir(tablero)

print("Quinto movimiento ambos lados")
tablero[0][2]=2
tablero[4][1]=1
tablero[1][3]=0
tablero[3][0]=0
imprimir(tablero)

print("Sexto movimiento ambos lados")
tablero[2][0]=2
tablero[2][3]=1
tablero[3][1]=0
tablero[1][2]=0
imprimir(tablero)

print("Septimo movimiento ambos lados")
tablero[2][1]=2
tablero[2][2]=1
tablero[1][0]=0
tablero[3][3]=0
imprimir(tablero)

print("Octavo movimiento ambos lados")
tablero[4][2]=2
tablero[0][1]=1
tablero[2][0]=0
tablero[2][3]=0
imprimir(tablero)

print("Noveno movimiento ambos lados")
tablero[0][3]=2
tablero[4][0]=1
tablero[2][1]=0
tablero[2][2]=0
imprimir(tablero)

print("Decimo movimiento ambos lados")
tablero[2][1]=2
tablero[2][2]=1
tablero[4][3]=0
tablero[0][0]=0
imprimir(tablero)

print("Decimoprimer movimiento ambos lados")
tablero[2][0]=2
tablero[2][3]=1
tablero[0][2]=0
tablero[4][1]=0
imprimir(tablero)

print("Decimosegundo movimiento ambos lados")
tablero[3][0]=2
tablero[1][3]=1
tablero[2][1]=0
tablero[2][2]=0
imprimir(tablero)

print("Decimotercer movimiento ambos lados")
tablero[3][3]=2
tablero[1][0]=1
tablero[4][2]=0
tablero[0][1]=0
imprimir(tablero)

print("Decimocuarto movimiento ambos lados")
tablero[0][0]=2
tablero[4][3]=1
tablero[3][3]=0
tablero[1][0]=0
imprimir(tablero)

print("Decimoquinto movimiento ambos lados")
tablero[1][1]=2
tablero[3][2]=1
tablero[2][0]=0
tablero[2][3]=0
imprimir(tablero)

print("Decimosexto movimiento ambos lados")
tablero[1][2]=2
tablero[3][1]=1
tablero[3][0]=0
tablero[1][3]=0
imprimir(tablero)

print("Decimoseptimo movimiento ambos lados")
tablero[0][2]=2
tablero[4][1]=1
tablero[1][1]=0
tablero[3][2]=0
imprimir(tablero)

print("Decimooctavo movimiento ambos lados")
tablero[0][1]=2
tablero[4][2]=1
tablero[1][2]=0
tablero[3][1]=0
imprimir(tablero)