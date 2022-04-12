from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create die with 6 sides one D6
die = Die()

# simulation of a series of throws with saving the results in the list
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analysis of the result    

frequencies = []   # how many times each party number is repeated?
for value in range(1, die.num_sides+1):
   frequency = results.count(value)
   frequencies.append(frequency) 

# print(frequencies) 

# --> Data visualizition
x_value = list(range(1, die.num_sides+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', 
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')                   