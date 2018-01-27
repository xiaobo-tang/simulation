import numpy as np

def Failure ():
	global S
	global NextFailure
	global NextRepair

	S -= 1
	if S == 1:
		NextFailure = clock + np.random.choice([1,2,3,4,5,6], 1)
	if S == 2:
		NextRepair = clock + 2.5
		NextFailure = clock + np.random.choice([1,2,3,4,5,6], 1)

def Repair():
	global S
	global NextFailure
	global NextRepair

	S += 1
	if S == 2:
		NextRepair = clock + 2.5
	if S == 3:
		NextRepair = float('inf')

def Timer():
	global clock
	global NextRepair
	global NextFailure

	if NextFailure < NextRepair:
		result = "Failure"
		clock = NextFailure

	else:
		result = "Repair"
		clock = NextRepair
	return result 


np.random.seed(1)
Ylist = []

# Replication loop
for reps in range(999):
	# initialize clock, state, and next events
	clock = 0
	S = 3
	NextRepair = float('inf')
	NextFailure = np.random.choice([1,2,3,4,5,6], 1)

	while S > 0: # While system is functional
		NextEvent = Timer()

		if NextEvent == "Repair":
			Repair()
		else:
			Failure()

	# add samples to the lists
	Ylist.append(clock)

#return mean and standard deviation of the elements in list avg
mean = np.mean(Ylist)
StanDev = np.std(Ylist,ddof=1) #here specifies ddof = 1 gives an unbiased estimator (using N-1)

UCI = mean + 1.96*StanDev/np.sqrt(len(Ylist)) #upper 95% CI
LCI = mean - 1.96*StanDev/np.sqrt(len(Ylist)) #lower 95% CI

print "95% Confidence Interval for the expected TTF with 2 spare components is between", UCI, "and", LCI