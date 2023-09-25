# -*- coding: utf-8 -*-

import pandas as pd 
from scipy.stats import skewnorm
import random
import numpy as np


class gendist():
    def ruin_normality(self,finalparams, n):
        for num in range(random.randint(3, 6)):
            mean=float(random.uniform(.1,4))
            if random.randint(1,2)==2:
                mean=-mean
            noise=pd.Series(skewnorm.rvs(
                                a=finalparams[0]/float(random.uniform(-4 ,6)),
                                loc=finalparams[1]/mean,
                                scale=finalparams[2]/float(random.uniform(.1,8)), 
                                size=int(round((n/random.randint(1,4)),0))
                                ))
            self.pop=pd.concat([self.pop, noise], axis=0)
        
        for num in range(random.randint(3,6)):
            value1=self.pop.sample().iloc[0]
            value2=self.pop.sample().iloc[0]
            while value1>=value2:
                value2=self.pop.sample().iloc[0]
                
            noise=pd.Series(np.random.randint(value1,value2, size=int(round((n/random.randint(3,15)),0))))
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
        n=15000
        
        self.pop=pd.Series(skewnorm.rvs(a=finalparams[0],loc=finalparams[1],scale=finalparams[2], size=n))
        print(self.tickstatus.get())
        
        if int(self.tickstatus.get())==1:
            self.ruin_normality(finalparams,n)