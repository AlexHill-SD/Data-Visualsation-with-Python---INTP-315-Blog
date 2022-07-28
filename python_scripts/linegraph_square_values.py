import matplotlib.pyplot as pyplot

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# NOTE: style must be set before you plot anything, otherwise the style won't apply
pyplot.style.use('dark_background')

# NOTE: the subplots() command returns 2 variables in order: a figure, set of axes.
#replaces: pyplot.figure()
#           figure.add_subplot(111)
figure, axes = pyplot.subplots()
axes.plot(values, squares, linewidth=4)

axes.set_title("Square numbers", fontsize=30)
axes.set_xlabel("Value", fontsize=18)
axes.set_ylabel("Sqaure of Value", fontsize=18)
axes.tick_params(axis='both', labelsize=18)


# pyplot.show()
pyplot.savefig('linegraph_1.png', bbox_inches='tight', pad_inches=0.1, transparent=True)
