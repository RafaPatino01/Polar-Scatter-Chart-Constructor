#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:26:00 2020

@author: rafaelpatino
"""

import tkinter
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

class Ventana:
    def createWindow(self):
        self.randomData = False
        self.Seleccionado = False
        self.window = tkinter.Tk()
        self.window.title("Gráfica Polar")
        self.window.geometry("780x400")
        
        #Labels
        self.label00 = tkinter.Label(self.window, text = "Generador de gráfica polar")
        self.label00.place(x = 10, y = 10)
        self.label00.config(font=("Helvetica", 23))
        
        #TITULO
        self.label01 = tkinter.Label(self.window, text = "Título del gráfico:")
        self.label01.place(x = 10, y = 50)
        self.label01.config(font=("Helvetica", 15))
        
        self.Entry_Title = tkinter.Entry(self.window,width=13)
        self.Entry_Title.place(x = 175, y = 50)
        
        #CANTIDAD DE PUNTOS
        self.label02 = tkinter.Label(self.window, text = "Cantidad de puntos:")
        self.label02.place(x = 10, y = 80)
        self.label02.config(font=("Helvetica", 15))
        
        self.Entry_Puntos = tkinter.Entry(self.window,width=10)
        self.Entry_Puntos.place(x = 175, y = 80)
        
        #TAMAÑO DE PUNTOS
        self.label03 = tkinter.Label(self.window, text = "Tamaño de punto:")
        self.label03.place(x = 10, y = 110)
        self.label03.config(font=("Helvetica", 15))
        
        self.Entry_Size = tkinter.Entry(self.window,width=10)
        self.Entry_Size.place(x = 175, y = 110)
        
        #COLOR DEL TEMA
        self.color = 1
        
        self.label04 = tkinter.Label(self.window, text = "Color:")
        self.label04.place(x = 10, y = 150)
        self.label04.config(font=("Helvetica", 15))
        
        
        self.btn01 = tkinter.Button(self.window,text = "Aleatorio",command = self.btn01_click)
        self.btn01.place(x = 70, y = 150)
        
        self.btn02 = tkinter.Button(self.window,text = "B/N",command = self.btn02_click)
        self.btn02.place(x = 142, y = 150)
        
        self.btn03 = tkinter.Button(self.window,text = "Azul",command = self.btn03_click)
        self.btn03.place(x = 180, y = 150)
        
        self.btn04 = tkinter.Button(self.window,text = "Verde",command = self.btn04_click)
        self.btn04.place(x = 220, y = 150)
        
        self.btn05 = tkinter.Button(self.window,text = "Rojo",command = self.btn05_click)
        self.btn05.place(x = 270, y = 150)
        
        #TIPO DE DATO:
        self.label05 = tkinter.Label(self.window, text = "Datos:")
        self.label05.place(x = 10, y = 190)
        self.label05.config(font=("Helvetica", 15))
        
        self.btn08 = tkinter.Button(self.window,text = "Aleatorio",command = self.btn08_click)
        self.btn08.place(x = 70, y = 190)
        
        self.btn09 = tkinter.Button(self.window,text = "Ingresar",command = self.btn09_click)
        self.btn09.place(x = 142, y = 190)
        
        #Mensaje de puntos
        self.Label_Added = tkinter.Label(self.window, text = "(No seleccionado)")
        self.Label_Added.place(x = 10, y = 225)
        self.Label_Added.config(font=("Helvetica", 15))
        
        #BOTON DE CREAR / RESET
        self.btn06 = tkinter.Button(self.window,text = "Crear gráfico", command=self.btn06_click)
        self.btn06.place(x = 10, y = 270)
        self.btn06.config(height=2, width = 35)
        
        self.btn07 = tkinter.Button(self.window,text = "Reset", command = self.btnReset_click)
        self.btn07.place(x = 10, y = 320)
        self.btn07.config(height=2, width = 35)
        
        self.window.mainloop()
       
    #MÉTODOS DE LOS BOTONES
    def btnReset_click(self):
        self.window.destroy()
        self.createWindow()
        
    def btn01_click(self):
        self.color = 1
    def btn02_click(self):
        self.color = 2
    def btn03_click(self):
        self.color = 3
    def btn04_click(self):
        self.color = 4
    def btn05_click(self):
        self.color = 5
        
    def btn06_click(self):
        if self.Seleccionado:
            if self.randomData:
                self.makeGraph(self.randomData)
                self.open_img()
            else:
                self.makeGraph(self.randomData,p_r = self.dataR,p_theta = self.dataTheta)
                self.open_img()
        else:
            tkinter.messagebox.showinfo(title=None, message="No has definido puntos")
            
    
    #BOTON PARA SELECCIONAR RANDOM
    def btn08_click(self):
        self.randomData = True
        self.Seleccionado = True
        
        self.OtherLabel_Added = tkinter.Label(self.window, text = "(Puntos Aleatorios)")
        self.OtherLabel_Added.place(x = 10, y = 225)
        self.OtherLabel_Added.config(font=("Helvetica", 15))
    
    #BOTON PARA INGRESAR DATOS
    def btn09_click(self):
        
        def New_Window(self):
            self.n = (int(self.Entry_Puntos.get()))
            if(self.n > 15):
                self.n = 15
            y = self.n*30
            
            self.InputWindow = tkinter.Tk()
            self.InputWindow.title("Ingresar Puntos")
            self.InputWindow.geometry("300x"+str(y+120))
            
            def CreateEntries(n):
                self.Entry_R = []
                self.Entry_Theta = []
                self.New_Labels = []
                vertical = 40
                for i in range(0,n):
                    self.Entry_R.append(tkinter.Entry(self.InputWindow,width=8))
                    self.Entry_Theta.append(tkinter.Entry(self.InputWindow,width=8))
                    self.New_Labels.append(tkinter.Label(self.InputWindow, text = str(i+1)))
                    
                    self.Entry_R[i].place(x = 60, y = vertical)
                    self.Entry_Theta[i].place(x = 180, y = vertical)
                    self.New_Labels[i].place(x = 10, y = vertical)
                    vertical += 32
            
            self.Label_R = tkinter.Label(self.InputWindow, text = "Distancia")
            self.Label_R.place(x = 60, y = 10)
            self.Label_R.config(font=("Helvetica", 15))
            
            self.Label_Theta = tkinter.Label(self.InputWindow, text = "Grados")
            self.Label_Theta.place(x = 180, y = 10)
            self.Label_Theta.config(font=("Helvetica", 15))
            
            #CREA N NÚMERO DE ENTRADAS
            Cantidad = int(self.Entry_Puntos.get())
            if Cantidad > 15:
                Cantidad = 15
            CreateEntries(Cantidad)
            
            altura = Cantidad*31
            
            self.OK = tkinter.Button(self.InputWindow,text = "OK", command=self.OK_Clicked)
            self.OK.place(x = 10, y = altura+60)
            self.OK.config(height=2, width = 30)
            
            self.InputWindow.mainloop()
        
        #n = int(self.Entry_Puntos.get())
        New_Window(self)
        
        
    def OK_Clicked(self):
        #LABEL VENTANA PRINCIPAL "n Puntos añadidos"
        self.newLabel_Added = tkinter.Label(self.window, text = "(" + str(self.n) + " puntos añadidos)")
        self.newLabel_Added.place(x = 10, y = 225)
        self.newLabel_Added.config(font=("Helvetica", 15))
        
        self.Seleccionado = True
        self.randomData = False
        
        tkinter.messagebox.showinfo(title=None, message="Puntos Correctamente añadidos")
        
        self.dataR = []
        self.dataTheta = []
        
        for i in range(0,int(self.Entry_Puntos.get())):
            self.dataR.append(int(self.Entry_R[i].get()))
            self.dataTheta.append(int(self.Entry_Theta[i].get()))
        
        self.InputWindow.destroy()
        
        
    
    #HACER GRÁFICA
    def makeGraph(self,random,p_r = [], p_theta = []):
        title = str(self.Entry_Title.get())
        puntos = int(self.Entry_Puntos.get())
        size = int(self.Entry_Size.get())
        color = self.color
        N = puntos
        
        if(random == True):
            r = 2 * np.pi * np.random.rand(N) #DISTANCIA DEL ORIGEN
            theta = 2 * np.pi * np.random.rand(N) #POSICIÓN EN EL CÍRCULO
        else:
            r = np.array(p_r)
            theta = np.array(p_theta)/(57.296)
            
        area = size * np.array([1]) #TAMAÑO DE PUNTO
        
        
        if color == 1:
            color = np.random.rand(N)
        elif color == 2:
            color = ["black"]*N
        elif color == 3:
            color = ["blue"]*N
        elif color == 4:
            color = ["green"]*N
        elif color == 5:
            color = ["red"]*N
        else:
            color = np.random.rand(N)
        
        fig = plt.figure(dpi = 200)
        ax = fig.add_subplot(projection = 'polar')
        ax.set_title(title,va='bottom',fontsize=30)
        graph = ax.scatter(theta, r, c = color, s = area, cmap = 'hsv', alpha = 0.75)
        plt.savefig('grafica.png')
    
    
    def openfn():
        filename = filedialog.askopenfilename(title='open')
        return filename
            
    def open_img(self):
        img = Image.open('grafica.png')
        img = img.resize((500, 330), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.window, image=img)
        panel.image = img
        panel.pack()
        panel.place(x=330,y=15)
        

        
VentanaPrincipal = Ventana()
VentanaPrincipal.createWindow()
        
