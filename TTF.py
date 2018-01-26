import numpy as np

def Failure ():
	global S
	global Slast
	global Tlast
	global Area
	global NextFailure
	global NextRepair

	S -= 1
	if S == 1:
		NextFailure = clock + np.random.choice([1,2,3,4,5,6], 1)
	if S == 2:
		NextRepair = clock + 2.5
		NextFailure = clock + np.random.choice([1,2,3,4,5,6], 1)
	Area = Area + Slast * (clock - Tlast)
	Slast = S
	Tlast = clock

def Repair():
	global S
	global Slast
	global Tlast
	global Area
	global NextFailure
	global NextRepair

	S += 1
	if S == 2:
		NextRepair = clock + 2.5
	if S == 3:
		NextRepair = float('inf')
	Area = Area + Slast * (clock - Tlast)
	Slast = S
	Tlast = clock

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


np.random.seed(1) # fix random number seed

Ylist = [] # list to keep samples of time to failure
Arealist = [] # list to keep samples of average # of func. components

# Replication loop
for reps in range(999):
	# initialize clock, state, and next events
	clock = 0
	S = 3
	NextRepair = float('inf')
	NextFailure = np.random.choice([1,2,3,4,5,6], 1)
	# define variables to keep the last state and time, and the area under the sample path
	Slast = S
	Tlast = clock
	Area = 0

	while S > 0: # While system is functional
		NextEvent = Timer()

		if NextEvent == "Repair":
			Repair()
		else:
			Failure()

	# add samples to the lists
	Ylist.append(clock)
	Arealist.append(Area/float(clock))

# print sample averages
print(np.mean(Ylist),np.mean(Arealist))

CI_bond = 1.96*np.sqrt((np.sum([(x-np.mean(Ylist))**2 for x in Ylist])/999)/1000)

print ("95% confidence interval for the expected TTF with 2 spare components is between", 
np.mean(Ylist) + CI_bond, np.mean(Ylist) - CI_bond)
