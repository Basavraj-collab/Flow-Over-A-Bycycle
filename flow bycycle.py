#Program to calculate drag force
import matplotlib.pyplot as plt
#Inputs

#Frontal Area
A = 0.1

#Density
rho = 1.2

#Bycycle Velocity
V = [5,6,7,8,9,10,11,12]
d1 = []
#Calculating relationship between drag force and velocity
#consiedring drag coefficient constant
for v in V:
    d1.append(0.5*0.7*rho*A*v**2)
print(d1)    
plt.plot(V,d1)
plt.xlabel("Velocity(m/s)")
plt.ylabel("Drag Force(N)")
plt.show()
    
#calculating relationship between drag force and drag coefficient
#considering constant velocity
#Drag coefficient
c_d = [0.7,1.15,100]
d2 = []
for cd in c_d:
    d2.append(0.5*cd*rho*A*6**2)

plt.plot(c_d,d2)
plt.xlabel("Coeffient of Drag")
plt.ylabel("Drag Force(N)")
plt.show()
