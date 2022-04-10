import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime

# Check coordinate conversion
# Maybe use binary heatmap instead of gradual seaborn
# the complex roots will lie in the plane [-2, 2]; [-2j, 2j]

def coeff_list(bin_num):
    coeff = []
    for digit in str(bin_num):
        if digit == "0":
            coeff.append(-1)
        else:
            coeff.append(1)
    return coeff

degree = 15
n = degree
root_list = []
resolution = 90 #ensure divisible by 2

print("Roots...")

for i in range(2**n):
    b = bin(i)[2:].zfill(n)
    coeff = coeff_list(b)
    roots = np.roots(coeff)
    root_list.append(roots)

bucketed_map = np.zeros(shape=(resolution,resolution))
#print("root_list", root_list)

print("Bucketing...")

for i in range(len(root_list)):
    x = root_list[i]

    for j in range(len(x)):
        real_part = x[j].real
        complex_part = x[j].imag
        placement_x = round((resolution / 2) * real_part) + round((resolution / 2))
        placement_y = (round((resolution / 2) * complex_part) - round((resolution / 2))) * (-1)

        if placement_y <= (resolution - 1) and placement_x <= (resolution - 1):
            bucketed_map[placement_x][placement_y] += 1        

print("Plotting...")
bucketed_map = np.array(bucketed_map)
vmin = 0
vmax = np.amax(bucketed_map)

plt.figure()
pic = sns.heatmap(bucketed_map, cmap='mako', cbar=False, vmin = vmin, vmax = vmax)
pic.set(xticks=[])
pic.set(yticks=[])
plt.show()

