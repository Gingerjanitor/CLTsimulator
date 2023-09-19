# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:01:04 2023

@author: Matt0
"""
import tkinter as tk
import pandas as pd

import gui.initparams as initparams
import funcs.GenDistribution as gendist
import funcs.graphit as graphit



class CLTsimulation(initparams.mixin,
                    gendist.gendist,
                    graphit.mixin): 
    def __init__(self,master):
        
        self.sample=pd.DataFrame()
        self.tickstatus = tk.IntVar()

        
        self.master=master
        self.entry(master)
        
        
        
    def mainscript(self):
        self.pop_dist()
        self.graphit()
        self.graphwindow()
        ##initialize the next display


runit=tk.Tk()
runit.eval('tk::PlaceWindow . center')
gui=CLTsimulation(runit)