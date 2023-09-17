# -*- coding: utf-8 -*-

import pandas as pd 
from scipy.stats import skewnorm

class gendist():
    def pop_dist(self):
        self.invalid.grid_forget()
        self.skrange.grid_forget()
        
        mean=self.mean.get()
        sd=self.sd.get()
        skew=self.skew.get()
        
        #validate
        starters=[skew,mean,sd]
        finalparams=[]
        for value in starters:
            try:
                value=float(value)
                finalparams.append(value)
            except ValueError:
                self.invalid.grid(row=4,column=0,columnspan=2, padx=5, pady=5)
                return
        if abs(finalparams[0])>8:
                self.skrange.grid(row=4,column=0,columnspan=2, padx=5, pady=5)
        
                
        print(finalparams)
        n=15000
        
        self.pop=pd.Series(skewnorm.rvs(a=finalparams[0],loc=finalparams[1],scale=finalparams[2], size=n))
        