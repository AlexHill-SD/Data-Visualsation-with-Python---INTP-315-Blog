from random import choice

class RandomWalk:
	# A class to generate random walks.

	def __init__(self, num_points=5000):
		# Initialize attributes of a walk.
		self.num_points = num_points

		# All walks start at (0, 0).
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		# Calculate all the points in the walk.

		# Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:
			# Decide which direction to go and how far to go in that direction.
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			x_step = x_direction * x_distance
			
			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			y_step = y_direction * y_distance
			
			# Reject moves that go nowhere.
			if x_step == 0 and y_step == 0:
				continue
		
			# Calculate the new position.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)

import matplotlib.pyplot as pyplot

# Make a random walk.
generatedWalk = RandomWalk()
# Fill the x and y values with an array of "steps"
generatedWalk.fill_walk()

# Plot the points in the walk.
pyplot.style.use('dark_background')

figure, axes = pyplot.subplots()
axes.scatter(generatedWalk.x_values, generatedWalk.y_values, s=15)

pyplot.savefig('walk_visualised_1.png', bbox_inches='tight',
               pad_inches=0.1, transparent=True)

generatedWalk = RandomWalk(100_000)
# Fill the x and y values with an array of "steps"
generatedWalk.fill_walk()

# Plot the points in the walk.
pyplot.style.use('dark_background')

figure, axes = pyplot.subplots(figsize=(15, 15), dpi=600)
walk_order = range(generatedWalk.num_points)

axes.scatter(generatedWalk.x_values, generatedWalk.y_values, c=walk_order, cmap=pyplot.cm.coolwarm, edgecolors='none', s=0.5)
axes.scatter(0,0, c='green', edgecolors='none', s=50)
axes.scatter(generatedWalk.x_values[-1], generatedWalk.y_values[-1], c='red', edgecolors='none', s=50)

axes.get_xaxis().set_visible(False)
axes.get_yaxis().set_visible(False)

pyplot.savefig('walk_visualised_2.png', bbox_inches='tight',
               pad_inches=0.1, transparent=True)