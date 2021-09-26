import math
import matplotlib
import matplotlib.pyplot as plt


import LIbComp as lc
import LIbEspVect as lE

#quitar el (#) para usar los ejercicios

def estados(m,v,clk):
    for i in range (clk):
        v = lE.accionMacVec(m,v)
    return v

def dobleRendija(numoRen,numBlan,clk):
    tam = 7
    ren = numoRen
    blan = numBlan
    zeros = 2
    if numoRen > 2 or numBlan > 3:
        numoRen = numoRen - 2 
        tam = numoRen * 3 + tam
        zeros = numoRen * 2 + zeros
        numBlan = numBlan - 3
        tam = tam + numBlan
    matriz = [[(0,0) for i in range (-1,tam)] for i in range (-1,tam)] 
    for i in range (0,tam+1):
        for j in range (0,tam+1):
            if i == 0 and 0 < j < ren+1:
                matriz[i][j] = (1/ren,0)
            elif 0 < i <= ren:
                if i == 1 and 2 * (ren-2) + 2 - (ren-2) < j < 2 * (ren-2) + blan + 3 - (ren-2):
                    matriz[i][j] = (1/blan,0)
                if i == 2 and 2 * (ren-2) + 4 - (ren-2) < j < 2 * (ren-2) + blan + 5 - (ren-2) and ren >= 2:
                    matriz[i][j] = (1/blan,0)
                if i == 3 and 2 * (ren-2) + 6 - (ren-2) < j < 2 * (ren-2) + blan + 7 - (ren-2) and ren >= 3:
                    matriz[i][j] = (1/blan,0)
                if i == 4 and 2 * (ren-2) + 8 - (ren-2) < j < 2 * (ren-1) + blan + 9 - (ren-2) and ren >= 4:
                    matriz[i][j] = (1/blan,0)
            elif i > ren and j == i:
                matriz[i][j] = (1,0)
    m = lE.transpuesta(matriz)
    for i in range (clk):
        s = lE.producMat(m,m)
    return s

def dobleRendijaCuantico(numoRen,numBlan,clk):
    xRen = math.sqrt(2 * numoRen)
    xBlan = math.sqrt(2 * numBlan)
    tam = 7
    ren = numoRen
    blan = numBlan
    zeros = 2
    if numoRen > 2 or numBlan > 3:
        numoRen = numoRen - 2 
        tam = numoRen * 3 + tam
        zeros = numoRen * 2 + zeros
        numBlan = numBlan - 3
        tam = tam + numBlan
    matriz = [[(0,0) for i in range (-1,tam)] for i in range (-1,tam)] 
    for i in range (0,tam+1):
        for j in range (0,tam+1):
            if i == 0 and 0 < j < ren+1:
                matriz[i][j] = (1/xRen((-1)**j/2),(1/xRen)*((-1)**j))
            elif 0 < i <= ren:
                if i == 1 and 2 * (ren-2) + 2 - (ren-2) < j < 2 * (ren-2) + blan + 3 - (ren-2):
                    matriz[i][j] = ((1/xBlan)*((-1)**(j/2)),(1/xBlan)*((-1)**j))
                if i == 2 and 2 * (ren-2) + 4 - (ren-2) < j < 2 * (ren-2) + blan + 5 - (ren-2) and ren >= 2:
                    matriz[i][j] = ((1/xBlan)*((-1)**(j/2)),(1/xBlan)*((-1)**j))
                if i == 3 and 2 * (ren-2) + 6 - (ren-2) < j < 2 * (ren-2) + blan + 7 - (ren-2) and ren >= 3:
                    matriz[i][j] = ((1/xBlan)*((-1)**(j/2)),(1/xBlan)*((-1)**j))
                if i == 4 and 2 * (ren-2) + 8 - (ren-2) < j < 2 * (ren-1) + blan + 9 - (ren-2) and ren >= 4:
                    matriz[i][j] = ((1/xBlan)*((-1)**(j/2)),(1/xBlan)*((-1)**j))
            elif i > ren and j == i:
                matriz[i][j] = (1,0)
    m = lE.transpuesta(matriz)
    for i in range (clk):
        s = lE.producMat(m,m)
    return s

def diagramaEstados(v):
    eje_x = v
    eje_y = [0,1]
    plt.bar(eje_x, eje_y)
    plt.show()


#if __name__ == '__main__':
#ejercicio 3.1.3 (experimento con cualquier matriz),(5,0),(3,0),(10,0)
    m_313 = [[(0,0),(1/6,0),(5/6,0)],
             [(1/3,0),(1/2,0),(1/6,0)],
             [(2/3,0),(1/3,0),(0,0)]]
    v_313 =  [(1/6,0),(1/6,0),(2/3,0)]
    #print(estados(m_313,v_313,1))
    #respuesta: a nivel físico las nuevas canicas aparecerian 

#ejercicio 3.1.4 (experimento de matriz con -1)
    m_314 = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(-1,0),(0,0),(0,0),(0,0),(1,0)],
         [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
         [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
         [(-1,0),(0,0),(0,0),(0,0),(-1,0),(0,0)]]
    v_314 = [(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)]
    #print(estados(m_314,v_314,1))
    #respuesta: en una de las cajas puede quedar un numero de canicas negativas 

#ejercicio 3.1.5 (experimento calles de ciudad)
    m_315 = [[(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(1,0),(0,0),(0,0)],
         [(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(1,0),(1,0)]]
    v_315 = [(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0)]
    #print("despues de un click: ",estados( m_315,v_315,1))
    #print("despues de dos click: ",estados( m_315,v_315,2))
    #print("despues de cuatro click: ",estados( m_315,v_315,4))


#Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
#doble rendija (# de rendijas, blancos, cliks)
    #print(dobleRendija(2,3,1))


#Experimentos de las múltiples rendijas cuantico, con más de dos rendijas.
#doble rendija (# de rendijas, blancos, cliks)
    #print(dobleRendijaCuantico(2,3,1))


#Diagrama de estados
    #print(diagramaEstados(v))


