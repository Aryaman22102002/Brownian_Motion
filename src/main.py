# main.py is the main file of the python module which imports the movement function from Brownian_Motion.py and 
# uses it to simulate the Brownian Motion

import matplotlib.pyplot as plt 
from Brownian_Motion import movement

# Repeatedly calling the movement function with a certain pause
while True:
   movement()
   plt.pause(0.5)