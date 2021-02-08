# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:53:21 2021

@author: KEVIN
"""

import tkinter as tk
#from tkinter.messagebox import showinfo


vent = tk.Tk()                 #crear venytana
vent.geometry('750x600')

vent.title('Plan de Vuelo')    #agregar titulo
vent.config(bg= 'silver')

###########################################################################
#Agregar etiqueta 1
etiq1 = tk.Label(vent, text='Distancia focal (mm)', bg='silver',  fg='black')
etiq1.grid(row = 0, column = 0, padx = (50,50))

  #Agregar caja 1
entry1 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry1.grid(row = 1, column = 0)

############################################################################
#Agregar etiqueta 2
etiq2 = tk.Label(vent, text='Ancho de imagen (pixel)', bg='silver',  fg='black')
etiq2.grid(row = 0, column = 1)

   #Agregar caja 2
entry2 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry2.grid(row = 1, column = 1)

#############################################################################
#Agregar etiqueta 3
etiq3 = tk.Label(vent, text='Ancho de imagen (pixel)', bg='silver',  fg='black')
etiq3.grid(row = 0, column = 2)

   #Agregar caja 3
entry3 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry3.grid(row = 1, column = 2)

#############################################################################
#Agregar etiqueta 4
etiq4 = tk.Label(vent, text='Ancho del sensor (mm)', bg='silver',  fg='black')
etiq4.grid(row = 2, column = 0)

   #Agregar caja 4
entry4 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry4.grid(row = 3, column = 0)

############################################################################
#Agregar etiqueta 5
etiq5 = tk.Label(vent, text='Alto del sensor (mm)', bg='silver',  fg='black')
etiq5.grid(row = 2, column = 1)

   #Agregar caja 5
entry5 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry5.grid(row = 3, column = 1)

############################################################################
#Agregar etiqueta 6
etiq6 = tk.Label(vent, text='Altura de vuelo (m)', bg='silver',  fg='black')
etiq6.grid(row = 2, column = 2, padx = (50,50))

   #Agregar caja 6
entry6 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry6.grid(row = 3, column = 2)

############################################################################
#Agregar etiqueta 7
etiq7 = tk.Label(vent, text='Solape longitudinal (%)', bg='silver',  fg='black')
etiq7.grid(row = 4, column = 0)

   #Agregar caja 7
entry7 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry7.grid(row = 5, column = 0)

#############################################################################
#Agregar etiqueta 8
etiq8 = tk.Label(vent, text='Solape transversal (%)', bg='silver',  fg='black')
etiq8.grid(row = 4, column = 1)

   #Agregar caja 8
entry8 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry8.grid(row = 5, column = 1)

#############################################################################
#Agregar etiqueta 9
etiq9 = tk.Label(vent, text='Largo parcela (m)', bg='silver',  fg='black')
etiq9.grid(row = 4, column = 2)

   #Agregar caja 9
entry9 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry9.grid(row = 5, column = 2)

##############################################################################
#Agregar etiqueta 10
etiq10 = tk.Label(vent, text='Ancho parcela (m)', bg='silver',  fg='black')
etiq10.grid(row = 6, column = 0)

   #Agregar caja 10
entry10 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry10.grid(row = 7, column = 0)

##############################################################################
#Agregar etiqueta 11
etiq11 = tk.Label(vent, text='Velocidad de vuelo (m/s)', bg='silver',  fg='black')
etiq11.grid(row = 6, column = 1)

   #Agregar caja 11
entry11 = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
entry11.grid(row = 7, column = 1)

##############################################################################

textResult = tk.Text(vent, bg = 'black')
textResult.grid(row = 8, column = 0, columnspan = 3, padx = (50,50), pady = (20,20))

vent.mainloop()







