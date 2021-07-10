import numpy as np
import math as m
from random import uniform
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import seaborn as sns 

sns.color_palette("viridis", as_cmap=True)
viridis = cm.get_cmap('viridis', 12)
iter = 20
n = 200
omega_list = np.arange(0, 1.002, 0.002)
K_list = np.arange(0, 1.002, 0.002)
results = np.zeros(shape=(501,501))
print("starting...")

for p, omega in enumerate(omega_list):
    for q, K in enumerate(K_list):
        W_mean = 0
        for i in range(iter):
            theta_n = uniform(0, 1)
            W = 0
            for j in range(n):
                theta_before = theta_n
                theta_n = (theta_n + omega - K * m.sin(2 * m.pi * theta_n)) 
                delta_theta = (theta_n - theta_before) % 1
                W = W + delta_theta
            W = W / n
            W_mean = W_mean + W
        W_mean = W_mean / iter
        results[p][q] = W_mean
print("Done")
sns.heatmap(results, cmap='viridis')
plt.show()
            
        



