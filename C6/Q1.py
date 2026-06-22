'''
An interesting toy called the Astro Blaster (See Fig. 6-37)
consists of four plastic balls on a stick. When the stick is
dropped vertically the bottom ball bounces off the ground and
then collides with the ball above. The second ball then col
lides with the third ball, which collides with the fourth ball.
The speed of the top ball after the last collision is consider
ably larger than the speed at which the first ball hits the
ground. Assuming all collisions are elastic, find the ratio of
the masses of the four balls that will result in the largest final
speed of the fourth ball, given that the lightest ball has 1/64
the mass of the heavest ball. (Note: This problem should be
solved numerically, but it can also be solved analytically.)
'''
import matplotlib.pyplot as plt
import numpy as np

#elastic collision
def collide(m_a, m_b, v_a, v_b):
    v_B = (((2*m_a)/(m_a + m_b))*v_a) + (((m_b - m_a)/(m_a + m_b))*v_b)
    v_A = (((2*m_b)/(m_a + m_b)*v_b)) + (((m_a - m_b)/(m_a + m_b))*v_a)
    return (v_A, v_B)

v_1 = 1
m_1 = 64
m_4 = 1

tops = {0: (0,0)}

steps = 5000

for m_2 in np.linspace(1, 64, steps):
    for m_3 in np.linspace(1, 64, steps):
        #collision 1
        v_2 = -1
        col_1 = collide(m_1, m_2, v_1, v_2)
        v_2 = col_1[1]

        #collision 2
        v_3 = -1
        col_2 = collide(m_2, m_3, v_2, v_3)
        v_3 = col_2[1]

        #collision 3
        v_4 = -1
        col_3 = collide(m_3, m_4, v_3, v_4)
        v_4 = col_3[1]

        tops[v_4] = (m_2, m_3)
    

tops_sorted = sorted(tops.keys(), reverse = True)
v_4 = tops_sorted[0]
masses = tops[v_4]
print(f"The following masses for m_2 and m_3 were calculated to be as follows: \n {masses[0]:.3f} kg and {masses[1]:.3f} kg \n the final speed of the ball was {v_4:.3f}")

with open("DatatoSteps.txt", "a+") as f:
    f.write(f"{steps} steps: m_2 = {masses[0]:.3f}, m_3 = {masses[1]:.3f}, v_4 = {v_4:.3f}\n")

