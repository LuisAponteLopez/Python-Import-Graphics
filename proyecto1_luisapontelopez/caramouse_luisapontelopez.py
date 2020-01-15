# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:23:52 2019

@author: Luis Aponte
"""


   
    
from graphics import*

def main():
    win = GraphWin("Mr. Potato",800,800)
    win.setCoords(-10,-10,10,10)
   # win.setBackground("white")
    miImagen = Image(Point(0,0),"toystory.gif").draw(win)
    

  
    
    texto =  Text(Point(6,8),"Donde quiere la cara?")
    texto.draw(win)
    
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()# te  permite estraer la x
    y = clickPoint.getY()
    
    cara = Oval(Point(x - 4, y - 5),Point(x + 4,y + 5))
    cara.draw(win)
    cara.setFill("sienna3")
    cara.setWidth(3)
    
    
    texto.undraw()
    texto = Text(Point(6,8),"Donde quieres el ojo derecho?")
    texto.draw(win)
    
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()# te  permite estraer la x
    y = clickPoint.getY()
    ojoDerecho = Circle(Point(x,y),1)
    ojoDerecho.draw(win)
    ojoDerecho.setFill("white")
    ojoDerecho.setWidth(3)
    
    b = Circle(Point(x,y),.4)
    b.draw(win)
    b.setFill("black")
    
    texto.undraw()
    texto = Text(Point(6,8),"donde quieres el ojo izquierdo?")
    texto.draw(win)
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()# te  permite estraer la x
    y = clickPoint.getY()
   
    ojoIzquierdo = Circle(Point(x,y),1)
    ojoIzquierdo.draw(win)
    ojoIzquierdo.setFill("white")
    ojoIzquierdo.setWidth(3)
    
    a = Circle(Point(x,y),.4)
    a.draw(win)
    a.setFill("black")
    
    texto.undraw()
    texto = Text(Point(6,8),"donde quiere la nariz?")
    texto.draw(win)
  
    clickPoint = win.getMouse()
    x = clickPoint.getX()# te  permite estraer la x
    y = clickPoint.getY()
    nariz = Oval(Point(x+1.5,y+1),Point(x-1.5,y-1))
    nariz.draw(win)
    nariz.setFill("red")
    nariz.setWidth(3)
    
    texto.undraw()
    texto = Text(Point(6,8),"donde quiere la boca?")
    texto.draw(win)
  
    clickPoint = win.getMouse()
    x = clickPoint.getX()# te  permite estraer la x
    y = clickPoint.getY()
    boca = Oval(Point(x-1.25,y-.75),Point(x+1.25,y+.75))
    boca.draw(win)
    boca.setFill("white")
    boca.setWidth(3)
    
    texto.undraw()
    texto = Text(Point(6,8),"Donde quiere el bigote?")
    texto.draw(win)
    
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    bigoteA = Oval(Point(x,y-.75),Point(x+2.5,y+.75))
    bigoteA.draw(win)
    bigoteA.setFill("black")
    bigoteA.setWidth(3)
    
    bigoteB = Oval(Point(x,y-.75),Point(x-2.5,y+.75))
    bigoteB.draw(win)
    bigoteB.setFill("black")
    bigoteB.setWidth(3)
    
    
    texto.undraw()
    texto = Text(Point(6,8),"Donde quiere la oreja derecha?")
    texto.draw(win)
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    orejaDere = Oval(Point(x,y-1.75),Point(x+2.5,y+1.75))
    orejaDere.draw(win)
    orejaDere.setFill("pink")
    orejaDere.setWidth(3)
    
    texto.undraw()
    texto = Text(Point(6,8),"Donde quiere la oreja izquierda?")
    texto.draw(win)
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    orejaIzqu = Oval(Point(x,y-1.75),Point(x-2.5,y+1.75))
    orejaIzqu.draw(win)
    orejaIzqu.setFill("pink")
    orejaIzqu.setWidth(3)
    
    texto.undraw()
    texto = Text(Point(6,8),"Donde quiere el sombrero?")
    texto.draw(win)
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    sombrero = Oval(Point(x+3,y-1.5),Point(x-3,y+1.5))
    sombrero.draw(win)
    sombrero.setFill("black")
    sombreroB = Oval(Point(x+2,y+2.5),Point(x-2,y-1))
    sombreroB.draw(win)
    sombreroB.setFill("black")
    
    texto.undraw()
    texto = Text(Point(6,8),"Donde quiere el lazo?")
    texto.draw(win)
    
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    
    lazo = Polygon(Point(x-2.5,y+2),Point(x,y),Point(x+2.5,y-2),Point(x+2.5,y+2),Point(x,y),Point(x-2.5,y-2),Point(x-2.5,y+2))
    lazo.setWidth(3)
    lazo.setFill("blue")
    lazo.draw(win)
    
    texto.undraw()
    texto = Text(Point(-3,9.5),"Soy Sr. Papa")
    texto.draw(win)
    textob= Text(Point(-1,9),"Gracias , por usar el programa")
    textob.draw(win)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()