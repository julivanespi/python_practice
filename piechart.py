import matplotlib.pyplot as plt

# the size of the slices
slices = [7,2,2,13]

# labels for the slices
activities = ['sleeping', 'eating', 'working' , 'playing']

# colors for the slices
cols = ['m', 'c', 'r', 'b']

'''
Notice that the order of the lists for: slices, activities, cols
are in order when plt.pie is called. The index for one list will 
match the same index for another list.
'''

# creating the pie chart in the background
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f')


# title for my plot
plt.title('Mi Pinche Pie Chart\nCreated by Julio Espinosa')

plt.show()