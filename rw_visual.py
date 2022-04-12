import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    """Building a random walk"""
    rw = RandomWalk(50000)
    rw.fall_walk()

    # --> Plotting points on a chart
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, 
               c=point_numbers, 
               cmap=plt.cm.Blues, 
               edgecolors='none', 
               s=1)
    #  selection or markering  of the first and last point
    ax.scatter(0, 0, 
               c='green', 
               edgecolors='none', 
               s=100) # first
    ax.scatter(rw.x_values[-1], rw.y_values[-1], 
               c='red', 
               edgecolors='none', 
               s=100) # last


    # delete the axis

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input('Make another walk? (y/n):') # see in Terminal
    if keep_running == 'n':
        break