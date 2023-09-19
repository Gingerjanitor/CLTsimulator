# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:21:35 2023

@author: Matt0
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


class mixin():
    
        
    def graphit(self):
        
        #self.graph=plt.Figure(figsize=(7,5))
        self.graph, ax=plt.subplots(figsize=(7,5))
        
        sns.kdeplot(data=self.pop, ax=ax)
        #self.graph.show()
        
        if self.sample.empty==False:
            ##this is where the second graph would be incorporated
            pass
    def graphwindow(self):
        self.second=tk.Tk()
        self.second.eval('tk::PlaceWindow . center')

        self.second.geometry("+300-125")
        #master.geometry("300x200")
        #establish the labels and entry field pairs
        
        self.header=tk.Message(self.second, width=600, justify="center", text="Here's your population distribution. Now you can draw samples from it and see how their characteristics compare to the true parameters")


        ##prepare the graph
        
        # generate figure
        self.figure = FigureCanvasTkAgg(self.graph, master = self.second)  
        self.figure.draw()
        
        # placing the canvas on the Tkinter window

        #buttons
        
        self.add5=tk.Button(self.second, text="Sample 5 cases",command=self.draw5)
        self.add25=tk.Button(self.second, text="Sample 25 cases",command=self.draw25)
        self.add100=tk.Button(self.second, text="Sample 100 cases",command=self.draw100)

                   
        #place the graph
        
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=3,padx=5,pady=5)
        
        #place the labels
        self.header.grid(row=0,column=0, columnspan=3,padx=5, pady=5)
        self.add5.grid(row=2,column=0, padx=5, pady=5)
        self.add25.grid(row=2,column=1, padx=5, pady=5)
        self.add100.grid(row=2,column=2, padx=5, pady=5)

        tk.mainloop()
    def draw5(self):
        print(5)
        
    def draw25(self):
        print(25)
    
    def draw100(self):
        print(100)