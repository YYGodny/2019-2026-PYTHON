import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#window
window = ttk.Window(themename='darkly')
window.title('To do!')
window.geometry('1000x600')

#title
title_label = ttk.Label(master = window, text = 'FAG', font = 'Calibri 48 bold')
title_label.pack()

#fag
fag_frame = ttk.Frame(master = window)
fag_frame.pack(expand=True, fill='both')

#matte
matte = ttk.Frame(master = fag_frame)
matte_title = ttk.Label(master = matte, text = 'MATTE', background='blue')
matte.pack(side='left')
matte_title.pack()

#naturfag
naturfag = ttk.Frame(master = fag_frame)
naturfag_title = ttk.Label(master = naturfag, text = 'NATURFAG', background='red')
naturfag.pack(side='left')
naturfag_title.pack()


#run
window.mainloop()
