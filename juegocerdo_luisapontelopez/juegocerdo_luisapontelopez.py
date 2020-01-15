# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:05:43 2019

@author: Luis Aponte
"""

from random import randint
from graphics import*
from time import sleep

#abri el archivo record.txt 
def textoArchivo():
       
    f = open ('record.txt','r')
    palabras = f.read()
    palabras= palabras.split(",")
    f.close()
    
    return palabras # se devulve una lista con un nombre y su puntuacion

#ventana dse bienvenida 
def VentanaBienvenida(win):
    
     imagen =  Image(Point(0,0),"cerdo_fondonegro.gif").draw(win)
     textoBienvenida = Text(Point(0,8),"EL JUEGO DEL CERDO").draw(win)
     textoBienvenida.setFill("Pink")
     textoBienvenida.setStyle("bold italic")
     textoBienvenida.setSize(18)
     botonComenzar = Rectangle(Point(-2,-7),Point(2,-9)).draw(win)
     botonComenzar.setFill("Red")
     textoComenzar=Text(Point(0,-8),"COMENZAR").draw(win)
     textoComenzar.setStyle("bold")
     textoComenzar.setFill("White")
     win.getMouse()
    
    #borrando ventana
     imagen.undraw()
     textoBienvenida.undraw()
     botonComenzar.undraw()
     textoComenzar.undraw()


#ususario se pone nombre 
def VentanaNombre(win):
   
    textoUsuario = Text(Point(0,2),"Entre un nombre de usuario").draw(win)
    textoUsuario.setStyle("bold italic")
    textoUsuario.setSize(18)
    textoUsuario.setFill("Pink")
    nombre = Entry(Point(0,0),15).draw(win)
    boton = Rectangle(Point(-2,-2),Point(2,-4)).draw(win)
    boton.setFill("Blue")
    textoJugar=Text(Point(0,-3),"JUGAR").draw(win)
    textoJugar.setStyle("bold")
    textoJugar.setFill("White")
    win.getMouse()
   
    #borrando ventana
    textoUsuario.undraw()
    nombre.undraw()
    boton.undraw()
    textoJugar.undraw()
    
    return nombre.getText() #devulve el nombre de usuario que el usuario se puso 

#la corrida del dado
def ventanaJuego(win,nombre,palabras):
    
    suma = 0  # variable suma se utilza para sumar el numero que salga en el dado
    a = True
    textoSuma=Text(Point(-7,-1),suma).draw(win)
    textoSuma.setFill("white")
    textoScore = Text(Point(-7,1),"SCORE").draw(win)
    textoScore.setFill("red")
    palabraRecord =Text(Point(7,1),"RECORD").draw(win)
    palabraRecord.setFill("red")
    textoRecord = Text(Point(7,-1),str(palabras[0])+": "+str(palabras[1])).draw(win)
    textoRecord.setFill("white")
    
    while a:
       
        #crear botones
        parar = Rectangle(Point(2,-7),Point(6,-9)).draw(win)
        parar.setFill("Red")
        textoA=Text(Point(4,-8),"Parar").draw(win)
        seguir= Rectangle(Point(-2,-7),Point(-6,-9)).draw(win)
        seguir.setFill("Blue")
        textoB=Text(Point(-4,-8),"SEGUIR").draw(win)
        
        for i in range(13):#ciclo de tirar el dado
           
            # tirar dado
            numero = randint(1,6)
            imagen = Image(Point(0,0),"die" + str(numero)+".gif").draw(win)
            sleep(.5)
            
            if i<12 :
                imagen.undraw()
      
        if numero == 1: #si sale uno el usuario pierde  y su puntuacion es 0
            
            sleep(.5)
            borrarVentanaJuego(imagen,parar,seguir,textoA,textoB) #borrar los elemnto de la pantalla
            suma=0
            break
        
        else:
            
            textoSuma.undraw()
            suma = suma + numero #Score
            textoSuma=Text(Point(-7,-1),suma).draw(win)
            textoSuma.setFill("white")
       
        while True:
            
            clickPoint = win.getMouse()
            x = clickPoint.getX()
            y = clickPoint.getY()
            if x>=2 and x<=6 and y<=-7 and y>=-9:
                
                print("Tu puntuacion final es : ",suma)
                a = False
                borrarVentanaJuego(imagen,parar,seguir,textoA,textoB)
                 
                break
            if x<=-2 and x>=-6 and y<=-7 and y>=-9:
                borrarVentanaJuego(imagen,parar,seguir,textoA,textoB)
                break
        
    return suma
        
 #borrar objeto que estan en la ventana       
def borrarVentanaJuego(imagen,parar,seguir,textoA,textoB):
    imagen.undraw()
    parar.undraw()
    seguir.undraw()
    textoA.undraw()
    textoB.undraw()
      
def recordNuevo(score,nombre,palabras):
    if score > int(palabras[1]):
        import os
        file = open("record.txt","w")
        file.write(nombre+","+str(score)+os.linesep)
        file.close
        a=True
        return a
        
def ventana3(win,score,nombre,palabras):
    
    a = recordNuevo(score,nombre,palabras)
    palabras = textoArchivo()
    perdiste = ["P","E","R","D","I","S","T","E"]
    listaPerdiste=[]
    borrar = Rectangle(Point(-10,-10),Point(10,10)).draw(win)
    borrar.setFill("black")
    
    if score > 0:
        
        #texto score y puntuacion
        textoAscore=Text(Point(0,8),"SCORE").draw(win)
        textoAscore.setFill("Red")
        sleep(.5)
        textoBscore=Text(Point(0,6),str(score)).draw(win)
        textoBscore.setFill("white")
        sleep(.5)
        textoRecordnuevo = Text(Point(0,2),"RECORD").draw(win)
        textoRecordnuevo.setFill("blue")
        sleep(.5)
        textoRecordnumero = Text(Point(0,0),palabras[0]+" : "+palabras[1]).draw(win)
        textoRecordnumero.setFill("white")
             
        if a == True:
            sleep(.5)
            textoRecordnuevo = Text(Point(0,2),"NEW RECORD").draw(win)
            textoRecordnuevo.setFill("blue")
            palabras = textoArchivo()
            sleep(.5)
            textoRecordnumero = Text(Point(0,0),palabras[0]+" : "+palabras[1]).draw(win)
            textoRecordnumero.setFill("white")
    else:
        for i in range(8):
            letra=Text(Point(-4+i,8),perdiste[i]).draw(win)
            letra.setFill("white")
            listaPerdiste.append(letra)
            sleep(.15)
       
        sleep(.5)    
        textoAscore=Text(Point(0,6),"SCORE").draw(win)
        textoAscore.setFill("Red")
        sleep(.5)
        textoBscore=Text(Point(0,4),str(score)).draw(win)
        textoBscore.setFill("white")
        sleep(.5)
        textoRecordnuevo = Text(Point(0,2),"RECORD").draw(win)
        textoRecordnuevo.setFill("blue")
        sleep(.5)
        textoRecordnumero = Text(Point(0,0),palabras[0]+" : "+palabras[1]).draw(win)
        textoRecordnumero.setFill("white")
            
    #botones de volver a jugar o salir
    salir = Rectangle(Point(2,-7),Point(6,-9)).draw(win)
    salir.setFill("Red")
    textoAsalir=Text(Point(4,-8),"Salir").draw(win)
    repetir= Rectangle(Point(-2,-7),Point(-6,-9)).draw(win)
    repetir.setFill("Blue")
    textoBrepetir=Text(Point(-4,-8),"Jugar de\nnuevo").draw(win)
    
    #funciona para que solo los 2 botones reconozca el clickPoint
    while True:
        
        clickPoint = win.getMouse()
        x = clickPoint.getX()
        y = clickPoint.getY()
        
        #cuando no quieres volver a jugar
        if x>=2 and x<=6 and y<=-7 and y>=-9:
            if score>1:
                borrarVentana3(textoAscore,textoBscore,salir,repetir,textoAsalir,textoBrepetir,textoRecordnuevo,textoRecordnumero)
            else:
                borrarVentana3(textoAscore,textoBscore,salir,repetir,textoAsalir,textoBrepetir,textoRecordnuevo,textoRecordnumero)
                for i in range(8):
                    listaPerdiste[i].undraw()
            
            despedida= Text(Point(0,0),"GRACIAS POR JUGAR").draw(win)
            despedida.setFill("pink")
            
            sleep(1)
            win.close()
            break
        
        #volver a jugar
        if x<=-2 and x>=-6 and y<=-7 and y>=-9:
            if score>1:
                
                borrarVentana3(textoAscore,textoBscore,salir,repetir,textoAsalir,textoBrepetir,textoRecordnuevo,textoRecordnumero)
            else:
                borrarVentana3(textoAscore,textoBscore,salir,repetir,textoAsalir,textoBrepetir,textoRecordnuevo,textoRecordnumero)
                for i in range(8):
                    listaPerdiste[i].undraw()
          
            score = ventanaJuego(win,nombre,palabras) #se juega otra vez
            ventana3(win,score,nombre,palabras)# se repite el ciclo para ver si repite o no
            
#borrar todo impleentado en la ventana 3
def borrarVentana3(textoAscore,textoBscore,salir,repetir,textoAsalir,textoBrepetir,textoRecordnuevo,textoRecordnumero):
    
        textoAscore.undraw()
        textoBscore.undraw()    
        salir.undraw()
        repetir.undraw()
        textoAsalir.undraw()
        textoBrepetir.undraw()
        textoRecordnuevo.undraw()
        textoRecordnumero.undraw()
                
def main():
    
    #saber el record
    palabras = textoArchivo()
    
    #crear ventana grafica
    win= GraphWin("Dado",800,600)
    win.setCoords(-10,-10,10,10)
    win.setBackground("black")
    
    VentanaBienvenida(win)
    
    #ventana donde el usuario pone su nombre por si hace un record 
    nombre = VentanaNombre(win)
    
    #ventana juego y devulve score  que se va utulizar en la def puntuacion()
    score = ventanaJuego(win,nombre,palabras)
    
    #ventana  de score y boton de volver a jugar o salir 
    ventana3(win,score,nombre,palabras)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()