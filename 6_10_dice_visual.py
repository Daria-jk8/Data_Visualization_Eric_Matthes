from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create die with 6 sides two D6
die_1 = Die()
die_2 = Die(10)

# simulation of a series of throws with saving the results in the list
results = []

for roll_num in range(50000):       # --> how many time do you want to throw of dice? 100/1000/50000...
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analysis of the result    

frequencies = []   # how many times each party number is repeated?
max_result = die_1.num_sides + die_2.num_sides # --> total number of sides

for value in range(1, max_result+1): 
   frequency = results.count(value)
   frequencies.append(frequency) 

# print(frequencies) 

# --> Data visualizition
x_value = list(range(1, max_result+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', 
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d10_d6.html')                   