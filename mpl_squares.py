import matplotlib.pyplot as plt

"""The matplotlib.pyplot.subplots method provides a way to plot multiple plots on a single figure. 
   Given the number of rows and columns, it returns a tuple (fig, ax), 
   giving a single figure fig with an array of axes ax."""

input_values = [1, 2, 3, 4, 5]
squares = [1, 4 , 9, 16, 25] 
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

# --> Assignment: header, the name of the x and y axes 
ax.set_title("SQUARE NUMBERS", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
# --> Assignment: setting the font size of tick marks on the axes
ax.tick_params(axis='both', labelsize=14)

plt.show()