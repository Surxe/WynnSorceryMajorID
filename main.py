from random import seed
from random import random

sorcChance = .3
totalSim = 10000
numSim = 1
totalCasts = 0
seed(1)

while (numSim <= totalSim):
    numCast = 1
    while True:
        if (numCast == 1):
            print("Simulation: ",
                  numSim,
                  " Casts ",
                  numCast,
                  ", ",
                  sep='',
                  end='')
        else:
            print(numCast, ", ", sep='', end='')
        if (random() < (1 - sorcChance)):
            print()
            totalCasts = totalCasts + numCast
            break
        else:
            numCast = numCast + 1
    numSim = numSim + 1

print()
print("Average casts per manual cast by simulation: ", totalCasts / totalSim)
print("Average casts per manual cast by Taylor series: ", .3**0 + .3**1 + .3**2 + .3**3 + .3**4 + .3**5 + .3**6 + .3**7)
