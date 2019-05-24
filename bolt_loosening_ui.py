#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 24, 2019 10:33:17 PM IST  platform: Windows NT

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

import bolt_loosening_ui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = bolt_loosening_main (root)
    bolt_loosening_ui_support.init(root, top)
    root.mainloop()

w = None
def create_bolt_loosening_main(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = bolt_loosening_main (w)
    bolt_loosening_ui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_bolt_loosening_main():
    global w
    w.destroy()
    w = None

class bolt_loosening_main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1365x680+287+105")
        top.title("Evaluating Bolt-loosening")
        top.configure(background="#d8ba27")

        self.openfileFrame = tk.LabelFrame(top)
        self.openfileFrame.place(relx=0.007, rely=0.015, relheight=0.081
                , relwidth=0.989)
        self.openfileFrame.configure(relief='groove')
        self.openfileFrame.configure(foreground="black")
        self.openfileFrame.configure(text='''Open an Image File''')
        self.openfileFrame.configure(background="#d9d9d9")
        self.openfileFrame.configure(highlightcolor="#000000")
        self.openfileFrame.configure(width=1350)

        self.lblFileLocation = tk.Label(self.openfileFrame)
        self.lblFileLocation.place(relx=0.17, rely=0.364, height=21, width=783
                , bordermode='ignore')
        self.lblFileLocation.configure(background="#d9d9d9")
        self.lblFileLocation.configure(disabledforeground="#a3a3a3")
        self.lblFileLocation.configure(foreground="#000000")
        self.lblFileLocation.configure(text='''File Location''')
        self.lblFileLocation.configure(width=783)

        self.btnBrowse = tk.Button(self.openfileFrame)
        self.btnBrowse.place(relx=0.763, rely=0.364, height=24, width=107
                , bordermode='ignore')
        self.btnBrowse.configure(activebackground="#ececec")
        self.btnBrowse.configure(activeforeground="#000000")
        self.btnBrowse.configure(background="#d9d9d9")
        self.btnBrowse.configure(disabledforeground="#a3a3a3")
        self.btnBrowse.configure(foreground="#000000")
        self.btnBrowse.configure(highlightbackground="#d9d9d9")
        self.btnBrowse.configure(highlightcolor="black")
        self.btnBrowse.configure(pady="0")
        self.btnBrowse.configure(text='''Browse File''')
        self.btnBrowse.configure(width=107)

        self.lab56 = tk.Label(top)
        self.lab56.place(relx=0.007, rely=0.103, height=540, width=330)
        self.lab56.configure(background="#d9d9d9")
        self.lab56.configure(disabledforeground="#a3a3a3")
        self.lab56.configure(foreground="#000000")
        self.lab56.configure(text='''Original Image''')
        self.lab56.configure(width=330)

        self.lab57 = tk.Label(top)
        self.lab57.place(relx=0.256, rely=0.103, height=540, width=330)
        self.lab57.configure(activebackground="#f9f9f9")
        self.lab57.configure(activeforeground="black")
        self.lab57.configure(background="#d9d9d9")
        self.lab57.configure(disabledforeground="#a3a3a3")
        self.lab57.configure(foreground="#000000")
        self.lab57.configure(highlightbackground="#d9d9d9")
        self.lab57.configure(highlightcolor="black")
        self.lab57.configure(text='''Edge Image''')
        self.lab57.configure(width=330)

        self.lab58 = tk.Label(top)
        self.lab58.place(relx=0.505, rely=0.103, height=540, width=330)
        self.lab58.configure(activebackground="#f9f9f9")
        self.lab58.configure(activeforeground="black")
        self.lab58.configure(background="#d9d9d9")
        self.lab58.configure(disabledforeground="#a3a3a3")
        self.lab58.configure(foreground="#000000")
        self.lab58.configure(highlightbackground="#d9d9d9")
        self.lab58.configure(highlightcolor="black")
        self.lab58.configure(text='''Identified Nut & Bolt''')
        self.lab58.configure(width=330)

        self.lab59 = tk.Label(top)
        self.lab59.place(relx=0.755, rely=0.103, height=540, width=330)
        self.lab59.configure(activebackground="#f9f9f9")
        self.lab59.configure(activeforeground="black")
        self.lab59.configure(background="#d9d9d9")
        self.lab59.configure(disabledforeground="#a3a3a3")
        self.lab59.configure(foreground="#000000")
        self.lab59.configure(highlightbackground="#d9d9d9")
        self.lab59.configure(highlightcolor="black")
        self.lab59.configure(text='''Result''')
        self.lab59.configure(width=330)

        self.operationsFrame = tk.LabelFrame(top)
        self.operationsFrame.place(relx=0.007, rely=0.912, relheight=0.081
                , relwidth=0.989)
        self.operationsFrame.configure(relief='groove')
        self.operationsFrame.configure(font="-family {Segoe UI} -size 12 -weight bold -underline 1")
        self.operationsFrame.configure(foreground="black")
        self.operationsFrame.configure(text='''OPERATIONS''')
        self.operationsFrame.configure(background="#d9d9d9")
        self.operationsFrame.configure(width=1350)

        self.btnEdge = tk.Button(self.operationsFrame)
        self.btnEdge.place(relx=0.378, rely=0.364, height=24, width=74
                , bordermode='ignore')
        self.btnEdge.configure(activebackground="#ececec")
        self.btnEdge.configure(activeforeground="#000000")
        self.btnEdge.configure(background="#d9d9d9")
        self.btnEdge.configure(disabledforeground="#a3a3a3")
        self.btnEdge.configure(foreground="#000000")
        self.btnEdge.configure(highlightbackground="#d9d9d9")
        self.btnEdge.configure(highlightcolor="black")
        self.btnEdge.configure(pady="0")
        self.btnEdge.configure(text='''Edge Detect''')

        self.btnNut = tk.Button(self.operationsFrame)
        self.btnNut.place(relx=0.459, rely=0.364, height=24, width=114
                , bordermode='ignore')
        self.btnNut.configure(activebackground="#ececec")
        self.btnNut.configure(activeforeground="#000000")
        self.btnNut.configure(background="#d9d9d9")
        self.btnNut.configure(disabledforeground="#a3a3a3")
        self.btnNut.configure(foreground="#000000")
        self.btnNut.configure(highlightbackground="#d9d9d9")
        self.btnNut.configure(highlightcolor="black")
        self.btnNut.configure(pady="0")
        self.btnNut.configure(text='''Detect Nut & Bolt''')
        self.btnNut.configure(width=114)

        self.btnEvaluate = tk.Button(self.operationsFrame)
        self.btnEvaluate.place(relx=0.578, rely=0.364, height=24, width=74
                , bordermode='ignore')
        self.btnEvaluate.configure(activebackground="#ececec")
        self.btnEvaluate.configure(activeforeground="#000000")
        self.btnEvaluate.configure(background="#d80000")
        self.btnEvaluate.configure(disabledforeground="#a3a3a3")
        self.btnEvaluate.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.btnEvaluate.configure(foreground="#000000")
        self.btnEvaluate.configure(highlightbackground="#d9d9d9")
        self.btnEvaluate.configure(highlightcolor="#000000")
        self.btnEvaluate.configure(pady="0")
        self.btnEvaluate.configure(text='''Evaluate''')

if __name__ == '__main__':
    vp_start_gui()





