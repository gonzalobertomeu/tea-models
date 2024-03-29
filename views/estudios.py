#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#    Jul 11, 2019 08:23:27 PM -03  platform: Windows NT

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
import views.buscarpaciente as buscarpaciente
import views.buscarmedico as buscarmedico

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
    global w, w_win, rt, top
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
        top.title("captura")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#ffffff")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.233, rely=0.033, relheight=0.096
                , relwidth=0.55)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Estudio''')
        self.Message1.configure(width=330)

        self.paciente = ttk.Label(top)
        self.paciente.place(relx=0.067, rely=0.156, height=19, width=66)
        self.paciente.configure(background="#d9d9d9")
        self.paciente.configure(foreground="#000000")
        self.paciente.configure(font="TkDefaultFont")
        self.paciente.configure(relief="flat")
        self.paciente.configure(text='''Paciente''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.medico = ttk.Label(top)
        self.medico.place(relx=0.067, rely=0.222, height=19, width=66)
        self.medico.configure(background="#d9d9d9")
        self.medico.configure(foreground="#000000")
        self.medico.configure(font="TkDefaultFont")
        self.medico.configure(relief="flat")
        self.medico.configure(text='''Médico''')

        self.gest = ttk.Label(top)
        self.gest.place(relx=0.067, rely=0.289, height=19, width=66)
        self.gest.configure(background="#d9d9d9")
        self.gest.configure(foreground="#000000")
        self.gest.configure(font="TkDefaultFont")
        self.gest.configure(relief="flat")
        self.gest.configure(text='''Gestos''')

        self.salir = ttk.Button(top)
        self.salir.place(relx=0.75, rely=0.889, height=25, width=76)
        self.salir.configure(command=estudios_support.destroy_window)
        self.salir.configure(takefocus="")
        self.salir.configure(text='''Salir''')

        self.graba = ttk.Button(top)
        self.graba.place(relx=0.583, rely=0.889, height=25, width=76)
        self.graba.configure(takefocus="")
        self.graba.configure(text='''Grabar''')
        self.graba.configure(state='disabled')

        self.inicio = ttk.Button(top)
        self.inicio.place(relx=0.375, rely=0.889, height=25, width=106)
        self.inicio.configure(takefocus="")
        self.inicio.configure(text='''Iniciar captura''')

        self.muestraPaciente = ttk.Label(top)
        self.muestraPaciente.place(relx=0.233, rely=0.156, height=19, width=316)
        self.muestraPaciente.configure(background="#a09ed8")
        self.muestraPaciente.configure(foreground="#000000")
        self.muestraPaciente.configure(font="TkDefaultFont")
        self.muestraPaciente.configure(relief="flat")
        self.muestraPaciente.configure(textvariable=estudios_support.pacienteLabel)

        self.buscarPaciente = ttk.Button(top)
        self.buscarPaciente.place(relx=0.783, rely=0.144, height=25, width=66)
        self.buscarPaciente.configure(takefocus="")
        self.buscarPaciente.configure(text='''Buscar''')
        self.buscarPaciente.configure(command=self.abrirBuscarPaciente)

        self.buscarMedico = ttk.Button(top)
        self.buscarMedico.place(relx=0.783, rely=0.211, height=25, width=66)
        self.buscarMedico.configure(takefocus="")
        self.buscarMedico.configure(text='''Buscar''')
        self.buscarMedico.configure(command=self.abrirBuscarMedico)

        self.muestraMedico = ttk.Label(top)
        self.muestraMedico.place(relx=0.233, rely=0.222, height=19, width=316)
        self.muestraMedico.configure(background="#a09ed8")
        self.muestraMedico.configure(foreground="#000000")
        self.muestraMedico.configure(font="TkDefaultFont")
        self.muestraMedico.configure(relief="flat")
        self.muestraMedico.configure(textvariable=estudios_support.medicoLabel)

        self.listaGestos = ScrolledListBox(top)
        self.listaGestos.place(relx=0.183, rely=0.311, relheight=0.544
                , relwidth=0.652)
        self.listaGestos.configure(background="white")
        self.listaGestos.configure(disabledforeground="#a3a3a3")
        self.listaGestos.configure(font="TkFixedFont")
        self.listaGestos.configure(foreground="black")
        self.listaGestos.configure(highlightbackground="#d9d9d9")
        self.listaGestos.configure(highlightcolor="#d9d9d9")
        self.listaGestos.configure(selectbackground="#c4c4c4")
        self.listaGestos.configure(selectforeground="black")
        self.listaGestos.configure(width=10)

        self.calibraCamara = ttk.Button(top)
        self.calibraCamara.place(relx=0.125, rely=0.889, height=25, width=136)
        self.calibraCamara.configure(takefocus="")
        self.calibraCamara.configure(text='''Calibrar cámara''')
    def abrirBuscarMedico(self):
        buscarmedico.create_buscarMedico(root)

    def abrirBuscarPaciente(self):
        buscarpaciente.create_buscarPaciente(root)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





