import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO()                 #Create GEKKO model
y = m.Var(0)                #Create GEKKO variable
m.Equation(y.dt()==-y+1)    #Create GEKKO equation
m.time = np.linspace(0,50)  #Time points

#Solve ODE
m.options.IMODE = 4
m.solve()

#Plot results
plt.plot(m.time,y)
plt.xlabel('time')
plt.ylabel('y(t)')

#Calculate the value of y(t) as t tends to infinity
m.options.IMODE = 3
m.solve(disp=False)
print('Final Value: ' + str(y.value))

#Show results
plt.show()