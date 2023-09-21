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
import pandas as pd
import funcs.clt_simulation as clt_simulation


class mixin(clt_simulation.clt_simulation):
    
    sns.set_style("darkgrid")
    
    def graphit(self):
        
        #self.graph=plt.Figure(figsize=(7,5))
        self.graph, ax=plt.subplots(figsize=(11,6.5))
        
        sns.kdeplot(data=self.pop, ax=ax)
        ax.set_xlim(self.pop.min()*1.10, self.pop.max()*.9)
        #ax.set_xticks(range(self.pop.min(), self.pop.max()))
        ax.axvline(x = self.pop.mean(),
                   linestyle="dashed",
                   color="red",
                   ymin = 0, # Bottom of the plot
                   ymax = 1)
        #self.graph.show()
        
        #A sample has been drawn, graph it!
        if self.sample.empty==False:
            ##this is where the second graph would be incorporated
            sns.histplot(data=self.sample,stat="density", ax=ax,alpha=.4, palette=["blue"])
            ax.axvline(x = self.sample.mean(),
                       linestyle="dashed",
                       color="orange",
                       ymin = 0, # Bottom of the plot
                       ymax = 1)
            
            
            self.figure = FigureCanvasTkAgg(self.graph, master = self.second)  
            #self.figure.draw()
            self.figure.get_tk_widget().grid(row=1,column=0,columnspan=3,padx=5,pady=5)
            print(self.sample.mean())
            
            self.sampdesc=tk.Message(self.second,width=700, text=f"Sample mean= {round(self.sample.mean(),2)}    Sample SD= {round(self.sample.std(),2)}    Sample N={self.sample.count()}")
            self.sampdesc.grid(row=2,column=0, columnspan=3, padx=5,pady=5)
            
            #place the continue button
            self.democlt.grid(row=4,column=0, columnspan=4, padx=5, pady=4)

        
    def graphwindow(self):
        self.second=tk.Tk()
        self.second.eval('tk::PlaceWindow . center')

        self.second.geometry("+300-50")
        #master.geometry("300x200")
        #establish the labels and entry field pairs
        
        
        
        self.header=tk.Message(self.second, width=700, justify="center", text=f"Here's your population distribution. Now you can draw samples from it. Observe what happens as you draw more and more cases.\n\n Pop mean= {round(self.pop.mean(), 2)}    Pop SD= {round(self.pop.std(),2)}")


        ##prepare the graph
        
        # generate figure
        self.figure = FigureCanvasTkAgg(self.graph, master = self.second)  
        #self.figure.draw()
        
        # placing the canvas on the Tkinter window

        #buttons
        
        self.add5=tk.Button(self.second, text="Sample 5 cases",command=self.draw5)
        self.add25=tk.Button(self.second, text="Sample 25 cases",command=self.draw25)
        self.add100=tk.Button(self.second, text="Sample 100 cases",command=self.draw100)
        self.resetsamp=tk.Button(self.second, text="Reset",command=self.resetsample)
        self.democlt=tk.Button(self.second, text="But even with a large sample my sample mean might still be wrong!",command=self.CLTdemo)

                   
        #place the graph
        
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4,padx=5,pady=5)
        
        #place the labels
        self.header.grid(row=0,column=0, columnspan=4,padx=5, pady=5)
        self.add5.grid(row=3,column=0, padx=5, pady=5)
        self.add25.grid(row=3,column=1, padx=5, pady=5)
        self.add100.grid(row=3,column=2, padx=5, pady=5)
        self.resetsamp.grid(row=3,column=4, padx=25, pady=5)
        
        tk.mainloop()
    def draw5(self):
        
        self.sample=pd.concat([self.sample, self.pop.sample(5)])
        
        self.graphit()
        
        
    def draw25(self):
        self.sample=pd.concat([self.sample, self.pop.sample(25)])
        self.graphit()
    
    
    def draw100(self):
        self.sample=pd.concat([self.sample, self.pop.sample(100)])
        self.graphit()
    
    def resetsample(self):
        self.sample=pd.Series()
        print(self.sample)
        self.graphit()
        self.figure = FigureCanvasTkAgg(self.graph, master = self.second)  
        #self.figure.draw()
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=3,padx=5,pady=5)
        
