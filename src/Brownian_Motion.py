# Brownian_Motion.py is used to simulate the movement of the point like Brownian Motion

import matplotlib.pyplot as plt 
import random

# Initialize the variables
x = 8
y = 8
dir = "Start"
dir1 = 0
dir2 = 0
dir3 = 0
dir4 = 0

# Plotting the graph
fig, ax = plt.subplots()
points, = ax.plot(x, y, marker='o', linestyle='None')
ax.set_xlim(0, 16) 
ax.set_ylim(0, 16)

"""
Function Name: movement
Input:  No inputs required
Output: Function does not return anything
Logic:  The function is used to control the movement of the point. The point starts from the centre of the sqaure and
        moves straight upwards initially. After it collides with a wall, it rotates randomly either to the left or 
        to the right or doesn't rotate at all. After rotating, it again moves in the direction which it is facing.
Example call: movement()
"""

def movement():
    global x, y, dir, dir1, dir2, dir3, dir4
    
    # Travelling in the direction in which the point has rotated after colliding with a particular wall 
    if x > 0 and x < 16 and y > 0 and y < 16:
            if dir == "Start":
                new_x = x
                new_y = y+1
            elif dir == "UpperBorder":
                new_x = x + dir1
                new_y = y - 1
            elif dir == "LowerBorder":
                new_x = x + dir2
                new_y = y + 1
            elif dir == "LeftBorder":
                new_x = x + 1
                new_y = y + dir3
            elif dir == "RightBorder":
                new_x = x - 1
                new_y = y + dir4    
                
    # If the point collides with the upper wall
    elif x > 0 and x < 16 and y >= 16:
            # Deciding where to roatate the point randomly
            dir1 = random.randrange(-1, 1, 1)
            new_x = x + dir1
            new_y = y - 1
            dir = "UpperBorder"
            
    # If the point collides with the lower wall
    elif x > 0 and x < 16 and y <= 0:
            dir2 = random.randrange(-1, 1, 1)
            new_x = x + dir2
            new_y = y + 1
            dir = "LowerBorder"
            
    # If the point collides with the left wall
    elif x <= 0 and y > 0 and y < 16:
            dir3 = random.randrange(-1, 1, 1)
            new_x = x + 1
            new_y = y + dir3
            dir = "LeftBorder"
            
    # If the point collides with the right wall
    elif x >=16 and y > 0 and y < 16:
            dir4 = random.randrange(-1, 1, 1)
            new_x = x - 1
            new_y = y + dir4
            dir = "RightBorder"
    points.set_data(new_x, new_y)
    x = new_x
    y = new_y
        
    


    

