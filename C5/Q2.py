'''
Starting from rest a person pushes a 95-kg crate across a rough
floor with a force given by 
F=200e^(-0.15t)
where F is in new
tons and t is in seconds. The force decreases exponentially be
cause the person tires. As long as the crate is moving a constant
frictional force of 80 N opposes the motion. (a) How long after
starting does the crate stop? (b) How far does it go? (c) How
accurate are your results? (Try using the Euler method with an
initial time interval of t 
0.01 s. Repeat the process, but use
a time interval of t 
0.001 s. Compare the results to get an
estimate of your accuracy.)
'''

import matplotlib.pyplot as plt
import numpy as np

#mass in kg
mass = 95

#velocity in m/s
v_n = 0
v_f = 0

#displacement in m
x_n = 0
x_f = 0

#frictional force in newtons
fric = 80

#time dependent force
force = lambda time: 200*np.exp(-0.15*time)

#time step in s
step = 0.01

#total time in s
t_total = 0

displacements = []
velocities = []
time = []

while True:
    displacements.append(x_f)
    velocities.append(v_f)
    time.append(t_total)
    v_n = v_f
    x_n = x_f
    v_f = v_n + step*(1/mass*(force(t_total) - fric))
    x_f = x_n + step*v_n
    if v_f < 0:
        break
    t_total += step

#plotting
fig, ax = plt.subplots()
ax.plot(time, velocities)
plt.show()
    