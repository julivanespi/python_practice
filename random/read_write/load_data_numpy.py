import matplotlib.pyplot as plt
import numpy as np

'''
Since I know that the file that I am loading only has 2 columns,
I create 2 list (x,y) and use the np.loadtxt function to populate
the list. I specify my delimiter 
'''
x, y = np.loadtxt('nomames.txt', delimiter=',', unpack=True)

# plot the data in the background
plt.plot(x, y, label='Loaded From file bro!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mi Pinche Data from nomames.txt\nCreated by Julio Espinosa')

plt.legend()
plt.show()