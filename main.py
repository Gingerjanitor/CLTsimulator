# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:01:04 2023

@author: Matt0
"""
import tkinter as tk
import pandas as pd

import gui.initparams as initparams
import funcs.GenDistribution as gendist
import funcs.analysis_opts as analysis_opts


class CLTsimulation(initparams.mixin,
                    gendist.gendist,
                    analysis_opts.mixin): 
    def __init__(self,master):
        
        self.sample=pd.Series()
        self.samplemeans=pd.Series()
        self.tickstatus = tk.IntVar()
        self.resetit=False
        self.successrate=pd.Series()
        
        self.tickstatus
        self.ci_samps=pd.DataFrame(columns=['mean','CIlower', 'CIupper'])
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