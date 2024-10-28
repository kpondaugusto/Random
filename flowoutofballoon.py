# %%
import numpy as np 
import matplotlib.pyplot as plt

 

mu =  1
x = 1# np.linspace(0,10,100)
y = np.linspace(0,10,100)

h = max(y)

m =  -100
b = 0
Px = -(m*x + b)

def velocityprofile(y):
    return U/h*y - 1/(2*mu)*Px*y*(h-y)

U = max(velocityprofile(y))

fig,ax=plt.subplots()

ax.plot(velocityprofile(y),y)

# %%
