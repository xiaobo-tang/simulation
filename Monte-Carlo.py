import numpy as np
import matplotlib.pyplot as plt

#generate 10000 random numbers from an exponential distribution with lambda 0.2 and store them in a list rv_x
rv_x = np.random.exponential(scale=1/0.2, size=10000)

#subtract each element in list rv_x by 2 and evaluate it against 0 to return the bigger value, then store it in list fx
fx = [max(0, x-2) for x in rv_x]

#return cumulative sums from list fx and store them in a new list fval
fval = np.cumsum(fx)

#initiate an empty list avg
avg = []

#for each element in fval calculate the average by dividing it by its index value plus 1, then append them to the avg list
for i in range(0, len(fval)):
    avg.append(fval[i]/(i+1))

#return mean and standard deviation of the elements in list avg
mean = np.mean(avg)
StanDev = np.std(avg,ddof=1) #here specifies ddof = 1 gives an unbiased estimator (using N-1)

UCI = mean + 1.96*StanDev/np.sqrt(len(avg)) #upper 95% CI
LCI = mean - 1.96*StanDev/np.sqrt(len(avg)) #lower 95% CI

#plot the averages showing convergence
plt.plot(avg)
plt.xlabel('# of samples')
plt.ylabel('MAX(0, X-2)')
plt.show()

print "95% Confidence Interval for the expected time to failure is between", UCI, "and", LCI, "with convergence mean of:", mean