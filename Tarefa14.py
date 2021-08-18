from tkinter import *
import numpy as np
import matplotlib
import tkinter as tk
import tkinter.ttk as ttk
import entrada as ent
import math

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

janela=Tk()
janela.title("Tarefa 14(Instrumentação II)_Luísa")
#janela.geometry("1000x1000")
janela.configure(bg='magenta',background='grey')

figure=Figure(figsize=(5,4),dpi=100)
plot=figure.add_subplot(1,1,1)

x=np.linspace(2,8,4)
y=x*10
plot.plot(x,y,color="brown",marker=".",linestyle="")
plot.set_title("Gráfico de área X largura.")
plot.set_xlabel('Largura(m)')
plot.set_ylabel('Área(m²)')

area=tk.Label(janela, text="FORMATO DA HORTA", bg="pink")
area.grid(row=1,column=0,pady=20,padx=50)
area.configure(font=("Microsoft JhengHei UI", 10))

texto1=Label(janela,text="ESCOLHA A LARGURA DA HORTA:",pady=25, padx=25,background='pink')
texto1.grid(row=0,column=2,columnspan=3,rowspan=3,sticky=W+E,pady=20,padx=50)
texto1.configure(font=("Microsoft JhengHei UI", 10))

unit=tk.StringVar()
unit_box=ttk.Combobox(janela,width=23,textvariable=unit,state="readonly")
unit_box["values"]=("2","4","6","8")
unit_box.current(0)
unit_box.grid(row=1,column=2,columnspan=2)


def calcula():
    ans=ent.calcula(unit.get())
    global ans_frame
    ans_frame = tk.Frame(janela, width=50, height=50)
    ans_frame.grid(row=2, column=2, columnspan=3, pady=25, padx=25)
    win = tk.Label(ans_frame, text="A área é: {} m²".format(ans), background='pink')
    win.grid(row=0, column=0)


def clear():
    resultado.destroy()
    pass
def close_window():
    janela.destroy()
    pass
convert_btn=ttk.Button(janela,text="Calcular", command=calcula,cursor="heart")
convert_btn.grid(row=1,column=4)

canvas=FigureCanvasTkAgg(figure,janela)
canvas.get_tk_widget().grid(row=0,column=0)

canvas1=Canvas(janela, bg="green",height=150,width=250)
arc=canvas1.create_rectangle(5,0,5,0,fill="red")
canvas1.grid(row=2,column=0)

def clear():
    ans_frame.destroy()
    pass

def close_window():
    janela.destroy()

botao = tk.Button(text = "Fechar janela", command = close_window,relief=SUNKEN,cursor="heart")
botao.grid(row=3,column=3,rowspan=3,pady=15)
clear_btn=ttk.Button(janela,text="Limpar", command=clear,cursor="heart")
clear_btn.grid(row=2,column=4,rowspan=2,pady=20)



janela.mainloop()