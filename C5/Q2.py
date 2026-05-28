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
    