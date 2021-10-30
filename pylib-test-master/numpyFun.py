import numpy as np
import math

# Basic array
a = np.array([1,2])
print(a)

# Two d array
b = np.array([[1,2],[3,4]])
print(b)

# Create an array from 1-12 with a step of 2
c = np.arange(1,12,2)
print(c)

# Create an array of floats from 1 to 12 with 6 elements (it will calculate even distance)
d = np.linspace(1,12,6)
d

# Reshape array to 3 rows, 2 columns
e = d.reshape(3,2)
e

# Get size data of array
e.size # Just gets number of elements regardless of shape
e.shape # Returns dimensions of array
e.dtype # Returns the datatype of the array (could be a numpy data type)
e.itemsize # Tells you how much memory each item in array takes up

# Multi-dimensional arrays 
f = np.array([(1.5,2,3), (4,5,6)]) # Creates a two-d array
f

# Operations on array made easy
e < 4 # Checks each element of array to see if meets condition
e*3 # Multiplies each element of array * 3

# Create array of zeros
g = np.zeros((3,4))
g

# Create array of ones
h = np.ones((3,4))
h

# Add both of the above arrays together
h+g

# Create array of random values
i = np.random.random((2,3)) # Range from 0 to 1
i

# Set print options for all future print statements on numpy
np.set_printoptions(precision=2, suppress=True)
i

# Create array of random integers
j = np.random.randint(0,10,5) # Random from 0-10, 5 elements
j

# Stat operations
e.sum() # Sums all elements
e.min()
e.max()
e.mean()
e.var() # Get variance
e.std() # Get standard deviation

# Get stat operations on specific items
e.sum(axis=1) # Adds each row
e.sum(axis=0) # Adds each column

# Can load data from a file
data = np.loadtxt("data.txt",dtype=np.uint8,delimiter=",",skiprows=1)

# Arrangement of arrays
k = np.arange(10)
np.random.shuffle(k) # Shuffles the order of the array
k
k = np.sort(k) # Sorts the array
k

# Picks random choice from the array
np.random.choice(k)

## MY OWN STUFF ##
a_1 = np.array([(1,2,3),(4,5,6)])
a_2 = np.array([(1,2),(3,4),(5,6)])

a_1 * a_2.transpose() # Multiplying the arrays together requires transpose on one of the elements

# Cross Products
b_1 = np.array([(1,2,3),(4,5,6),(7,8,9)])
b_2 = np.array([(3,2,1),(6,5,4),(9,8,7)])

np.cross(b_1,b_2)

# Dot Products
c_1 = np.array((1,2,-1))
c_2 = np.array((3,1,0))

np.dot(c_1,c_2)

# Vector Addition and Subtraction
d_1 = np.array([1,3])
d_2 = np.array([5,1])

d_1 - d_2
d_1 + d_2

# Magnitude
e_1 = np.array([11,4])
math.sqrt(np.sum(e_1*e_1)) #OR
e_1_mag = np.linalg.norm(e_1)

# Direction
e_1_dir_vec = e_1/e_1_mag # Gets direction
np.linalg.norm(e_1_dir_vec) # Check work step, Should be very close to 1

# Identity Matrix
np.identity(3)

# Determinent
f_1 = np.array([[1, 2], [3, 4]])
np.linalg.det(f_1)

# Inverse
np.linalg.inv(f_1)

# Projections
g_1 = np.array([1,2])
g_base = np.array([1,1])

g_base_unit = 1/np.linalg.norm(g_base)
g_1_proj = (g_1 * g_base_unit) * g_base_unit

# Check parallel
h_1 = np.array([1,1])
h_2 = np.array([2,2])

h_1/np.linalg.norm(h_1) == h_2/np.linalg.norm(h_2)

# Check orthogonal
h_1 = np.array([1,1])
h_2 = np.array([1,-1])

np.dot(h_1,h_2) == 0