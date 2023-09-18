# -*- coding: utf-8 -*-

import pandas as pd 
from scipy.stats import skewnorm
import random
import numpy as np

class gendist():
    def ruin_normality(self,finalparams, n):
        for num in range(random.randint(1, 5)):
            noise=pd.Series(skewnorm.rvs(
                                a=finalparams[0]/float(random.uniform(-5 ,5)),
                                loc=finalparams[1]/float(random.uniform(.2,3)),
                                scale=finalparams[2]/float(random.uniform(.2,7)), 
                                size=int(round((n/random.randint(1,7)),0))
                                ))
            self.pop=pd.concat([self.pop, noise], axis=0)
        
        for num in range(random.randint(1,5)):
            value1=self.pop.sample().iloc[0]
            value2=self.pop.sample().iloc[0]
            while value1>=value2:
                value2=self.pop.sample().iloc[0]
                
            noise=pd.Series(np.random.randint(value1,value2, size=int(round((n/random.randint(5,15)),0))))
            self.pop=pd.concat([self.pop, noise], axis=0)


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
                self.invalid.grid(row=5,column=0,columnspan=2, padx=5, pady=5)
                return
        if abs(finalparams[0])>8:
                self.skrange.grid(row=5,column=0,columnspan=2, padx=5, pady=5)
        
                
        print(finalparams)
        n=5000
        
        self.pop=pd.Series(skewnorm.rvs(a=finalparams[0],loc=finalparams[1],scale=finalparams[2], size=n))
        print(self.tickstatus.get())
        
        if int(self.tickstatus.get())==1:
            print("I want to make it messed up")
            self.ruin_normality(finalparams,n)