import numpy as np

def build_circle(x0, y0, rad, rows, cols):
    """
    Build a binary mask representing a circle.
    
    Parameters:
    -----------
    x0, y0 : float
        Center coordinates
    rad : float
        Circle radius
    rows, cols : int
        Dimensions of the output matrix
    
    Returns:
    --------
    M : numpy.ndarray
        Binary mask with 1s inside the circle
    """
    M = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            if (r - x0) ** 2 + (c - y0) ** 2 < rad ** 2:
                M[r, c] = 1
    return M

def draw_left_inducer(x0, y0, theta0, kappa0, arc_perimeter):
    """
    Draw a left inducer as a circular arc.
    
    Parameters:
    -----------
    x0, y0 : float
        Starting point coordinates
    theta0 : float
        Orientation in degrees
    kappa0 : float
        Curvature
    arc_perimeter : float
        Length of the arc
    
    Returns:
    --------
    M : numpy.ndarray
        Array of complex numbers representing points on the arc
    """
    theta0 = theta0 * np.pi / 180
    
    R = abs(1 / kappa0)
    t0 = theta0 + np.pi / 2
    
    Xc = x0 - R * np.cos(t0)
    Yc = y0 - R * np.sin(t0)
    
    t_range = arc_perimeter / R
    t_step = t_range / 100
    
    t_values = np.arange(t0, t0 + t_range + t_step, t_step)
    
    # Create complex array directly
    x_coords = Xc + R * np.cos(t_values)
    y_coords = Yc + R * np.sin(t_values)
    M = x_coords + 1j * y_coords
    
    return M

def draw_right_inducer(x0, y0, theta0, kappa0, arc_perimeter):
    """
    Draw a right inducer as a circular arc.
    
    Parameters:
    -----------
    x0, y0 : float
        Starting point coordinates
    theta0 : float
        Orientation in degrees
    kappa0 : float
        Curvature
    arc_perimeter : float
        Length of the arc
    
    Returns:
    --------
    M : numpy.ndarray
        Array of complex numbers representing points on the arc
    """
    theta0 = theta0 * np.pi / 180
    
    R = abs(1 / kappa0)
    t0 = theta0 + np.pi / 2
    
    Xc = x0 - R * np.cos(t0)
    Yc = y0 - R * np.sin(t0)
    
    t_range = arc_perimeter / R
    t_step = t_range / 100
    
    t_values = np.arange(t0, t0 - t_range - t_step, -t_step)
    
    # Create complex array directly
    x_coords = Xc + R * np.cos(t_values)
    y_coords = Yc + R * np.sin(t_values)
    M = x_coords + 1j * y_coords
    
    return M