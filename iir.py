import random
import matplotlib.pyplot as plt
import numpy as np

#random.normalvariate(0,1)
f=[]
f10=[]
f100=[]
fdiff=[]
for i in range(500):
	f.append(float(1000))
for i in range(1000,1500,1):
	f.append(float(i))
for i in range(500):
	f.append(float(1500))

#add gaussian noise
for i in range(1,len(f)):
	f[i]=f[i] + random.normalvariate(0,20)

alpha10=0.05
alpha100=0.025


f10.append(f[0])
f100.append(f[0])
for i in range(1,len(f)):
	f10.append((alpha10*f[i])+((1-alpha10)*f10[i-1]))
	f100.append((alpha100*f[i])+((1-alpha100)*f100[i-1]))




for i in range(1,len(f10)):
	fdiff.append((f10[i] - f100[i])*10)

plt.plot(f)
plt.plot(f10)
plt.plot(f100)
plt.plot(fdiff)
plt.grid(True)
plt.show()
