import matplotlib

# in kg
mass = 0.15

# in seconds
time_step = 0.001

# in m/s^2
g = 9.81

# in kg/s
b = 0.015 

v_n = -25
v_n_1 = 0
y = 0
total_time = 0

#while loop where drag always opposes motion so -ve of v
while True:
    v_n_1 = v_n 
    v_n = v_n_1 + (g - (b/mass)*(v_n_1))*time_step
    y += v_n_1*time_step + 0.5*(g - (b/mass)*(v_n_1))*((time_step)**2)
    if y > 300:
        break
    print(f"{v_n_1} is previous velocity\n{v_n} is current velocity\n{y} is the current height")
    total_time += time_step

print(f"{total_time} seconds were taken")