import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#window
window = ttk.Window(themename='solar')
window.title('To do!')
window.geometry('1000x600')

#title
title_label = ttk.Label(window, text = 'FAG', font = 'Calibri 48 bold', background = 'blue', anchor = 'center')
title_label.pack(fill='x')

#fag
fag_frame = ttk.Frame(window)
fag_frame.pack(expand=True, fill='both')


class Fag:
    def __init__(self, fag, farge):
        self.navn = fag
        self.farge = farge
        self.todoos = []

#matte
matte_frame = ttk.Frame(fag_frame)
matte_tittel = ttk.Label(matte_frame, text = 'Matte', background ='light blue')

#matte_tittel.place(x = 0, y = 0, width=100, height = 50)
matte_tittel.pack(fill='x')
matte_frame.pack(side = 'left', expand=True, fill='both')

#naturfag
naturfag_frame = ttk.Frame(fag_frame)
naturfag_tittel = ttk.Label(naturfag_frame, text = 'Naturfag', background ='green')

#naturfag_tittel.place(x = 0, y = 0, width=100, height = 50)
naturfag_tittel.pack(fill='x')
naturfag_frame.pack(side = 'left', expand=True, fill='both')

#norsk
norsk_frame = ttk.Frame(fag_frame)
norsk_tittel = ttk.Label(norsk_frame, text = 'Norsk', background ='red')

#norsk_tittel.place(x = 0, y = 0, width=100, height = 50)
norsk_tittel.pack(fill='x')
norsk_frame.pack(side = 'left', expand=True, fill='both')


#run
window.mainloop()
