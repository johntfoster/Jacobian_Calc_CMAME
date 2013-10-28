#!/usr/bin/env python
import speed
import accuracy
import numpy as np

import matplotlib 
matplotlib.use('pgf')
import matplotlib.pyplot as plt
#import mpl_toolkits.axisartist as axisartist

font = {'family':'serif',
	'serif':['Times'],
	'size':12}

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#matplotlib.rc('font', **font)

speed_data = speed.Speed()
accuracy_data = accuracy.Accuracy()

speed_averages = {}
speed_per_mat_element = {}
accuracy_averages = {}
accuracy_per_mat_element = {}

series_to_rowcount = {}
series_to_rowcount[1000.0] = 3000.0
series_to_rowcount[2000.0] = 5400.0
series_to_rowcount[3000.0] = 8526.0
series_to_rowcount[4000.0] = 12288.0
series_to_rowcount[6000.0] = 18468.0
series_to_rowcount[8000.0] = 24000.0
series_to_rowcount[12000.0] = 33396.0
series_to_rowcount[16000.0] = 50700.0
series_to_rowcount[32000.0] = 96768.0

series_to_nonzero_entries = {}
series_to_nonzero_entries[1000.0] = 1994454.0 
series_to_nonzero_entries[2000.0] = 4252230.0
series_to_nonzero_entries[3000.0] = 7792128.0
series_to_nonzero_entries[4000.0] = 15389352.0
series_to_nonzero_entries[6000.0] = 20027466.0
series_to_nonzero_entries[8000.0] = 31388724.0
series_to_nonzero_entries[12000.0] = 40060026.0
series_to_nonzero_entries[16000.0] = 83778480.0
series_to_nonzero_entries[32000.0] = 165140640.0


xlimit = 100000.0
xmin = 2000.0


marker = ""
c =""
fig1= plt.figure(1, figsize=(4,3.7))
ax1 = fig1.add_subplot(111)


print speed_data.master_data_map
for subkey in speed_data.master_data_map[speed_data.master_data_map.keys()[0]]:
	speed_averages[subkey] = [[],[]]
	speed_per_mat_element[subkey] = []
	accuracy_averages[subkey] = [[],[]]
	accuracy_per_mat_element[subkey] = []

for index,key in enumerate(speed_data.master_data_map.keys()):
	print "The key is: " + str(key)
	for subindex, subkey in enumerate(speed_data.master_data_map[key]):
		print "The subkey is: " + str(subkey)
		subdata = [float(entry) for entry in speed_data.master_data_map[key][subkey]]
		speed_averages[subkey][1].append(np.average(np.copy(subdata)))
		speed_averages[subkey][0].append(series_to_nonzero_entries[float(key)])		



for index, key in enumerate(accuracy_data.master_data_map.keys()):
	print "The key is: " + str(key)
	for subindex, subkey in enumerate(accuracy_data.master_data_map[key]):
		print "The subkey is: " + str(subkey)
		subdata = [float(entry) for entry in accuracy_data.master_data_map[key][subkey]]
		accuracy_averages[subkey][1].append(np.average(np.copy(subdata)))
		accuracy_averages[subkey][0].append(series_to_nonzero_entries[float(key)])
		accuracy_per_mat_element[subkey].append(accuracy_averages[subkey][1][-1])
		#/accuracy_averages[subkey][0][-1])

print "The speed averages are:", speed_averages
print "The accuracy averages are:", accuracy_averages
cs = ax1.scatter(speed_averages['CS'][0][:], speed_averages['CS'][1][:], marker='^', c='g', s=64)
cd = ax1.scatter(speed_averages['CD'][0][:], speed_averages['CD'][1][:], marker='x', c='r', s=64 )
fd = ax1.scatter(speed_averages['FD'][0][:], speed_averages['FD'][1][:], marker='s', c='b', s=64) 
ad = ax1.scatter(speed_averages['AD'][0][:], speed_averages['AD'][1][:], marker='o', c='y', s=64)
plt.xlim(1.e5, 1.e9)
plt.xlabel("Number of nonzero elements in TS")
plt.ylabel("Average time to compute TS (s)")
#plt.title("Average time to compute a Jacobian matrix vs.\nnumber of nonzero Jacobian matrix elements")
plt.legend([cs, cd, fd, ad],['CS', 'CD', 'FD', 'AD'], scatterpoints = 1, loc='upper left', bbox_to_anchor=(0., 1.),
                  fancybox=True, shadow=True, ncol=1)

plt.xscale('log')
plt.yscale('log')

plt.grid(True)
plt.grid(which='major', linestyle='--', color='grey')

plt.yticks([.1,1.0, 10.0, 100.0, 1000.0], [.1, 1.0, 10.0, 100.0, 1000.0])

fig1.savefig("serial_speed.pgf")

fig2= plt.figure(2, figsize=(4,3.9))
ax2 = fig2.add_subplot(111)


cs2= ax2.scatter(accuracy_averages['CS'][0][:], accuracy_averages['CS'][1][:], marker='^', c='g', s=64)
cd2= ax2.scatter(accuracy_averages['CD'][0][:], accuracy_averages['CD'][1][:], marker='x', c='r', s=64 )
fd2= ax2.scatter(accuracy_averages['FD'][0][:], accuracy_averages['FD'][1][:], marker='s', c='b', s=64) 
plt.xlim(1.e5, 1.e9)
#plt.xticks(np.arange(1.e-10, 1.0, .25))
plt.xlabel("Number of nonzero elements in TS")
plt.ylabel("$l^2$ norm of difference to AD TS (MPa)")
#plt.title("Frobenius norm of difference to AD TS vs.\nnumber of nonzero TS elements")
plt.legend([cs2, cd2, fd2],['CS', 'CD', 'FD'], scatterpoints = 1, loc='upper left', bbox_to_anchor=(0., .38),
                  fancybox=True, shadow=True, ncol=1)

plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.grid(which='major', linestyle='--', color='grey')

plt.yticks([1.E-10, 1.E-7, 1.E-4, 1.E-1, 1.E2], [1.E-10, 1.E-7, 1.E-4, 1.E-1,1.E2])

beta1, beta0 = np.polyfit(np.log10(np.array(accuracy_averages['CD'][0][:])), np.array(accuracy_averages['CD'][1][:]), 1)
print accuracy_averages['CD'][1][:]
print accuracy_averages['CD'][0][:]
print "beta0 is ", beta0
print "beta1 is ", beta1
yvals = beta0*np.ones(9) + beta1*np.log10(np.array(accuracy_averages['CD'][0][:]))
print "yvals are ", yvals
#fitcs = ax2.scatter(accuracy_averages['CD'][0][:], yvals)


fig2.savefig("serial_accuracy.pgf")
plt.show()

