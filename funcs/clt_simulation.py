# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:19:04 2023

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

class clt_simulation():
    def CLTdemo(self):
        self.sample=pd.Series()
        self.second.destroy()
        print("It's CLT, not CLIT!")
        self.clt_graphit()
        self.clt_interface()
    
    def clt_interface(self):
        self.cltwindow=tk.Tk()
        self.cltwindow.eval('tk::PlaceWindow . center')

        self.cltwindow.geometry("+300-50")
        #master.geometry("300x200")
        #establish the labels and entry field pairs
        
        
        
        self.header=tk.Message(self.cltwindow, width=775, justify="center", text=f"If we took an infinite number of samples and the average in each sample, we'd see something very interesting happen. Regardless of if the population distribution is normal or not, these sample means will, eventually, form a normal distribution. And the midpoint of that distribution is the population mean!")


        ##prepare the graph
        
        # generate figure
        self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.cltwindow)  
        self.figure.draw()
        
        # placing the canvas on the Tkinter window

        #buttons
        
        self.samp5=tk.Button(self.cltwindow, text="Draw 5 samples",command=self.samp5)
        self.samp25=tk.Button(self.cltwindow, text="Sample 5 samples",command=self.samp25)
        self.samp100=tk.Button(self.cltwindow, text="Sample 100 samples",command=self.samp100)
        self.resetsamp=tk.Button(self.cltwindow, text="Reset",command=self.resetsample)
        self.democlt=tk.Button(self.cltwindow, text="...But I'm only ever gonna have one sample!",command=self.CLTdemo)

                   
        #place the graph
        
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4,padx=5,pady=5)
        
        #place the labels
        self.header.grid(row=0,column=0, columnspan=4,padx=5, pady=5)
        self.samp5.grid(row=3,column=0, padx=5, pady=5)
        self.samp25.grid(row=3,column=1, padx=5, pady=5)
        self.samp100.grid(row=3,column=2, padx=5, pady=5)
        self.resetsamp.grid(row=3,column=4, padx=25, pady=5)
        
        tk.mainloop()

    def clt_graphit(self):
        
        #self.graph=plt.Figure(figsize=(7,5))
        self.sampgraph, ax=plt.subplots(figsize=(11,6.5))
        
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
        if self.samplemeans.empty==False:
            print("me try")
            ##this is where the second graph would be incorporated
            sns.histplot(data=self.samplemeans,stat="density", ax=ax,alpha=.4, palette=["grey"])
            ax.axvline(x = self.samplemeans.mean(),
                       linestyle="dashed",
                       color="orange",
                       ymin = 0, # Bottom of the plot
                       ymax = 1)
            
            
            self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.cltwindow)  
            #self.figure.draw()
            self.figure.get_tk_widget().grid(row=1,column=0,columnspan=3,padx=5,pady=5)
            
            self.sampdesc=tk.Message(self.cltwindow,width=700, text=f"Mean of the sample means= {round(self.samplemeans.mean(),2)}    Sample means SD= {round(self.samplemeans.std(),2)}    numher of samples drawn={self.samplemeans.count()}")
            self.sampdesc.grid(row=2,column=0, columnspan=3, padx=5,pady=5)
            
            ##place the continue button
            #self.democlt.grid(row=4,column=0, columnspan=4, padx=5, pady=4)
    
    def samp5(self):
        newcases=[]
        for k in range(5):
            print(k)
            newcases.append(self.pop.sample(15).mean())
        temp=pd.Series(newcases)
        self.samplemeans=pd.concat([self.samplemeans,temp])
        print(self.samplemeans)
        self.clt_graphit()
        
        
    def samp25(self):
        self.sample=pd.concat([self.sample, self.pop.sample(25)])
        self.clt_graphit()
    
    
    def samp100(self):
        self.sample=pd.concat([self.sample, self.pop.sample(100)])
        self.clt_graphit()
