#

#Based uon: http://newcoder.io/dataviz/part-1/

#
import numpy as np
import plotly.express as px
import tkinter as tk



#enter characteristics for a distribution starting point- N, SD, and Mean.

#Rnorm generate that distribution

#generate a new window with a graph and buttons to randomly draw 10,25,100 cases

#each time the button is clicked, K cases are drawn from the dataset and added to a list.

#In each case, lines on the graph will also show the mean, SD, and 95% confidence interval as well as true pop mean



def tempprint():
    print(mean.get())
    print(sd.get())

master = tk.Tk()

master.geometry("+480-250")
#master.geometry("300x200")
#establish the labels

header=tk.Message(master, width=250, justify="center", text="This tool demonstrates the central limit theorem. First, please describe the population distribution.")
descrip1=tk.Label(master,text="Mean=")
mean=tk.Entry(master)
descrip2=tk.Label(master,text="SD=")
sd=tk.Entry(master)
start=tk.Button(text="Click to start",command=tempprint)

#place the labels

header.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
descrip1.grid(row=1,column=0, padx=5)
mean.grid(row=1,column=1, padx=5)
descrip2.grid(row=2,column=0, padx=5, pady=5)
sd.grid(row=2,column=1, padx=5, pady=5)
start.grid(row=3,column=0,columnspan=2, padx=5, pady=5)

tk.mainloop()


