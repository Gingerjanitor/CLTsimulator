# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:01:04 2023

@author: Matt0
"""
import tkinter as tk
import gui.initparams as initparams

class CLTsimulation(initparams.mixin): 
    def __init__(self,master):
        self.master=master
        self.entry(master)
        
    def tempprint(self):
        print(self.mean.get())
        print(self.sd.get())


runit=tk.Tk()
runit.eval('tk::PlaceWindow . center')
gui=CLTsimulation(runit)