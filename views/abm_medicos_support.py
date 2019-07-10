#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#    Jul 03, 2019 01:12:43 PM -03  platform: Windows NT

import sys
import controllers.Medico as ctrl

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

def set_Tk_var():
    global medicoNombre
    medicoNombre = tk.StringVar()
    global medicoApellido
    medicoApellido = tk.StringVar()
    global especialidad
    especialidad = tk.StringVar()
    global matricula
    matricula = tk.StringVar()

def nuevoMedico():
    success = ctrl.crearMedico(medicoNombre.get(),medicoApellido.get(),especialidad.get(),matricula.get())
    if (success != None) :
        print("Se creo exitosamente")
        import views.abm_medicos as abm_medicos
        abm_medicos.top.insertarUltimo(success)
        abm_medicos.top.clear()
    else :
        print("Error en la creacion del medico")

def getAll():
    return ctrl.buscarAllMedicos()

def destroy_window():
    print('abm_medicos_support.destroy_window')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import abm_medicos
    abm_medicos.vp_start_gui()



