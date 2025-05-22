import matplotlib.pyplot as plt
def plot_curves(x, y, color):

    plt.plot(x, y, color=color)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Elastica in Tangent Bundle')
    plt.grid(True)
    plt.axis('equal')
    plt.show()