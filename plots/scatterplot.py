import matplotlib.pyplot as plt

# here I define my two list
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 4, 6, 7, 8, 3, 5, 7]

# here I create my scatterplot in the background
plt.scatter(x, y, label='skitscat', color='k', marker='+', s=200)

# here I create my labels for my GUI plot
plt.xlabel('x')
plt.ylabel('y')

# title & lengend for my plot
plt.title('Mi Pinche Scatter Plot\nCreated by Julio Espinosa')
plt.legend(loc='upper left')

# show my plot
plt.show()