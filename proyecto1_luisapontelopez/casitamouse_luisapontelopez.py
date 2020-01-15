# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:20:20 2019

@author: Luis Aponte
"""

from graphics import*


def main():
   
    #dibujar ventana 
    
    win = GraphWin("Cara",1000,500)#Definir el tamaño de la ventana
    win.setCoords(-20,-10,20,10)# cambiar las Coordenadas cartesianas
    
    #estetica de ventana 
    
    ladoIzquierdo = Rectangle(Point(0,-20),Point(-20,20)).draw(win)
    ladoIzquierdo.setFill("white")
    ladoIzquierdo.setWidth(5)
    
    
    
    #bienvenida y intruciones del programa
    
    texto =  Text(Point(-10,4),"Bienvenido, este programa esta hecho para que").draw(win)
    texto.setStyle("bold")
    textoB = Text(Point(-10,3),"el usario pueda dibujar una casa y pintarla .").draw(win)
    textoB.setStyle("bold")
    
    textoc = Text(Point(10,4),"La parte gris es para dibujar la casa").draw(win)
    textoc.setStyle("bold")
    
    
    botonfondo = Rectangle(Point(-12,-.5),Point(-8,.5)).draw(win)
    
    comenzar = Text(Point(-10,0),"Empezar").draw(win)
    
    
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    
    
    texto.undraw()
    textoB.undraw()
    textoc.undraw()
    comenzar.undraw()
    botonfondo.undraw()
    
    
    
    #click1 y click2 – especifica esquina inferior izquierda y esquina superior derecha de una casa rectangular.
    
    texto =  Text(Point(-10,4),"Especifica esquina inferior izquierda de la casa.").draw(win)
    texto.setStyle("bold")
    
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    
    
    texto.undraw()
    
   
    
    
    texto =  Text(Point(-10,4),"Especifica esquina superio derecho de la casa .").draw(win)
    texto.setStyle("bold")
    
    clickPoint = win.getMouse()
    a = clickPoint.getX()
    b = clickPoint.getY()
    
    
    
    
  
    base =  Rectangle(Point(x,y),Point(a,b)).draw(win)
    base.setWidth(3)
   
     
    texto.undraw()
       
    tono = Entry(Point(-10,-1),15)
    tono.setText("color")
    tono.draw(win)
   

  
    texto  =     Text(Point(-10,8),"Entre un color de los  de la lista ").draw(win)
    texto.setStyle("bold")
    textoa =     Text(Point(-10,7),"1. white ").draw(win)
    textob =     Text(Point(-10,6),"2. blue ").draw(win) 
    textoc =     Text(Point(-10,5),"3. black").draw(win)
    textod =     Text(Point(-10,4),"4. red").draw(win)
    textoe =     Text(Point(-10,3),"5. green").draw(win)
    textof =     Text(Point(-10,2),"6. pink").draw(win) 
    textog =     Text(Point(-10,1),"7. violet").draw(win) 
    
    
    botonfondo =Rectangle(Point(-11,-1.5),Point(-9,-2.5)).draw(win)
    botonfondo.setFill("white")
    
    boton =Text(Point(-10,-2),"pintar").draw(win)
    

    
    win.getMouse()
    
    
    base.setFill(tono.getText())
    
    texto.undraw()
    textoa.undraw()
    textob.undraw()
    textoc.undraw()
    textod.undraw() 
    textoe.undraw()
    textof.undraw()
    textog.undraw() 
    
    
    tono.undraw()
    
    boton.undraw()
    
    botonfondo.undraw()
    
   
    

        
    #formula en base a los primero 2 datos 
    
     
    grosor1cuarto = (a-x)/4  #El grosor de la puerta deberá ser una cuarta parte del ancho de la casa.
    
    anchoVentana = grosor1cuarto  /2 #La ventana deberá tener la mitad del ancho de la puerta
    
    ventana = anchoVentana / 2 # se va a utilizar para poder definir las cordenada de la ventana
    
    xTopeTecho = (a-x)/2
    
    X=x
    Y=y
    A=a
    B=b
    
    
    
    
    #click3 – especifica el tope del borde superior de la puerta rectangular. El grosor de la puerta deberá ser una cuarta parte del ancho de la casa.
                                        
   
   
    

    

    texto =  Text(Point(-10,4),"Especifica el tope del borde superior de la puerta rectangular.").draw(win)
    texto.setStyle("bold")
    
    clickPoint = win.getMouse()
    a = clickPoint.getX()
    b = clickPoint.getY()
   
    
    
    puerta = Rectangle(Point(a,b),Point(a+grosor1cuarto,y)).draw(win) 
    puerta.setWidth(3)
    
    texto.undraw()
    
    tono = Entry(Point(-10,-1),15)
    tono.setText("color")
    tono.draw(win)
   
    
    
  
    texto  =     Text(Point(-10,8),"Entre un color de la puerta ").draw(win)
    texto.setStyle("bold")
    textoa =     Text(Point(-10,7),"1. white ").draw(win)
    textob =     Text(Point(-10,6),"2. brown ").draw(win) 
    textoc =     Text(Point(-10,5),"3. black").draw(win)
    
    botonfondo =Rectangle(Point(-11,-1.5),Point(-9,-2.5)).draw(win)
   
    boton =Text(Point(-10,-2),"pintar").draw(win)
    

    
    
    win.getMouse()
    
    puerta.setFill(tono.getText())
    
    texto.undraw()
    textoa.undraw()
    textob.undraw()
    textoc.undraw()
   
    
    
    tono.undraw()
    
    boton.undraw()
    
    
     
    botonfondo.undraw()
        
        
    #click4 – especifica centro de una ventana cuadrada. La ventana deberá tener la mitad del ancho de la puerta

    
    
    
    
    texto =  Text(Point(-10,4),"Especifica centro de una ventana .").draw(win)
    texto.setStyle("bold")
     
     
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    
    
    
    window =  Rectangle(Point(x-ventana,y-ventana),Point(x+ventana,y+ventana)).draw(win)
    window.setFill("blue")
    window.setWidth(3)
   
    
    lineaA = Line(Point(x-ventana,y),Point(x+ventana,y)).draw(win)
    lineaA.setWidth(3)
    
    lineaB=Line(Point(x,y - ventana),Point(x,y + ventana)).draw(win)
    lineaB.setWidth(3)
    
    
    texto.undraw()
    
    tono = Entry(Point(-10,-2),15)
    tono.setText("color")
    tono.draw(win)
   
    
  
    texto  =     Text(Point(-10,8),"Entre el color del la linea negra de la ventana").draw(win)
    texto.setStyle("bold")
    textoa =     Text(Point(-10,7),"1. white ").draw(win)
    textob =     Text(Point(-10,6),"2. blue ").draw(win) 
    textoc =     Text(Point(-10,5),"3. black").draw(win)
    textod =     Text(Point(-10,4),"4. red").draw(win)
    textoe =     Text(Point(-10,3),"5. green").draw(win)
    textof =     Text(Point(-10,2),"6. pink").draw(win) 
    textog =     Text(Point(-10,1),"7. violet").draw(win) 
    textoh =     Text(Point(-10,0),"8.  brown").draw(win)

    botonfondo =Rectangle(Point(-11,-2.5),Point(-9,-3.5)).draw(win)
    
    
    boton =Text(Point(-10,-3),"pintar").draw(win)
    
    
    win.getMouse()
    
    lineaA.setFill(tono.getText())
    lineaB.setFill(tono.getText())
    window.setOutline(tono.getText())
    
    
    texto.undraw()
    textoa.undraw()
    textob.undraw()
    textoc.undraw()
    textod.undraw() 
    textoe.undraw()
    textof.undraw()
    textog.undraw() 
    textoh.undraw()
    
    tono.undraw()
    
    boton.undraw()
    
   
     
    botonfondo.undraw()
    
    
    #click5 – especifica el tope del techo de dos aguas. El tope se deberá conectar con las esquinas de la casa.
    
    
    
    texto =  Text(Point(-10,4),"Especifica el tope del techo de dos aguas.").draw(win)
    texto.setStyle("bold")
    
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    
    
    techo = Polygon(Point(X + xTopeTecho,y),Point(X-.5,B),Point(A+.5,B)).draw(win)
    techo.setWidth(3)
    
        
    texto.undraw()
    
    tono = Entry(Point(-10,-2),15)
    tono.setText("color")
    tono.draw(win)
   
    
    
  
    texto  =     Text(Point(-10,8),"Entre un color de techo").draw(win)
    texto.setStyle("bold")
    textoa =     Text(Point(-10,7),"1. white ").draw(win)
    textob =     Text(Point(-10,6),"2. blue ").draw(win) 
    textoc =     Text(Point(-10,5),"3. black").draw(win)
    textod =     Text(Point(-10,4),"4. red").draw(win)
    textoe =     Text(Point(-10,3),"5. green").draw(win)
    textof =     Text(Point(-10,2),"6. pink").draw(win) 
    textog =     Text(Point(-10,1),"7. violet").draw(win) 
    textoh =     Text(Point(-10,0),"8.  brown").draw(win)
    
    botonfondo =Rectangle(Point(-11,-3.5),Point(-9,-2.5)).draw(win)
    
    
    boton =Text(Point(-10,-3),"pintar").draw(win)
    
    
    
    win.getMouse()
    
    techo.setFill(tono.getText())
   
    
    
    texto.undraw()
    textoa.undraw()
    textob.undraw()
    textoc.undraw()
    textod.undraw() 
    textoe.undraw()
    textof.undraw()
    textog.undraw() 
    textoh.undraw()
    
    tono.undraw()
    
    
    boton.undraw()
    
    botonfondo.undraw()
    
    #mostrar la salida - Grasisas por usar el programa . Regresa pronto
    

    
    
    texto=Text(Point(-10,4),"Gracias por usar el programa.Regresa pronto.").draw(win)
   
    
    texto.setStyle("bold")
 
    boton =Text(Point(-10,-3),"terminar").draw(win)
    botonfondo =Rectangle(Point(-12,-3.5),Point(-8,-2.5)).draw(win)
    
    
    
    
    #terminar 
    win.getMouse()
    win.close()
    
    
    
main()