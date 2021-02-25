#coding utf8
import tkinter as tk
import sqlite3
import os


def Menu():
    fenetre = tk.Tk()
    label = tk.Label(fenetre, text="Bienvenu !")
    b_executer = tk.Button(fenetre, text="exectuer", command=Executer())
    b_modif = tk.Button(fenetre, text="Modifications",command=Modifications)
    b_sortie = tk.Button(fenetre, text="Quitter", command=fenetre.destroy)
    label.pack()
    b_executer.pack()
    b_modif.pack()
    b_sortie.pack()
    fenetre.mainloop()  

def Executer():
    print('OK')

def Modifications():
    print('OK2')

if __name__ == '__main__':
    Menu()