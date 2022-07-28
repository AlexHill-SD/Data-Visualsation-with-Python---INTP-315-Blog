import matplotlib.pyplot as pyplot

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# NOTE: style must be set before you plot anything,
#       otherwise the style won't apply
pyplot.style.use('dark_background')

figure, axes = pyplot.subplots()
axes.scatter(values, squares, s=100)

axes.set_title("Square numbers", fontsize=30)
axes.set_xlabel("Value", fontsize=18)
axes.set_ylabel("Sqaure of Value", fontsize=18)
axes.tick_params(axis='both', labelsize=18)

pyplot.savefig('scatterplot_1.png', bbox_inches='tight',
               pad_inches=0.1, transparent=True)


values = range(1, 1001)
squares = [x**2 for x in values]

# NOTE: style must be set before you plot anything,
# 		otherwise the style won't apply
pyplot.style.use('dark_background')

figure, axes = pyplot.subplots()
axes.scatter(values, squares, c='green', s=10)

axes.set_title("Square numbers", fontsize=30)
axes.set_xlabel("Value", fontsize=18)
axes.set_ylabel("Sqaure of Value", fontsize=18)
axes.tick_params(axis='both', labelsize=18)
axes.axis([0, 1100, 0, 1100000])

pyplot.savefig('scatterplot_2.png', bbox_inches='tight',
               pad_inches=0.1, transparent=True)


values = range(1, 1001)
squares = [x**2 for x in values]

# NOTE: style must be set before you plot anything,
# 		otherwise the style won't apply
pyplot.style.use('dark_background')

figure, axes = pyplot.subplots()
axes.scatter(values, squares, c=squares, cmap=pyplot.cm.viridis, s=10)

axes.set_title("Square numbers", fontsize=30)
axes.set_xlabel("Value", fontsize=18)
axes.set_ylabel("Sqaure of Value", fontsize=18)
axes.tick_params(axis='both', labelsize=18)
axes.axis([0, 1100, 0, 1100000])

pyplot.savefig('scatterplot_3.png', bbox_inches='tight',
               pad_inches=0.1, transparent=True)
