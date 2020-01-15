# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:55:17 2019

@author: Luis Aponte Lopez
"""

from graphics import*
from statistics import*

#funcion que calcula promedio, la mediana, valor mayor del eje de x y valor menor del eje de y. Mas lo imprime en pantalla
def calculoResultado(lista,win):
    
    #VALOR MINIMO
    Text(Point(3,20),"Valor minimo = "+str(lista[0])).draw(win)
    
    # valor maxinmo
    Text(Point(3,19),"Valor maximo = "+str(lista[-1])).draw(win)
    
    #promedio
    Text(Point(2.5,18),"Promedio = "+str(round(mean(lista)))).draw(win)
    
    #mediana
    largo = len(lista)
    mediana = largo/2
    mediana=lista[int(mediana)]
    Text(Point(2.5,17),"Mediana = "+str(mediana)).draw(win)

def evento(win):
    
    x=0#valor inicial
    
    #crear evento
    for i in range(10):
       
        #creando las cordenada del eje de x (seria el valor de la columnas)
        Text(Point(2+x,1.5),i).draw(win)
        
        x+=2# se utiliza para tener una separacion y columnas simetrica 

def columnas(lista,win):
    
    x=0 #valor inicial
   
    #columnas
    for i in range(10):
       
        #cuenta cuanta veces se repite el numero y lo imprime en la pantalla 
        frecuencia = lista.count(i)
       
        texto=Text(Point(2+x,2.5+frecuencia),frecuencia).draw(win)
        texto.setFill("red")
        
        #grafica columnas
        rectangle=Rectangle(Point(1.5+x,2+frecuencia),Point(2.5+x,2)).draw(win)
        rectangle.setFill("blue")
        
        x+=2# se utiliza para tener una separacion y columnas simetrica
        
def main():
   #bienvenida
    print("Bienvenido este programa solo funciona con:")
    
    for i in range(1,4):
        
        print("\narchivo"+str(i)+".txt")
   
    #ciclo para repetir o parar programa
    a = True
    while(a):
    
        #indicar archivo y leerlo
        fname = input("Entre uno de los 3  archivos: ")
        infile = open(fname,"r")
        
        lista=[]
        for line in infile:
            lista.append(int(line))
    
        #crear ventana
        win =  GraphWin("Histograma para "+fname,600,600)
        win.setCoords(0,0,22,22)
        win.setBackground("white")
        
       #calcular promedio , mediana , valor minimo  y  valor maximo
        calculoResultado(lista,win)
      
        #crear  evento(#creando las cordenada del eje de x (seria el valor de la columnas))
        evento(win)
        
        #columnas 
        columnas(lista,win)
        
        win.getMouse()
        win.close()
        print("")
        
        #lo que va determinar si se repite o se para el programa
        terminar=input("\nQuieres repetir el programa?(si/no): ")
       
        if(terminar == "no"):
            a = False

    #Despedida     
    print("\nGracias por usar el programa regresa pronto.")
main()
