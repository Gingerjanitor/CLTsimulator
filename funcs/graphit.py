# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:21:35 2023

@author: Matt0
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class mixin():
    def graphit(self):
        
        #self.pop = self.pop[np.isfinite(self.pop).all(0)]
        
        sns.histplot(self.pop,density=True)
        
        plt.show()
        
        if self.sample.empty==False:
            ##this is where the second graph would be incorporated
            pass