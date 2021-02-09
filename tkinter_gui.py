# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:36:49 2021

@author: KEVIN
"""

import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo

vent = tk.Tk()               #crear ventana
vent.geometry('800x600')

vent.title('Mi primer GUI')    #agregar titulo
vent.config(bg= 'blue')

eti = tk.Label(vent, text = 'Hola Mundo')   #agregar etiqueta
eti.pack()

cajatext = tk.Entry(vent, font = 'Calibri 20', justify = 'center')  #agregar caja de texto
cajatext.pack()

nombre_Label = tk.Label(vent)
nombre_Label.pack()

def get_text():               #funcion que recupera lo que se escribe en la caja
    texto = cajatext.get()
    nombre_Label['text'] = f'Hola {texto}'

boton1 = tk.Button(vent, text = 'Click', command = get_text)


#def saludo(nombre):           #funcion que imprime en la consola
#    print('Hola ' + nombre)
    
#boton1 = tk.Button(vent, text = 'Click', command = lambda: saludo('Jose'))
boton1.pack()

folder_path = tk.StringVar()

#def browsedir_button():
    #filedir = filedialog.askdirectory()
#    filedir = filedialog.askopenfile()
#    filename = filedir.name
#    folder_path.set(filename)

#botondir = tk.Button(text = 'Buscar Dir', command = browsedir_button)
#botondir.pack()

#textdir = tk.Entry(vent, textvariable = folder_path, width=40)
#textdir.pack()

def contar10():
    for i in range (10):
        valor = f'{i}\n'
        texto10.insert(tk.END, valor)

botoncount = tk.Button(text = 'Contar 10', command = contar10)
botoncount.pack()

texto10 = tk.Text(vent)
texto10.pack()

#Crear una ventana popup

#def popup_window():
#    win = tk.Toplevel()
#    win.wm_title('PopUp')
#    l = tk.Label(win , text ='Nueva ventana')
#    l.pack()
#    b = tk.Button(win , text = 'Exit', command = win.destroy)
#    b.pack()
    
def popup_showinfo():
    num1 = 5
    num2 = 10
    message = f'{num1} + {num2} = {num1+num2}'
    #result1 = num1 + num2
    showinfo("Suma", message)
    
button_showinfo = tk.Button(text ="Show Info ", command = popup_showinfo)
button_showinfo.pack()

vent.mainloop()






 