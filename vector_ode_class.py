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


tic = timeit.default_timer()
class ode_solve():

    def __init__(self):

        # Length of function vector
        self.n = 3

        # Simulation time info
        self.t0 = 0.0
        self.t_end = 10
        self.time_to_eval = np.linspace(self.t0,self.t_end,10)

        # Initialize the function holder.
        self.y0 = np.empty(self.n)

        # Initial values of y
        # starting everything at a value of one to get non-trivial solution
        for i in range(self.n):
            self.y0[i] = 1./(i+2)

        print self.y0

        # Initialize solution holder
        self.y = np.empty((self.n,np.shape(self.time_to_eval)[0]))

        # Set up A matrix.
        self.A = np.zeros((self.n,self.n))
        for i in range(self.n):
            self.A[i,i] = float((i+1))/float(i+2)

    # Define deriv function
    def deriv(self,t,y):
        #temp = self.A*y
        #print "shape of A = " + str(np.shape(self.A))
        #print "shape of y = " + str(np.shape(y))
        #print "temp " +str(temp)
        return np.matmul(self.A,y)

    #--------
test_class = ode_solve()

sol = solve_ivp(test_class.deriv,[test_class.t0,test_class.t_end],test_class.y0,t_eval=test_class.time_to_eval,method='RK23')

test_class.y = sol.y

toc = timeit.default_timer() - tic
print "Time to initialize and solve with python: " + str(toc)

for i in range(test_class.n):
    plt.plot(test_class.time_to_eval,test_class.y[i])

plt.show()
