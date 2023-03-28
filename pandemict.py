# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:56:04 2020

@author: talam

Pandemic Flu Spread. Consider a classroom of 21 elementary school kids. 20 of the kids are healthy 
(and susceptible to flu) on Day 1. Tommy (the 21st kid) walks in with the flu and starts interacting
 with his potential victims. To keep things simple, let’s suppose that Tommy comes to school every day 
 (whether or not he’s sick) and will be infectious for 3 days. Thus, there are 3 chances for Tommy to 
 infect the other kids — Days 1, 2, and 3. Suppose that the probability that he infects any individual
 susceptible kid on any of the three days is p = 0.02;
and suppose that all kids and days are independent (so that you have i.i.d. Bern(p) trials).
If a kid gets infected by Tommy, he will then become infectious for 3 days as well, starting on the next day.
(a)  What is the distribution of the number of kids that Tommy infects on Day 1?
(b)  What is the expected number of kids that Tommy infects on Day 1?
(c)  What is the expected number of kids that are infected by Day 2 (you can count Tommy if you want)?
(d)  Simulate the number of kids that are infected on Days 1,2,. . . . Do this many times. What are the
 (estimated) expected numbers of kids that are infected by Day i, i = 1, 2, . . .? Produce a histogram 
 detailing how long the “epidemic” will last.



You can assume kids will recover in 3 days and be immune

2 possible situations: first is that multiple infected students multiply the possibility of infections 
and second that it doesn't
This is the first situation.

no seed was used as we continually incremented the number of iterations until the results converged.
"""

import numpy as np
import pandas as pd
from time import perf_counter
import matplotlib.pyplot as plt


n_iter=4000000 #number of simulations

pinf=0.02 # probability of infection


# Initialize storage array - 50 days for 21 students | 0 = not infected, 1 = infected
start=perf_counter() #time
studentsdf=np.zeros((50,21))

# Simulate infection
for i in range(n_iter):
    # Initialize iteration array - 40 days for 21 students | 0 = not infected, 1 = infected
    students=np.zeros((50,21))
     # Set first student as Tommy and infected for first 3 days
    students[0:3,0]=1 #Tommy
    # iterate through each day
    for j in range(50):
        # iterate through each student
        for k in range(21):
             # i.i.d. Bern(p) trials | Conditions: randomly check if a student is infected and if a student is currently infected (meaning a student has the flu and it can be transmitted) and check if any student is not immune (they have not been infected)

            if np.random.uniform()<=np.sum(students[j,:])*pinf and np.sum(students[j,:])>=1 and np.sum(students[:,k])<1:
                students[j+1:j+4,k]=1 #infection starts on next day and goes for 3 days total
    # Add iteration array to storage array to get total number of infections by day by student
    studentsdf+=students   
print(perf_counter()-start," s")


# Convert to dataframe, sum across students to get total infections by day

studentdf=pd.DataFrame(studentsdf)
studentdf["Sum"]=studentdf.sum(axis=1) #sum each row
# Normalize by dividing by number of iterations to get average infection percentage by day
studentdfstat=studentdf/n_iter

plotdf=studentdfstat["Sum"].to_frame()
#write to csv
studentdf.to_csv("./data/multnonnormstudentf50.csv")
studentdfstat.to_csv("./data/multnormstudentf50.csv")
plotdf.to_csv('./data/multnormsum50.csv')

ax=plt.bar(plotdf.index,plotdf['Sum'])

plt.xticks(fontsize=10)
plt.suptitle('Infected Student Count by Day')
plt.ylabel('Number of Infected Students - Multi rate')
plt.xlabel('Day')
plt.savefig('./data/multi.jpg')
plt.close()


