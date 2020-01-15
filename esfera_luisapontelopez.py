#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:50:34 2019

@author: luisapontelopez
"""

from graphics import*
import math

def main():
    
    #dibujar ventana
    
    win = GraphWin("Calculadora de area y volumen", 400,300)#eso numero de 400 y 300 se refiere a pixeles
    win.setCoords(0,0,3,6)
    
    #dibujar la interfaz
    
    Text(Point(1,5),"Entre el radio de la esfera: : ").draw(win)
    Text(Point(1,3),"El area es:    ").draw(win)
    Text(Point(1,1),"El volumen es: ").draw(win)
    
    
    
    inputText = Entry(Point(2.25,5),5)# el 5 dice el tama~o de la ventana o cuadrito
    inputText.setText("0.0")# le asigne una propiedad 
    inputText.draw(win)
    
    Area = Text(Point(2.25,3),"").draw(win)
    
    Volumen= Text(Point(2.25,1),"").draw(win)
    
    
    button = Text(Point(1.5,4.0),"Calcula")
    button.draw(win)
    
    Rectangle(Point(1,3.5),Point(2,4.5)).draw(win)
    
    win.getMouse()
    
    
    #convertir de C a F
    R= eval(inputText.getText())
    A = math.pi*R**2
    V  = (4/3)*math.pi*R**3
   
    
    #mostrar la salida

    Area.setText(round(A,2))
    Volumen.setText(round(V,2))
    button.setText("Quit")
    
    #terminar 
    win.getMouse()
    win.close()
    
    
    
main()