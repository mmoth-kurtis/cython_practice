import scipy.constants as scipy_constants
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import math
import timeit
# This will be the first file practicing Cython. We will solve dy/dt = -0.5*y(t)
# (exponential decay). Once we implement classes, we can solve dy/dt = A(t)*y(t)
# where A(t) is saved as a class property.
# y(t) is an n x 1 vector of functions.

# The first step will be to compile with Cython. Then to correcly "type" everything
# with cdef, including numpy stuff.


# start timer:
tic = timeit.default_timer()
# Length of function vector
n = 5

# Simulation time info
t0 = 0.0
t_end = 100
time_to_eval = np.linspace(0,100,101)

# Initialize the function holder.
y0 = np.empty(n)

# Initial values of y
# starting everything at a value of one to get non-trivial solution
for i in range(n):
    y0[i] = i+1

# Initialize solution holder
y = np.empty((n,np.shape(time_to_eval)[0]))

# Set up A matrix.
A = np.zeros((n,n))
for i in range(n):
    A[i,i] = i+1

# Define deriv function
def deriv(t,y):
    return -0.05*(y)

sol = solve_ivp(deriv,[t0,t_end],y0,t_eval=time_to_eval,method='RK23')

y = sol.y

toc = timeit.default_timer() - tic
print "time to initialize and solve with python: " + str(toc)

for i in range(n):
    plt.plot(time_to_eval,y[i])

plt.show()
