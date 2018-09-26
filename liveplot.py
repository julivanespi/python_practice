import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def mianimate(i):
    print("Refreshing Data....")
    graph_data = open('nomames.txt', 'r').read()
    lines = graph_data.split("\n")
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(int(x))
            ys.append(int(y))
    ax1.clear()
    ax1.plot(x, y)


ani = animation.FuncAnimation(fig, mianimate, interval=1000)
plt.show()
