import numpy as np


def find_curvature_from_points(x0, y0, x1, y1, x2, y2):
    """
    Calculate curvature from three points.

    Parameters:
    -----------
    x0, y0, x1, y1, x2, y2 : float
        Coordinates of three points

    Returns:
    --------
    kappa : float
        Curvature value
    theta : float
        Angle
    circ : numpy.ndarray
        Complex array representing points on the circle
    """
    A = np.array([[x0 - x1, y0 - y1], [x1 - x2, y1 - y2]])
    b = 0.5 * np.array(
        [x1**2 + y1**2 - x0**2 - y0**2, x2**2 + y2**2 - x1**2 - y1**2]
    )

    p = np.linalg.inv(A) @ b
    R = np.sqrt((x0 - (-p[0]))**2 + (y0 - (-p[1]))**2)
    kappa = 1/R
    theta = np.arctan2(y0 - (-p[1]), (x0 - (-p[0])))

    t = np.linspace(0, 2 * np.pi, num=100)
    # Fix: Create center as a complex number, not a 2D array
    center = complex(-p[0], -p[1])
    circ = center + R * np.exp(1j * t)

    return kappa, theta, circ