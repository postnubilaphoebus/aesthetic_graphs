import numpy as np
from math import floor, pow, sin, pi, ceil
from random import uniform
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime

iter = 20
n = 200
precision = 0.002
omega_list = np.arange(0 + precision, 1 + precision, precision)
K_list = np.arange(0 + precision, 1 + precision, precision)
resolution = int(1 / precision)
results = np.zeros(shape=(resolution,resolution))
theta_list = np.arange(0, 1, 1/iter)

print("Starting circle map computation...")
est_time = ceil(7 * pow(10, -7) * pow(resolution, 2) *  iter * n)
print("Starting time:", datetime.datetime.now().time())

print("Resolution: {} x {}, Precision: {}, n: {}, Number of initial theta conditions: {}".format(resolution, resolution, precision, n, iter))
if est_time < 60:
    print("Estimated time: {} seconds".format(est_time))
elif est_time < 3600:
    print("Estimated time: {} minute(s)".format(ceil(est_time / 60)))
else:
    hours = round((est_time / 3600), 2)
    hour = floor(hours)
    minute = ceil((hours % 1) * 60)
    print("Estimated time: {} hour(s) and {} minute(s)".format(hour, minute))

for p, omega in enumerate(omega_list):
    for q, K in enumerate(K_list):
        W_mean = 0
        for theta_n in theta_list:
            theta_n = (theta_n + uniform(-0.02, 0.02)) % 1
            W = 0
            for j in range(n):
                theta_before = theta_n
                theta_n = (theta_n + omega - K * sin(2 * pi * theta_n)) 
                delta_theta = (theta_n - theta_before) % 1
                W = W + delta_theta
            W = W / n
            W_mean = W_mean + W
        W_mean = W_mean / iter
        results[-q][p] = W_mean

#pyplot.figure(figsize=(13, 13)) #uncomment if you want a larger figure
pic = sns.heatmap(results, cmap='mako', cbar=False)
pic.set(xticks=[])
pic.set(yticks=[])
plt.show()