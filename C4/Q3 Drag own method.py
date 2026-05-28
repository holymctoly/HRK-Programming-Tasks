'''
A 150-g ball is thrown straight upward from the edge of a cliff
with an initial speed of 25 m/s. On the way down it misses the
cliff edge and continues to fall to the ground 300 m below. In
addition to the force of gravity it is subjected to a force of air
resistance given by D = bv with b = 0.0150 kg/s. (a) How
long is the ball in flight? (b) What is its speed just before it hits
the ground? (c) What is the ratio of this speed to its terminal speed?
(Try using the Euler method with a time interval of Δt = 0.001 s)
'''

import matplotlib.pyplot as plt
import numpy as np

# in kg
mass = 0.15

# in seconds
time_step = 0.001

# in m/s^2
g = 9.81

# in kg/s
b = 0.015 

v_n = 0
v_n_1 = 0
y = 0
total_time = 0

#max distnace
dist = 2000

#calculation for terminal speed
v_terminal = mass*g/b

#with drag
#while loop where drag always opposes motion so -ve of v
x_axes_drag = []
y_axes_drag = []
while True:
    #with drag
    x_axes_drag.append(total_time)
    y_axes_drag.append(v_n)
    v_n_1 = v_n 
    v_n = v_n_1 + (g - (b/mass)*(v_n_1))*time_step
    y += v_n_1*time_step + 0.5*(g - (b/mass)*(v_n_1))*((time_step)**2)
    if y > dist:
        break
    total_time += time_step

 

#plotting
fig, ax = plt.subplots()
ax.plot(x_axes_drag, y_axes_drag)
plt.show()