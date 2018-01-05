"""
JULIA SET - MAPA DE CALOR
MODULOS: PYPLOT, NUMPY
~~~~~~~~~~~~~~~
"""
#MODULOS

import matplotlib.pyplot as plt
import numpy
from time import clock

#CONSTANTES
ORDEN = 2000 #matriz 1000x1000. 1M de pixels
MAXIT = 100
EXP = 2 #de momento
LIMIT = 2
#FUNCIONES

def juliaset(c):
    """Devuelve un entero entre 0 y 255 dada la evaluacion de un numero complejo C segun este acote o crezca"""
    z = c
    for i in range(MAXIT):
        z = z**EXP + complex("0.25+0.5j")
        if abs(z) >= 2:
            break
    return i
    
def display(matriz):
    """Dada una matriz muestra y guarda el mapa de calor de la misma. usamos pyplot."""
    plt.figure(1)
    plt.clf()
    plt.imshow(matriz.T,cmap=plt.cm.magma,origin='lower')
    plt.title("Julia set")
    plt.savefig("jset.png")
    
    plt.show()

def main():
        
    t_0 = clock()
    m_julia = numpy.zeros([ORDEN,ORDEN],dtype=float)
    x_val   = numpy.linspace(-2,2,ORDEN)
    y_val   = numpy.linspace(-2,2,ORDEN)
    
    for i,real in enumerate(x_val):
        for j,imag in enumerate(y_val):
            m_julia[i][j] = (juliaset(complex(real,imag))/100)
    
    display(m_julia)
    t_f = clock()
    print("Generado en %i segundos."%(t_f-t_0))
    
#main

if __name__ == "__main__":
    main()