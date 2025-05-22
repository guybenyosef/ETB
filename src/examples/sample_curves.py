def generate_selected_curves():
    import numpy as np
    import matplotlib.pyplot as plt
    from elastica import elastica_in_TI
    from visualization.drawing import build_circle
    from visualization.plotting import plot_curves

    # Parameters for a circle of R=sqrt(3)
    dx = 1.2247
    R = np.sqrt(3)
    tl, x, y, theta, dtheta, ddtheta, err = elastica_in_TI(-dx, 0, 45, -1/R, dx, 0, -45, -1/R, 0.001, [0, 0, 0, np.sqrt(3)*np.pi/2], 1)

    # Increasing and decreasing boundary curvature
    a_values = [0.3, 0.6, 0.9, -0.3, -0.5]
    params = [
        [0.15, -1.61, 0.75, 3.0244387],
        [0.28, -1.35, 2.26, 2.64],
        [0.25, -1.55, 4.9, 2.6],
        [0.27, 1.37, -0.4, 2.77],
        [-0.53, -1.56, -0.599, 2.88]
    ]

    for a, param in zip(a_values, params):
        tl, x, y, theta, dtheta, ddtheta, err = elastica_in_TI(-dx, 0, 45, -1/R-a, dx, 0, -45, -1/R-a, 0.001, param, 1)
        plot_curves(x, y, color='b')

    # Changing hbar
    plt.figure()
    plt.axis('equal')
    hbar_params = [
        [-0.07, -1.3, -1.05, 1.132],
        [-0.07, -1.5, -1.05, 1.13],
        [-0.171, -1.42, -1.23, 1.13],
        [0.5, -1.6, -1, 1.15],
        [0.8, 1.35, -1, 1.1],
        [-0.06, -4.2, 2.5, 1.15],
        [-0.5, -1.64, 3.05, 1.16]
    ]

    for i, param in enumerate(hbar_params):
        tl, x, y, theta, dtheta, ddtheta, err = elastica_in_TI(-0.5, 0, 45, -1, 0.5, 0, -45, -1, 0.001, param, 3-i)
        plot_curves(x, y, color=plt.cm.viridis(i / len(hbar_params)))

    plt.legend(['hbar=3', 'hbar=2', 'hbar=1', 'hbar=0.5', 'hbar=0.2', 'hbar=0.15', 'hbar=0.1'])
    plt.title('Selected Curves')
    plt.show()