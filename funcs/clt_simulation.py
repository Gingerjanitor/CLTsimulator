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
import funcs.ci_demonstration as ci
import matplotlib.gridspec as gridspec


class clt_simulation(ci.ci_simulation):
    def CLTdemo(self):
        self.sample=pd.Series()
        self.samplemeans=pd.Series()
        
        self.second.destroy()
        self.clt_graphit()
        self.clt_interface()
    
    def clt_interface(self):
        self.cltwindow=tk.Tk()
        self.cltwindow.eval('tk::PlaceWindow . center')

        self.cltwindow.geometry("+100-50")
        #master.geometry("300x200")
        #establish the labels and entry field pairs
        
        self.header=tk.Message(self.cltwindow, width=950, justify="left", text=(f''' If we took an infinite number of samples and the average in each sample, we'd see something very interesting happen. Regardless of if the population distribution is normal or not, these sample means will, eventually, form a normal distribution. And the midpoint of that distribution is the population mean! \n
This next set of options lets you simulate this by drawing many random samples. The slider controls the size of the samples that will be drawn. The buttons change the number of times a sample of that size is drawn. \n Watch how it centers around the population mean of {round(self.pop.mean(),2)} and the spread of the distributions widens with small samples. Small samples=higher odds of getting far off the true mean. '''))
                               



        ##prepare the graph
        

        
        # placing the canvas on the Tkinter window

        #buttons + slider
        
        self.slider=tk.Scale(self.cltwindow, from_=2, to=50, tickinterval=10, width=15, length=625, orient=tk.HORIZONTAL)
        self.slidelabel=tk.Label(self.cltwindow, text="Select the size of \n the samples to be drawn")
        
        self.samp5=tk.Button(self.cltwindow, text="Draw 5 samples",command=self.sample5)
        self.samp25=tk.Button(self.cltwindow, text="Draw 25 samples",command=self.sample25)
        self.samp100=tk.Button(self.cltwindow, text="Draw 100 samples",command=self.sample100)
        self.resetsamp=tk.Button(self.cltwindow, text="Reset",command=self.resetcli)
        self.demoCIs=tk.Button(self.cltwindow, text="...but in practice, you'll only have one sample!",command=self.ci_demo)

                   
        #place the graph
        
        # generate figure
        self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.cltwindow)  
        self.figure.draw()
        
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4,padx=25,pady=5)
        
        #place the labels, buttons, and slider
        self.header.grid(row=0,column=0, columnspan=4)
        self.slider.grid(row=3, column=1, columnspan=4, sticky="w")
        self.slidelabel.grid(row=3,column=0, sticky="e")
        self.samp5.grid(row=4,column=0, padx=5, pady=5)
        self.samp25.grid(row=4,column=1, padx=5, pady=5)
        self.samp100.grid(row=4,column=2, padx=5, pady=5)
        self.resetsamp.grid(row=4,column=4, padx=25, pady=5)
        
        
        self.samp5()
        
        tk.mainloop()

    def clt_graphit(self):
        
        #self.graph=plt.Figure(figsize=(7,5))
        self.sampgraph, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        #gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1]) 
        
        
        sns.kdeplot(data=self.pop, ax=ax1)
        ax1.set_xlim(self.pop.min()*1.10, self.pop.max()*.9)
        #ax.set_xticks(range(self.pop.min(), self.pop.max()))
        ax1.axvline(x = self.pop.mean(),
                   linestyle="dashed",
                   color="red",
                   ymin = 0, # Bottom of the plot
                   ymax = 1)
        ax1.set_title("Population Distribution")
        ax2.set_title("Distribution of Sample Means")
        
        
        
        lowerlim=self.pop.mean()-(self.pop.std()*2.5)
        upperlim=self.pop.mean()+(self.pop.std()*2.5)

        ax2.set_xlim(lowerlim, upperlim)

        ax2.axvline(x = self.pop.mean(),
                   linestyle="dashed",
                   color="red",
                   ymin = 0, # Bottom of the plot
                   ymax = 1)
        

        #self.graph.show()
        
        #A sample has been drawn, graph it!
        if self.samplemeans.empty==False:
            ##this is where the second graph would be incorporated
            sns.histplot(data=self.samplemeans,
                         stat="density", 
                         ax=ax2,
                         alpha=.4, 
                         bins=25)
            ax2.axvline(x = self.samplemeans.mean(),
                       linestyle="dashed",
                       color="orange",
                       ymin = 0, # Bottom of the plot
                       ymax = 1)
            
            
            self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.cltwindow)  
            #self.figure.draw()
            self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4)
            
            self.sampdesc=tk.Message(self.cltwindow,width=700, text=f"Mean of the sample means= {round(self.samplemeans.mean(),2)}    Sample means SD= {round(self.samplemeans.std(),2)}    Number of samples drawn={self.samplemeans.count()}")
            self.sampdesc.grid(row=2,column=0, columnspan=4, padx=5,pady=5)
            
            ##place the continue button
            self.demoCIs.grid(row=5,column=0, columnspan=4, padx=5, pady=4)
    
    def sample5(self):
        print("drawing 5")
        newcases=[]
        for k in range(5):
            print(k)
            newcases.append(self.pop.sample(int(self.slider.get())).mean())
        temp=pd.Series(newcases)
        self.samplemeans=pd.concat([self.samplemeans,temp])
        print(self.samplemeans)
        self.clt_graphit()
        
        
    def sample25(self):
        newcases=[]
        for k in range(25):
            print(k)
            newcases.append(self.pop.sample(int(self.slider.get())).mean())
        temp=pd.Series(newcases)
        self.samplemeans=pd.concat([self.samplemeans,temp])
        print(self.samplemeans)
        self.clt_graphit()
    
    
    def sample100(self):
        newcases=[]
        for k in range(100):
            print(k)
            newcases.append(self.pop.sample(int(self.slider.get())).mean())
        temp=pd.Series(newcases)
        self.samplemeans=pd.concat([self.samplemeans,temp])
        print(self.samplemeans)
        self.clt_graphit()
    
    def resetcli(self):
        self.samplemeans=pd.Series()
        self.clt_graphit()
    
        self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.cltwindow)  
        #self.figure.draw()
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4)
        
