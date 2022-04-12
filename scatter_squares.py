import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # -->s=sets the size of the points, c=linecolor, cmap=colormap

# --> Assignment: header, the name of the x and y axes 
ax.set_title("SQUARE NUMBERS", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
# --> Assignment: setting the font size of tick marks on the axes
ax.tick_params(axis='both', which='major', labelsize=14)
# --> Assignment: a range to each axis
ax.axis([0, 1100, 0, 1100000])

plt.savefig('15_8.png', bbox_inches='tight')
