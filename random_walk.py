from random import choice

class RandomWalk():
    # -->Generating random walks
    def __init__(self, num_points=5000):
        # initialization of walking attributes
        self.num_points = num_points

        # ALL walks start from the point (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fall_walk(self):
        # Calculation of all points of walks
        while len(self.x_values) < self.num_points:
            # --> Determining the direction and distance of movement
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance 
            # --> Deviation of zero displacements
            if x_step == 0 and y_step == 0:
                continue
            # --> Calculation of the following values 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step 

            self.x_values.append(x)
            self.y_values.append(y)

