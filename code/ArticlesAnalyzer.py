import tkinter as tk
from tkinter import *
import Analyzer
import Extractor
import Vizualizator

"""
Функция отображает окно ввода данных для работы с базой данных
"""
def ImportDbBox():
    textbox = tk.Tk()
    textbox.title = "Extracting data"
    textbox.geometry("500x300")
    label1 = tk.Label(textbox, text="Input username:")
    label2 = tk.Label(textbox, text="Input password:")
    label3 = tk.Label(textbox, text="Input database name:")
    txt1 = Entry(textbox, width=20)
    txt2 = Entry(textbox, width=20)
    txt3 = Entry(textbox, width=20)
    btn = tk.Button(textbox, text='Export data from database', width=20, height=5, bg="Sky blue2", fg="black",
                    command=lambda: (Extractor.ExportDB(txt1.get(), txt2.get(), txt3.get()))).place(relx=.35, rely=.5)
    label1.pack()
    txt1.pack()
    label2.pack()
    txt2.pack()
    label3.pack()
    txt3.pack()
    textbox.mainloop()

"""
Функция отображает основное окно 
"""
def Start():
    window = tk.Tk()
    window.title = "Articles analyzer"
    window.geometry("500x400")
    btn1 = tk.Button(window,
                     text='Extract data',
                     width=25,
                     height=5,
                     bg="Sky blue2",
                     fg="black",
                     command=ImportDbBox).place(relx=.3, rely=.1)
    btn2 = tk.Button(window,
                     text='Start clusterization',
                     width=25,
                     height=5,
                     bg="Sky blue2",
                     fg="black",
                     command=Analyzer.Analyzer).place(relx=.3, rely=.4)
    btn3 = tk.Button(window,
                     text='Show results',
                     width=25,
                     height=5,
                     bg="Sky blue2",
                     fg="black",
                     command=Vizualizator.Vizualize).place(relx=.3, rely=.7)
    window.mainloop()


Start()
