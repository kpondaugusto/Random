# %%
import numpy as np 
import matplotlib.pyplot as plt

 ### fully developed laminar flow btw 2 parallel plates
 ### for set x 
mu =  1
x = 1# np.linspace(0,10,100)
y = np.linspace(0,10,100)

h = max(y)

m =  100
b = 0
Px = 0 #-(m*x + b)

def velocityprofile(y):
    return U/h*y - 1/(2*mu)*Px*y*(h-y)

U = max(velocityprofile(y)) #or 0

fig,ax=plt.subplots()

ax.plot(velocityprofile(y),y)
ax.vlines(0,-0.1,10,colors='black',linestyles='dashed')
ax.set_ylabel('y values')
ax.set_xlabel('velocity profile')
# %%
### similarily for circular tube 
def circvelprofile(R):
    return (R**2 - a**2)/(4*mu)*Pz

z = 1
Pz = -(m*z)
R = np.linspace(-10,10,100) #radius
a = max(R)/2

fig,ax=plt.subplots()
ax.plot(circvelprofile(R),R)
# %%
