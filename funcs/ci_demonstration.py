
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



class ci_simulation():
    
    
    
    def ci_demo(self):
        self.cisample=pd.Series()
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
        self.slidelabel=tk.Label(self.ci_window, text="Select the size \n of the sample")

        self.samp1=tk.Button(self.ci_window, text="Draw 1 sample",command=self.cisamp1)
        self.samp5=tk.Button(self.ci_window, text="Draw 5 samples",command=self.cisamp5)
        self.samp25=tk.Button(self.ci_window, text="Draw 25 samples",command=self.cisamp25)
        self.resetsamp=tk.Button(self.ci_window, text="Reset",command=self.resetcli)
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
        self.samp1.grid(row=5,column=0, padx=5, pady=5,sticky="we")
        self.samp5.grid(row=5,column=1, padx=5, pady=5, sticky="we")
        self.samp25.grid(row=5,column=2, padx=5, pady=5, sticky="we")
        self.resetsamp.grid(row=5,column=3, padx=5, pady=5)
        
        tk.mainloop()
        
        
    def cidemo_visual(self):
        
        self.sampgraph, ax = plt.subplots(figsize=(12, 5))
        
        lowerlim=self.pop.mean()-(self.pop.std()*2.5)
        upperlim=self.pop.mean()+(self.pop.std()*2.5)

        sns.scatterplot(x=self.ci_samps.index, y=self.ci_samps['mean'], ax=ax)

        ax.set_ylim(lowerlim, upperlim)

        ax.set_xlim(0, 25)

        
        #ax.set_xticks(range(self.pop.min(), self.pop.max()))
        ax.axhline(y = self.pop.mean(),
                   linestyle="dashed",
                   color="red",
                   xmin = 0, # Bottom of the plot
                   xmax = 20)
        #ax1.set_title("Population Distribution")
        #ax2.set_title("Distribution of Sample Means")
        
        print("skipped visuals")
    
    
    def checkentry(self):
        if self.selections.get()=="Pick confidence":
            self.missed=tk.Label(self.ci_window, text="    ***", fg="red")
            self.missed.grid(row=4, column=0, padx=5, pady=5)
            error=True
            return error
        else:
            try:
                self.missed.grid_forget()
            except:
                pass

            

    
    def cisamp1(self):
        print(self.selections.get())
        error=self.checkentry()
        if error==True:
            return
        
        newcases=pd.Series(self.pop.sample(int(self.slider.get())))
        
        n=len(self.ci_samps.index)
        
        self.ci_samps.loc[n,'mean']=newcases.mean()
        
        print(self.ci_samps)
        if self.selections.get()=="90% confidence":
            
            self.ci_samps.loc[n,'CIupper']=newcases.mean()+(newcases.std()/np.sqrt(newcases.count())*1.645)
            self.ci_samps.loc[n,'CIlower']=newcases.mean()-(newcases.std()/np.sqrt(newcases.count())*1.645)

        
        if self.selections.get()=="95% confidence":
            self.ci_samps.loc[n,'CIupper']=newcases.mean()+(newcases.std()/np.sqrt(newcases.count())*1.96)
            self.ci_samps.loc[n,'CIlower']=newcases.mean()-(newcases.std()/np.sqrt(newcases.count())*1.96)
        
        if self.selections.get()=="99% confidence":
            self.ci_samps.loc[n,'CIupper']=newcases.mean()+(newcases.std()/np.sqrt(newcases.count())*2.58)
            self.ci_samps.loc[n,'CIlower']=newcases.mean()-(newcases.std()/np.sqrt(newcases.count())*2.58)

        
        print(self.ci_samps)
        
    
    def cisamp5(self):
        pass
    
    def cisamp25(self):
        pass    
    def resetcli(self):
        pass