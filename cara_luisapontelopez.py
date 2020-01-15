# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:51:22 2019

@author: Luis Aponte
"""

from graphics import*

def main():
   
    #variable.setFill() -------> se utilza para ponerle color a los objeto
    
    win = GraphWin("Cara",800,800)#Definir el tamaño de la ventana
    win.setCoords(-10,-10,10,10)# cambiar las Coordenadas cartesianas
      
    orejaDerecha = Oval(Point(4.25,3),Point(7,-1))
    orejaDerecha.draw(win)
    orejaDerecha.setFill("Burlywood1")
    
    pantallaDerecha =  Circle(Point(5.7,-.4),.25)
    pantallaDerecha.draw(win)
    pantallaDerecha.setFill("Gray80")
    pantallaDerecha2 = Circle(Point(5.7,-.4),.20)
    pantallaDerecha2.draw(win)
    pantallaDerecha2.setFill("Gray85")
    pantallaDerecha3 = Circle(Point(5.7,-.4),.15)
    pantallaDerecha3.draw(win)
    pantallaDerecha3.setFill("Gray90")
    pantallaDerecha4 = Circle(Point(5.7,-.4),.10)
    pantallaDerecha4.draw(win)
    pantallaDerecha4.setFill("Gray95")
    pantallaDerecha5 = Circle(Point(5.7,-.4),.05)
    pantallaDerecha5.draw(win)
    pantallaDerecha5.setFill("Gray99")
    
    orejaIzquierdo = Oval(Point(-4.25,3),Point(-7,-1))
    orejaIzquierdo.draw(win)
    orejaIzquierdo.setFill("Burlywood1")
    
    pantallaIzquierdo =  Circle(Point(-5.7,-.4),.25)
    pantallaIzquierdo.draw(win)
    pantallaIzquierdo.setFill("Gray80")
    pantallaIzquierdo2 = Circle(Point(-5.7,-.4),.20)
    pantallaIzquierdo2.draw(win)
    pantallaIzquierdo2.setFill("Gray85")
    pantallaIzquierdo3 = Circle(Point(-5.7,-.4),.15)
    pantallaIzquierdo3.draw(win)
    pantallaIzquierdo3.setFill("Gray90")
    pantallaIzquierdo4 = Circle(Point(-5.7,-.4),.10)
    pantallaIzquierdo4.draw(win)
    pantallaIzquierdo4.setFill("Gray95")
    pantallaIzquierdo5 = Circle(Point(-5.7,-.4),.05)
    pantallaIzquierdo5.draw(win)
    pantallaIzquierdo5.setFill("Gray99")
        
    rostro = Oval(Point(5,6),Point(-5,-6))
    rostro.draw(win)
    rostro.setFill("Burlywood1") 
    
    parpadoDerecho = Polygon(Point(.5,2),Point(1.25,2.50),Point(1.50,2.70),Point(1.75,2.80),Point(2,2.90),Point(2.50,2.90),Point(2.75,2.80),Point(3,2.70),Point(3.25,2.50),Point(4,2))
    parpadoDerecho.draw(win)
    
    escleraDerecha  = Polygon(Point(.5,2),Point(1.25,1.50),Point(1.50,1.30),Point(1.75,1.20),Point(2,1.10),Point(2.50,1.10),Point(2.75,1.20),Point(3,1.30),Point(3.25,1.50),Point(4,2))
    escleraDerecha.draw(win)
    escleraDerecha.setFill("white")
    
    irisDerecha = Circle(Point(2.25,1.5),.44)
    irisDerecha.draw(win)
    irisDerecha.setFill("Brown")
   
    pupilaDerecha =  Circle(Point(2.25,1.5),.20)
    pupilaDerecha.draw(win)
    pupilaDerecha.setFill("Black")
    
    cejaDerecha1 =  Oval(Point(.3,3.19),Point(1,3.71))
    cejaDerecha1.draw(win)
    cejaDerecha1.setFill("Black")
    cejaDerecha2 = Rectangle(Point(.5,3.19),Point(3.2,3.71))
    cejaDerecha2.draw(win)
    cejaDerecha2.setFill("Black")
    cejaDerecha3=Polygon(Point(3.2,3.71),Point(4.2,2.5),Point(3.2,3.19))
    cejaDerecha3.draw(win)
    cejaDerecha3.setFill("Black")
    cejaLinea = Polygon(Point(1.55,3.20),Point(2.6,3.71),Point(2.9,3.71),Point(1.85,3.20))
    cejaLinea.draw(win)
    cejaLinea.setFill("Burlywood1")
    parchoA = Line(Point(.3,3.71),Point(3.3,3.71))
    parchoA.draw(win)
    parchoA.setFill("Burlywood1")
    parchoB = Line(Point(.3,3.19),Point(3.19,3.19))
    parchoB.draw(win)
    parchoB.setFill("Burlywood1")
    
    suma=0#se utiliza para crear la misma pestañas en diferente punto de la x
    for i in range(14):#repetir la instruccion por 14 veces
        suma=.25  +suma
        pestañas=Line(Point(.25+suma,2),Point(.5+suma,2.50))
        pestañas.draw(win)
    
    parpadoIzquierdo = Polygon(Point(-.5,2),Point(-1.25,2.50),Point(-1.50,2.70),Point(-1.75,2.80),Point(-2,2.90),Point(-2.50,2.90),Point(-2.75,2.80),Point(-3,2.70),Point(-3.25,2.50),Point(-4,2))
    parpadoIzquierdo.draw(win)
    
    escleraIzquierdo = Polygon(Point(-.5,2),Point(-1.25,1.50),Point(-1.50,1.30),Point(-1.75,1.20),Point(-2,1.10),Point(-2.50,1.10),Point(-2.75,1.20),Point(-3,1.30),Point(-3.25,1.50),Point(-4,2))
    escleraIzquierdo.draw(win)
    escleraIzquierdo.setFill("white")
    
    irisIzquierda = Circle(Point(-2.25,1.5),.44)
    irisIzquierda.draw(win)
    irisIzquierda.setFill("Brown")
    
    pupilaIzquierda =  Circle(Point(-2.25,1.5),.20)
    pupilaIzquierda.draw(win)
    pupilaIzquierda.setFill("Black")
    
    cejaIzquierda1 =  Oval(Point(-.3,3.20),Point(-1,3.7))
    cejaIzquierda1.draw(win)
    cejaIzquierda1.setFill("Black")
    cejaIzquierda2 = Rectangle(Point(-.5,3.20),Point(-3.2,3.70))
    cejaIzquierda2.draw(win)
    cejaIzquierda2.setFill("Black")
    cejaIzquierda3=Polygon(Point(-3.2,3.70),Point(-4.2,2.5),Point(-3.2,3.2))
    cejaIzquierda3.draw(win)
    cejaIzquierda3.setFill("Black")
    
    suma=0#se utiliza para crear la misma pestañas en diferente punto de la x
    for i in range(14):#repetir la instruccion por 14 veces
        suma=.25  +suma
        pestañas=Line(Point(-4.25+suma,2),Point(-4+suma,2.50))
        pestañas.draw(win)
   
    narizA=Line(Point(-.30,1.7),Point(-.90,-.60))
    narizA.draw(win)
    narizB=Circle(Point(-1,-1),.5)
    narizB.draw(win)
    narizC=Circle(Point(0,-1.15),.65)
    narizC.draw(win)
    narizD=Circle(Point(1,-1),.5)
    narizD.draw(win)
    narizE=Line(Point(.30,1.7),Point(.90,-.60))
    narizE.draw(win)
    narizF=Rectangle(Point(-.759,-.399),Point(.759,-1.30))
    narizF.draw(win)
    narizF.setFill("Burlywood1")
    narizG = Line(Point(-.759,-1.30),Point(.759,-1.30))
    narizG.draw(win)
    narizG.setFill("Burlywood1")
    narizH = Line(Point(-.759,-.399),Point(-.759,-1.30))
    narizH.draw(win)
    narizH.setFill("Burlywood1")
    narizI = Line(Point(-.759,-.399),Point(.759,-.399))
    narizI.draw(win)
    narizI.setFill("Burlywood1")
    narizJ = Line(Point(.759,-1.30),Point(.759,-.399))
    narizJ.draw(win)
    narizJ.setFill("Burlywood1")
     
    for i in range(1,8):#repetir la instruccion por 7 veces
        peloA = Circle(Point(-4.05+i,5.5),1)
        peloA.draw(win)
        peloA.setFill("Black") 
    peloB = Circle(Point(-3.5,5),1)
    peloB.draw(win)
    peloB.setFill("Black")
    peloC = Circle(Point(3.5,5),1)
    peloC.draw(win)
    peloC.setFill("Black")
    peloD = Circle(Point(-3.7,4.75),1)
    peloD.draw(win)
    peloD.setFill("Black")
    peloE = Circle(Point(3.7,4.75),1)
    peloE.draw(win)
    peloE.setFill("Black")
    
    boca = Polygon(Point(-3,-2.5),Point(-2.90,-2.75),Point(-2.70,-3.25),Point(-2.5,-3.5),Point(-2.25,-3.75),Point(-2,-4),Point(-1,-4.5),Point(-.5,-4.6),Point(.5,-4.6),Point(1,-4.5),Point(2,-4),Point(2.25,-3.75),Point(2.5,-3.5),Point(2.70,-3.25),Point(2.90,-2.75),Point(3,-2.5))
    boca.draw(win)
    boca.setFill("Red")
    
    lengua = Polygon(Point(0,-3.7),Point(-.5,-3.4),Point(-.9,-3.3),Point(-1.3,-3.4),Point(-1.7,-3.7),Point(-2,-4),Point(-1,-4.5),Point(-.5,-4.6),Point(.5,-4.6),Point(1,-4.5),Point(2,-4),Point(1.7,-3.7),Point(1.3,-3.4),Point(.9,-3.3),Point(.5,-3.4),Point(0,-3.7),Point(0,-4.6))
    lengua.draw(win)
    lengua.setFill("Pink")
    lenguaLinea = Line(Point(0,-3.7),Point(0,-4.6))
    lenguaLinea.draw(win)
    lenguaLinea.setFill("Pink")

    diente =  Polygon(Point(-3,-2.5),Point(-2.75,-3),Point(2.75,-3),Point(3,-2.5))
    diente.draw(win)
    diente.setFill("White")
    
    suma =  0 #se utiliza para dividir los diente en un mismo tamaño
    for i in range(7):#repetir la instruccion por 7 veces
        suma = .75 + suma
        divisorDeDiente=Line(Point(-3+suma,-2.50),Point(-3+suma,-3))
        divisorDeDiente.draw(win)
       
    
    win.getMouse()
    win.close()
main()
