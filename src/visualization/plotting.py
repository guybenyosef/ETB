import matplotlib.pyplot as plt
def plot_curves(fig, x, y, color, label='Elastica in Tangent Bundle'):
    ax = fig.add_subplot(111)
    ax.plot(x, y, color=color)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(label)
    ax.grid(True)
    ax.axis('equal')
    plt.show()