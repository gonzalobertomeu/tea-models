#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#    Jun 26, 2019 01:28:02 AM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import views.estudios_support as estudios_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    estudios_support.set_Tk_var()
    top = captura (root)
    estudios_support.init(root, top)
    root.mainloop()

w = None
def create_captura(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    estudios_support.set_Tk_var()
    top = captura (w)
    estudios_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_captura():
    global w
    w.destroy()
    w = None

class captura:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+436+167")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#ffffff")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.233, rely=0.089, relheight=0.096
                , relwidth=0.55)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Captura Gestos''')
        self.Message1.configure(width=330)

        self.paciente = ttk.Label(top)
        self.paciente.place(relx=0.067, rely=0.244, height=19, width=66)
        self.paciente.configure(background="#d9d9d9")
        self.paciente.configure(foreground="#000000")
        self.paciente.configure(font="TkDefaultFont")
        self.paciente.configure(relief="flat")
        self.paciente.configure(text='''Paciente''')

        self.nombrepac = ttk.Entry(top)
        self.nombrepac.place(relx=0.192, rely=0.233, relheight=0.047
                , relwidth=0.21)
        self.nombrepac.configure(takefocus="")
        

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.medico = ttk.Label(top)
        self.medico.place(relx=0.067, rely=0.322, height=19, width=66)
        self.medico.configure(background="#d9d9d9")
        self.medico.configure(foreground="#000000")
        self.medico.configure(font="TkDefaultFont")
        self.medico.configure(relief="flat")
        self.medico.configure(text='''Médico''')

        self.nombremed = ttk.Entry(top)
        self.nombremed.place(relx=0.192, rely=0.311, relheight=0.047
                , relwidth=0.21)
        self.nombremed.configure(takefocus="")
        

        self.gest = ttk.Label(top)
        self.gest.place(relx=0.075, rely=0.4, height=19, width=66)
        self.gest.configure(background="#d9d9d9")
        self.gest.configure(foreground="#000000")
        self.gest.configure(font="TkDefaultFont")
        self.gest.configure(relief="flat")
        self.gest.configure(text='''Gestos''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.g1 = ttk.Checkbutton(top)
        self.g1.place(relx=0.2, rely=0.4, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1.configure(variable=estudios_support.gesto1)
        self.g1.configure(takefocus="")
        self.g1.configure(text='''Gesto 1''')

        self.salir = ttk.Button(top)
        self.salir.place(relx=0.667, rely=0.8, height=25, width=76)
        self.salir.configure(command=estudios_support.destroy_window)
        self.salir.configure(takefocus="")
        self.salir.configure(text='''Salir''')

        self.g2 = ttk.Checkbutton(top)
        self.g2.place(relx=0.2, rely=0.489, relwidth=0.103, relheight=0.0
                , height=21)
        self.g2.configure(variable=estudios_support.gesto2)
        self.g2.configure(takefocus="")
        self.g2.configure(text='''Gesto 2''')

        self.g1_6 = ttk.Checkbutton(top)
        self.g1_6.place(relx=0.2, rely=0.578, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1_6.configure(variable=estudios_support.gesto3)
        self.g1_6.configure(takefocus="")
        self.g1_6.configure(text='''Gesto 3''')

        self.g1_7 = ttk.Checkbutton(top)
        self.g1_7.place(relx=0.2, rely=0.667, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1_7.configure(variable=estudios_support.gesto4)
        self.g1_7.configure(takefocus="")
        self.g1_7.configure(text='''Gesto 4''')

        self.g1_8 = ttk.Checkbutton(top)
        self.g1_8.place(relx=0.467, rely=0.4, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1_8.configure(variable=estudios_support.gesto5)
        self.g1_8.configure(takefocus="")
        self.g1_8.configure(text='''Gesto 5''')

        self.g1_9 = ttk.Checkbutton(top)
        self.g1_9.place(relx=0.467, rely=0.489, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1_9.configure(variable=estudios_support.gesto6)
        self.g1_9.configure(takefocus="")
        self.g1_9.configure(text='''Gesto 6''')

        self.g1_10 = ttk.Checkbutton(top)
        self.g1_10.place(relx=0.467, rely=0.578, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1_10.configure(variable=estudios_support.gesto7)
        self.g1_10.configure(takefocus="")
        self.g1_10.configure(text='''Gesto 7''')

        self.g1_11 = ttk.Checkbutton(top)
        self.g1_11.place(relx=0.467, rely=0.667, relwidth=0.103, relheight=0.0
                , height=21)
        self.g1_11.configure(variable=estudios_support.gesto8)
        self.g1_11.configure(takefocus="")
        self.g1_11.configure(text='''Gesto 8''')

        self.g1_12 = ttk.Checkbutton(top)
        self.g1_12.place(relx=0.733, rely=0.4, relwidth=0.12, relheight=0.0
                , height=21)
        self.g1_12.configure(variable=estudios_support.gesto9)
        self.g1_12.configure(takefocus="")
        self.g1_12.configure(text='''Gesto 9''')

        self.g1_13 = ttk.Checkbutton(top)
        self.g1_13.place(relx=0.733, rely=0.489, relwidth=0.12, relheight=0.0
                , height=21)
        self.g1_13.configure(variable=estudios_support.gesto10)
        self.g1_13.configure(takefocus="")
        self.g1_13.configure(text='''Gesto 10''')

        self.g1_14 = ttk.Checkbutton(top)
        self.g1_14.place(relx=0.733, rely=0.578, relwidth=0.12, relheight=0.0
                , height=21)
        self.g1_14.configure(variable=estudios_support.gesto11)
        self.g1_14.configure(takefocus="")
        self.g1_14.configure(text='''Gesto 11''')

        self.g1_15 = ttk.Checkbutton(top)
        self.g1_15.place(relx=0.733, rely=0.667, relwidth=0.12, relheight=0.0
                , height=21)
        self.g1_15.configure(variable=estudios_support.gesto12)
        self.g1_15.configure(takefocus="")
        self.g1_15.configure(text='''Gesto 12''')

        self.graba = ttk.Button(top)
        self.graba.place(relx=0.458, rely=0.8, height=25, width=76)
        self.graba.configure(takefocus="")
        self.graba.configure(text='''Grabar''')

        self.inicio = ttk.Button(top)
        self.inicio.place(relx=0.2, rely=0.8, height=25, width=106)
        self.inicio.configure(takefocus="")
        self.inicio.configure(text='''Iniciar estudio''')

if __name__ == '__main__':
    vp_start_gui()




