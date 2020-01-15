# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:04:55 2019

@author: Luis Aponte
"""
from graphics import*

def main():
   
    #crear pantalla de interasion
    
    win = GraphWin("Account",500,500)
    win.setCoords(-10,-10,10,10)
    
    
    Image(Point(0,0),"ima.gif").draw(win)
    
   
    #bienvenida
    
    bienvenido =  Text(Point(0,0),"Este programa es para crea cuenta y desconifica la contrase~a").draw(win)
    button = Rectangle(Point(-3,-3),Point(3,-1)).draw(win)
    empezar = Text(Point(0,-2),"EMPEZAR").draw(win)
    bienvenido.setFill("white")
    
    button.setFill("white")
    
    clickPoint = win.getMouse()
    
    
    bienvenido.undraw()
    empezar.undraw()
    button.undraw()
    #que quiere hacer el usuario
    
    texto = Text(Point(0,0)," Por favor , seguir intrucuoines\n\nEscribe en el blanco: a o b\n\na). crear cuenta.\n\nb)descodificar contrase~a").draw(win)
    texto.setFill("white")
    
    blanco = Entry(Point(0,-5),5).draw(win)
    
    button = Rectangle(Point(-2,-8.5),Point(2,-7.5)).draw(win)
    button.setFill("white")
    enter = Text(Point(0,-8),"Enter").draw(win)
    
    
    
    clickPoint = win.getMouse()
   
    
    
    
    texto.undraw()
    blanco.undraw()
   
    #crear variable  con la intruccion que metio el usuario
   
    intruccion = blanco.getText()
    button.undraw()
    enter.undraw()
    
    
    #condicion
    
    
                               #crear usarname y passwor
    if intruccion == "a":
       
        texto =  Text(Point(0,0),"Entre su nombre completo").draw(win)
        texto.setFill("white")
        
        nombre = Entry(Point(0,-1),30).draw(win)
        
        button = Rectangle(Point(-3,-2),Point(3,-4)).draw(win)
        button.setFill("white")
        codificar =  Text(Point(0,-3),"Codificar").draw(win)
        
        
        
        clickPoint = win.getMouse()
        
        nombre.undraw()
        nombre = nombre.getText()
        texto.undraw()
        codificar.undraw()
        button.undraw()
        
        listaNombre =  nombre.split()
        largoNombre =  len(nombre)
        
        username = ""
        password = ""
        
        
        
        #username
        
        for cadena in listaNombre:
            username  += cadena[:2]  ## es lo mismo que username = username + cadena[:2].lower()
        for ch in nombre[::-1]:
            password = password + str(chr(ord(ch) + 2))
            suma += 1
                
        
        username = Text(Point(0,0),"usarname :"+username.lower() + str(largoNombre)).draw(win)
        username.setFill("white")
        
        password = Text(Point(0,-2),"password : "+password).draw(win)
        password.setFill("white")
      

         
                               #descodificar password
    else:
        
        texto = Text(Point(0,0),"Entre su password: ").draw(win)
        texto.setFill("white")
        password=  Entry(Point(0,-1),18).draw(win)
        
        button = Rectangle(Point(-3,-3),Point(3,-5)).draw(win)
        button.setFill("white")
        descodificador = Text(Point(0,-4),"Descodificar").draw(win)
        
        
        clickPoint = win.getMouse()
        password.undraw()
        
        password = password.getText()
        button.undraw()
        descodificador.undraw()
        texto.undraw()
        

        nombre = ""
        
        
        for i in password:
            nombre = nombre + str(chr(ord(i)-2))
            
       
        
        resultado = Text(Point(0,0),"Su nombre es: " + nombre[::-1]).draw(win) 
        resultado.setFill("white")
    
    
    
  
  
    #end
    win.getMouse()
    win.close()

main()
