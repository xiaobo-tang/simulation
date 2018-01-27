import numpy as np
import scipy.integrate

area_list = []
np.random.seed(1)

for i in range(0,29):
    
    clock = 0
    Xt = 0
    NextArrival = np.random.exponential(scale=1/0.8)
    NextDeparture = float('inf')
    Xt_list = [0]
    clock_list = [0]
    
    while clock < 100000:
    
        if NextArrival < NextDeparture:
            clock = NextArrival
            Xt = Xt + 1
            NextArrival = clock + np.random.exponential(scale=1/0.8)

            if NextDeparture == float('inf'):
                NextDeparture = clock + np.random.exponential(scale=1)
            else:
                NextDeparture = NextDeparture

        else:
            clock = NextDeparture
            Xt = Xt - 1
            NextArrival = NextArrival

            if Xt == 0:
                NextDeparture = float('inf')
            else:
                NextDeparture = clock + np.random.exponential(scale=1)

        Xt_list.append(Xt) 
        clock_list.append(float(clock))

    area = scipy.integrate.simps(Xt_list, clock_list)/100000
    
    area_list.append(area)

print "Averger # of customers over 100K time units under 30 simulations is:", np.mean(area_list)

#The expected value represents the avergae # of customers in the system