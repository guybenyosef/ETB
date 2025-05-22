import numpy as np
from scipy.optimize import fmin

def elastica_in_TI(x0, y0, t0, k0, x1, y1, t1, k1, h, param_init, hbar):
    th0 = t0 * np.pi / 180
    th1 = t1 * np.pi / 180
    hbars = hbar ** 2
    
    class ErrorFunction:
        def __init__(self):
            self.x = None
            self.y = None
            self.theta = None
            self.dtheta = None
            self.ddtheta = None
            self.l = None
        
        def __call__(self, param):
            c, phi, g0, l = param
            num_of_points = int(round(l / h))

            # Initialize arrays
            ddtheta = np.zeros(num_of_points)
            dtheta = np.zeros(num_of_points)
            theta = np.zeros(num_of_points)
            x = np.zeros(num_of_points)
            y = np.zeros(num_of_points)

            ddtheta[0] = g0
            dtheta[0] = k0
            theta[0] = th0
            y[0] = y0
            x[0] = x0

            for p in range(1, num_of_points):
                # Auxiliary calculations
                k = dtheta[p-1]
                try:
                    prev_dddtheta = ((k**2)/hbars - 2*k**4 - 3*k**6 + ddtheta[p-1]**2 + 
                                   7*hbars*ddtheta[p-1]**2*k**2) / (2*k*(1+hbars*k**2)) - \
                                  (c*np.sin(theta[p-1]+phi)*(1+hbars*k**2)**3) / (2*hbars*k)
                except:
                    # Handle potential division by zero
                    prev_dddtheta = 0
                
                ddtheta[p] = ddtheta[p-1] + h * prev_dddtheta
                dtheta[p] = dtheta[p-1] + h * ddtheta[p-1]
                theta[p] = theta[p-1] + h * dtheta[p-1]
                x[p] = x[p-1] + 0.5 * h * (np.cos(theta[p]) + np.cos(theta[p-1]))
                y[p] = y[p-1] + 0.5 * h * (np.sin(theta[p]) + np.sin(theta[p-1]))

            err_val = abs(x1 - x[-1]) + abs(y1 - y[-1]) + abs(th1 - theta[-1]) + abs(k1 - dtheta[-1])
            
            # Store the results in the instance
            self.x = x
            self.y = y
            self.theta = theta
            self.dtheta = dtheta
            self.ddtheta = ddtheta
            self.l = l
            
            return err_val
    
    errfunc = ErrorFunction()
    
    options = {'disp': False}
    optimized_param = fmin(errfunc, param_init, **options)
    
    # Get final error value
    err = errfunc(optimized_param)
    
    total_length_in_TI = h * np.sum(np.sqrt(1 + errfunc.dtheta ** 2))
    elastica_in_TI_value = h * np.sum((errfunc.dtheta ** 2 + hbars * errfunc.dtheta ** 4 + hbars * errfunc.ddtheta ** 2) / 
                               ((1 + hbars * errfunc.dtheta ** 2) ** 3))
    
    print(f"Elastica in TI: err:{err:.6f} c:{optimized_param[0]:.6f} phi:{optimized_param[1]:.6f} g0:{optimized_param[2]:.6f} l={optimized_param[3]:.6f}")
    
    return elastica_in_TI_value, errfunc.x, errfunc.y, errfunc.theta, errfunc.dtheta, errfunc.ddtheta, err