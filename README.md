# cython_practice

Right now, this repository contains two files: vector_ode.py and vector_ode_class.py. 

## vector_ode.py  
The goal of this file is to get practice with compiling a file with cython, and then to add types using the cdef declaration. Follow the steps [here](http://hplgit.github.io/teamods/cyode/cyode-sphinx/main_cyode.html#using-cython) can get you started with compilation, specifically using their setup.py file. This file also contains numpy types, so I imagine the workflow to be something like:  
* Run vector_ode.py as is. My time to run with python is ~0.006, probably should run a bunch and average.
* Create your own github branch to start experimenting with Cython.  
* Copy vector_ode.py to <new_file_name>.pyx
* Compile with cython, and re-time.
* Copy <new_file_name>.pyx to <new_file_name_2>.pyx
* Start using the cdef declaration to declare the variable types, compile with Cython, run and re-time. This will include figuring out how to cdef numpy stuff.

## vector_ode_class.py  
The goal of this file is to figure out how to use Cython with classes. 

## Re-evaluate, see if we need to figure out more things to implement Cython in our projects.
