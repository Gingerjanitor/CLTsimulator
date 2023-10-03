
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import pandas as pd
import matplotlib.gridspec as gridspec
from tkinter import ttk
from matplotlib import collections as matcoll

import time

class ci_simulation():
    
    
    
    def ci_demo(self):
        self.samplemeans=pd.Series()
        
        self.cisample=pd.Series()
        self.ci_samps=pd.DataFrame(columns=['mean','CIlower', 'CIupper'])

        
        
        self.samp5.destroy()
        self.cltwindow.destroy()
        
        self.cidemo_visual()
        self.ci_interface()
        
    def ci_interface(self):
        
        
        self.ci_window=tk.Tk()
        self.ci_window.eval('tk::PlaceWindow . center')

        self.ci_window.geometry("+100-50")
        #master.geometry("300x200")
        #establish the labels and entry field pairs
        
        self.header=tk.Message(self.ci_window, width=950, justify="left", text=(f'''Even with just one sample, we can approximate the population distribution with a *confidence interval*. Here's the logic: Remember the distribution of sample means in the last window? If we drew a sample it would be somewhere in that spread. But we don't know if it's in the middle or the edges. But what we can do is create a range that encompasses most of the values of that distribution. We do this by estimating the standard deviation of that sampling distribution (aka the standard error). This is simply sd/sqrt(n), meaning the interval narrows with a larger sample. This is used to create a range where the population mean should fall, with higher confidence meaning a larger interval.\n\n The below simulation lets you draw a sample and see if the population mean is captured within the confidence interval'''))
        self.options=["Pick confidence",
                 "90% confidence",
                 "95% confidence",
                 "99% confidence"]
        
        self.selections=tk.StringVar(self.ci_window)
        self.selections.set("Click to set a confidence level")
        self.dropdown=ttk.OptionMenu( self.ci_window , self.selections , *self.options )

        ##prepare the graph
        
        # generate figure
        self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.ci_window)  
        #self.figure.draw()
        
        # placing the canvas on the Tkinter window

        #buttons + slider
        self.slider=tk.Scale(self.ci_window, from_=5, to=250, tickinterval=50, width=15, length=625, orient=tk.HORIZONTAL)
        self.slider.set(20)
        self.slidelabel=tk.Label(self.ci_window, text="Select the size \n of the sample")

        self.cisamp1=tk.Button(self.ci_window, text="Draw 1 sample",command=self.cisample1)
        self.cisamp5=tk.Button(self.ci_window, text="Draw 5 samples",command=self.cisample5)
        self.cisamp25=tk.Button(self.ci_window, text="Draw 25 samples",command=self.cisample25)
        self.resetsamp=tk.Button(self.ci_window, text="Reset",command=self.reset_ci)
        self.demoCIs=tk.Button(self.ci_window, text="...but in practice, you'll only have one sample!",command=self.ci_demo)

                   
        #place the graph
        
        self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4,padx=25,pady=5)
        
        #place the labels, buttons, and slider
        self.header.grid(row=0,column=0, columnspan=5)
        
        self.slider.grid(row=4, column=1, columnspan=4, sticky="w")
        self.slidelabel.grid(row=4,column=0, sticky="e")
        
        ###eventually there will be a summary with: Most recent 95% CI, # of CIs that have hit the true pop mean
        # % that have hit the true pop mean
        
        self.dropdown.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.cisamp1.grid(row=5,column=0, padx=5, pady=5,sticky="we")
        self.cisamp5.grid(row=5,column=1, padx=5, pady=5, sticky="we")
        self.cisamp25.grid(row=5,column=2, padx=5, pady=5, sticky="we")
        self.resetsamp.grid(row=5,column=3, padx=5, pady=5)
        
        self.sampdesc=tk.Message(self.ci_window,width=700, text=f"No samples drawn yet, select something!")
        self.sampdesc.grid(row=2,column=0, columnspan=4, padx=5,pady=5)
        
        
        tk.mainloop()
        
        
    def cidemo_visual(self):
        
        self.sampgraph, ax = plt.subplots(figsize=(12, 5))
        
        
        try:
            if int(self.slider.get())<=20:
                
                lowerlim=self.pop.mean()-(self.pop.std()*1.3)
                upperlim=self.pop.mean()+(self.pop.std()*1.3)
            
            elif 20<int(self.slider.get())<=120:
                lowerlim=self.pop.mean()-(self.pop.std()*.6)
                upperlim=self.pop.mean()+(self.pop.std()*.6)
                
            elif 120<int(self.slider.get()):
                lowerlim=self.pop.mean()-(self.pop.std()*.3)
                upperlim=self.pop.mean()+(self.pop.std()*.3)
                
        except tk.TclError: 
                lowerlim=self.pop.mean()-(self.pop.std()*.6)
                upperlim=self.pop.mean()+(self.pop.std()*.6)
                
        
        print(self.ci_samps)
        
        sns.scatterplot(x=self.ci_samps.index, y=self.ci_samps['mean'], ax=ax)
        ax.set_title("Population Mean vs Means and Confidence Intervals of Samples")
        ax.set_ylim(lowerlim, upperlim)

        if len(self.ci_samps.index)<=25:
            ax.set_xlim(-1, 25)
        else:
            ax.set_xlim(-1, len(self.ci_samps['mean']))

        
        #ax.set_xticks(range(self.pop.min(), self.pop.max()))
        ax.axhline(y = self.pop.mean(),
                   linestyle="dashed",
                   color="red",
                   xmin = 0, # Bottom of the plot
                   xmax = 20,
                   label="Population Mean")
        ax.legend()
        #ax1.set_title("Population Distribution")
        #ax2.set_title("Distribution of Sample Means")

        if self.resetit==True:
            self.sampdesc.grid_forget()
            self.sampdesc=tk.Message(self.ci_window,width=700, text=f"No samples drawn yet, select something!")
            self.sampdesc.grid(row=2,column=0, columnspan=4, padx=5,pady=5)
        
            self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.ci_window)  
            #self.figure.draw()
            self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4)
            self.resetit=False

        if self.ci_samps.empty==False:
            ##this is where the second graph would be incorporated
            
            sns.scatterplot(data=self.ci_samps,
                         y=self.ci_samps['mean'],
                         x=self.ci_samps.index,
                         ax=ax,
                         color="black")
            
            plt.scatter(self.ci_samps.index, self.ci_samps['CIupper'], color='blue', s=0)
            plt.scatter(self.ci_samps.index, self.ci_samps['CIlower'], color='blue', s=0)


            # Connect two points with a line
            for value in self.ci_samps.index:
                if self.ci_samps['CIlower'].iloc[value]<=self.pop.mean()<=self.ci_samps['CIupper'].iloc[value]:
                    #Add a 1 if they match. 
                    self.successrate[len(self.successrate)+1]=1
                    plt.plot([self.ci_samps.index[value], self.ci_samps.index[value]], [self.ci_samps['CIlower'].iloc[value], self.ci_samps['CIupper'].iloc[value]], color='black')

                else:
                    #Add a 0 if they match.
                    self.successrate[len(self.successrate)+1]=0

                    plt.plot([self.ci_samps.index[value], self.ci_samps.index[value]], [self.ci_samps['CIlower'].iloc[value], self.ci_samps['CIupper'].iloc[value]], color='red')


            self.figure = FigureCanvasTkAgg(self.sampgraph, master = self.ci_window)  
            #self.figure.draw()
            self.figure.get_tk_widget().grid(row=1,column=0,columnspan=4)
            
            success=self.successrate.value_counts(normalize=True)
            
            self.sampdesc.grid_forget()

            self.sampdesc=tk.Message(self.ci_window,width=700, text=f"Thus far, %{round(success[1]*100,2)} of estimates have captured the true population mean")
            self.sampdesc.grid(row=2,column=0, columnspan=4, padx=5,pady=5)
            
            ##place the continue button
            #self.demoCIs.grid(row=5,column=0, columnspan=4, padx=5, pady=4)
    
    
    def checkentry(self):
        if self.selections.get()=="Pick confidence":
            self.missed=tk.Label(self.ci_window, text="    ***", fg="red")
            self.missed.grid(row=4, column=0, padx=5, pady=5)
            self.noticeme()
            error=True
            return error
        else:
            try:
                self.missed.grid_forget()
            except:
                pass

            

    
    def cisample1(self):
        error=self.checkentry()
        if error==True:
            return
        
        newcases=pd.Series(self.pop.sample(int(self.slider.get())))
        
        self.ci_select(newcases)
        
        self.cidemo_visual()
    
    def cisample5(self):
        error=self.checkentry()
        if error==True:
            return
        
        for num in range(0,5):
            newcases=pd.Series(self.pop.sample(int(self.slider.get())))
            
            self.ci_select(newcases)
            
        self.cidemo_visual()
        
    
    def cisample25(self):
        error=self.checkentry()
        if error==True:
            return
        
        for num in range(0,25):
            newcases=pd.Series(self.pop.sample(int(self.slider.get())))
            
            self.ci_select(newcases)
            
        self.cidemo_visual()
        
    def reset_ci(self):
        self.ci_samps=pd.DataFrame(columns=['mean','CIlower', 'CIupper'])
        self.successrate=pd.Series()        
        
        self.resetit=True
        self.cidemo_visual()
    
    def noticeme(self):
        self.blockit = tk.Label(self.ci_window, text="                  ")
        self.dropdown.grid_forget()
        self.blockit.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.ci_window.update()
        time.sleep(.3)
        self.blockit.grid_forget()
        self.dropdown.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    def ci_select(self, newcases):
        
        n=len(self.ci_samps.index)
        
        self.ci_samps.loc[n,'mean']=newcases.mean()
        
        if self.selections.get()=="90% confidence":
            
            self.ci_samps.loc[n,'CIupper']=newcases.mean()+(newcases.std()/np.sqrt(newcases.count())*1.645)
            self.ci_samps.loc[n,'CIlower']=newcases.mean()-(newcases.std()/np.sqrt(newcases.count())*1.645)

        
        if self.selections.get()=="95% confidence":
            self.ci_samps.loc[n,'CIupper']=newcases.mean()+(newcases.std()/np.sqrt(newcases.count())*1.96)
            self.ci_samps.loc[n,'CIlower']=newcases.mean()-(newcases.std()/np.sqrt(newcases.count())*1.96)
        
        if self.selections.get()=="99% confidence":
            self.ci_samps.loc[n,'CIupper']=newcases.mean()+(newcases.std()/np.sqrt(newcases.count())*2.58)
            self.ci_samps.loc[n,'CIlower']=newcases.mean()-(newcases.std()/np.sqrt(newcases.count())*2.58)
