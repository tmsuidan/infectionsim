# Infection Simulation


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
and second that it doesn't.


no seed was used as we continually incremented the number of iterations until the results converged.

python version 3.x

pandas 
numpy
matplotlib 

It's not complex code so most versions of these should work


Project completed with Robert AJ Alix

