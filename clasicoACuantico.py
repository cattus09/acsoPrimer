import math

import LIbComp as lc
import LIbEspVect as lE

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
    matriz = [[(0,0) for i in range (tam)] for i in range (tam)] 
    for i in range (tam):
        for j in range (tam):
            if i == 0 and j < ren:
                matriz[i][j] = 1/ren
            elif 0 < i <= ren:
                if i == 1 and 2 * (ren-1) -1 < j < 2 * (ren-1) + blan :
                    matriz[i][j] = 1/blan
                if i == 2 and 2 * (ren-1) +1 < j < 2 * (ren-1) + blan +2 and tam >= 7:
                    matriz[i][j] = 1/blan
                if i == 3 and 2 * (ren-1) +1 < j < 2 * (ren-1) + blan +4 and tam >= 12:
                    matriz[i][j] = 1/blan
                if i == 4 and 2 * (ren-1) +1 < j < 2 * (ren-1) + blan +6 and tam >= 15:
                    matriz[i][j] = 1/blan
            elif i > ren and j == i:
                matriz[i][j] = 1
    m = lE.transpuesta(matriz)
    s = lE.producMat(m,m)
    return s


if __name__ == '__main__':
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

#doble rendija (# de rendijas, blancos, cliks)
    print(dobleRendija(2,5,1))


#Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.


    

