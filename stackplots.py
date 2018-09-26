import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

labels=['sleeping', 'eating', 'working', 'playing']

fig, ax = plt.subplots()
ax.stackplot(days, sleeping, eating, working, playing, labels=labels, colors=['m','c','r','k'])

# here I create my labels for my GUI plot
plt.xlabel('x')
plt.ylabel('y')

# title & lengend for my plot
plt.title('Mi Pinche Stack Plot\nCreated by Julio Espinosa')
plt.legend()

# show my plot
plt.show()
