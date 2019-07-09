import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit

# Broken PMT Data (mm)
base_point_1 = np.array([4.771, 4.763, 4.769, 4.771, 4.779, 4.771])
base_point_2 = np.array([4.573, 4.540, 4.556, 4.529, 4.537, 4.577])
base_point_3 = np.array([4.343, 4.341, 4.329, 4.328, 4.362, 4.315])
base_point_4 = np.array([4.201, 4.207, 4.207, 4.203, 4.204, 4.212])
base_point_5 = np.array([4.301, 4.311, 4.315, 4.311, 4.293, 4.308])
base_point_6 = np.array([4.437, 4.440, 4.446, 4.440, 4.442, 4.440])
base_point_7 = np.array([4.499, 4.500, 4.510, 4.511, 4.503, 4.512])
base_point_8 = np.array([4.618, 4.631, 4.634, 4.640, 4.631, 4.640])
base_point_9 = np.array([4.778, 4.777, 4.788, 4.795, 4.785, 4.769])
base_point_10 = np.array([4.854, 4.869, 4.878, 4.891, 4.881, 4.890])
base_point_11 = np.array([5.041, 5.047, 5.056, 5.045, 5.047, 5.036])
base_point_12 = np.array([5.010, 5.010, 5.007, 5.012, 5.023, 5.006])

above_base_point_1 = np.array([4.552, 4.560, 4.546, 4.554, 4.580, 4.535])
above_base_point_2 = np.array([4.379, 4.386, 4.363, 4.357, 4.413, 4.405])
above_base_point_3 = np.array([4.191, 4.190, 4.200, 4.175, 4.156, 4.169])
above_base_point_4 = np.array([3.945, 3.982, 3.956, 3.974, 3.973, 3.955])
above_base_point_5 = np.array([4.039, 4.047, 4.049, 4.010, 4.021, 4.046])
above_base_point_6 = np.array([4.164, 4.207, 4.201, 4.207, 4.210, 4.223])
above_base_point_7 = np.array([4.281, 4.302, 4.306, 4.286, 4.282, 4.306])
above_base_point_8 = np.array([4.415, 4.424, 4.452, 4.429, 4.432, 4.453])
above_base_point_9 = np.array([4.555, 4.597, 4.554, 4.597, 4.526, 4.553])
above_base_point_10 = np.array([4.625, 4.617, 4.660, 4.625, 4.626, 4.651])
above_base_point_11 = np.array([4.801, 4.802, 4.825, 4.812, 4.804, 4.808])
above_base_point_12 = np.array([4.754, 4.762, 4.774, 4.754, 4.739, 4.762])

below_base_point_1 = np.array([4.596, 4.591, 4.629, 4.584, 4.559, 4.577])
below_base_point_2 = np.array([4.359, 4.264, 4.374, 4.318, 4.306, 4.255])
below_base_point_3 = np.array([4.181, 4.167, 4.224, 4.225, 4.170, 4.244])
below_base_point_4 = np.array([4.093, 4.067, 4.029, 4.087, 4.054, 4.107])
below_base_point_5 = np.array([4.251, 4.229, 4.213, 4.229, 4.216, 4.204])
below_base_point_6 = np.array([4.399, 4.393, 4.406, 4.403, 4.429, 4.415])
below_base_point_7 = np.array([4.452, 4.469, 4.426, 4.460, 4.432, 4.447])
below_base_point_8 = np.array([4.531, 4.489, 4.561, 4.559, 4.563, 4.566])
below_base_point_9 = np.array([4.617, 4.611, 4.657, 4.625, 4.632, 4.609])
below_base_point_10 = np.array([4.809, 4.811, 4.796, 4.841, 4.814, 4.779])
below_base_point_11 = np.array([4.921, 4.906, 4.913, 4.917, 4.929, 4.939])
below_base_point_12 = np.array([4.892, 4.896, 4.906, 4.907, 4.908, 4.919])

extra_point_1 = np.array([4.771, 4.763, 4.769, 4.771, 4.779, 4.771, 4.799, 4.785, 4.774, 4.776, 4.781, 4.788, 4.783,
                          4.756, 4.764, 4.796, 4.774, 4.769, 4.771, 4.774])

# Calculates mean value for each measurement point
base_point_1_mean = np.mean(base_point_1)
base_point_2_mean = np.mean(base_point_2)
base_point_3_mean = np.mean(base_point_3)
base_point_4_mean = np.mean(base_point_4)
base_point_5_mean = np.mean(base_point_5)
base_point_6_mean = np.mean(base_point_6)
base_point_7_mean = np.mean(base_point_7)
base_point_8_mean = np.mean(base_point_8)
base_point_9_mean = np.mean(base_point_9)
base_point_10_mean = np.mean(base_point_10)
base_point_11_mean = np.mean(base_point_11)
base_point_12_mean = np.mean(base_point_12)

above_base_point_1_mean = np.mean(above_base_point_1)
above_base_point_2_mean = np.mean(above_base_point_2)
above_base_point_3_mean = np.mean(above_base_point_3)
above_base_point_4_mean = np.mean(above_base_point_4)
above_base_point_5_mean = np.mean(above_base_point_5)
above_base_point_6_mean = np.mean(above_base_point_6)
above_base_point_7_mean = np.mean(above_base_point_7)
above_base_point_8_mean = np.mean(above_base_point_8)
above_base_point_9_mean = np.mean(above_base_point_9)
above_base_point_10_mean = np.mean(above_base_point_10)
above_base_point_11_mean = np.mean(above_base_point_11)
above_base_point_12_mean = np.mean(above_base_point_12)

below_base_point_1_mean = np.mean(below_base_point_1)
below_base_point_2_mean = np.mean(below_base_point_2)
below_base_point_3_mean = np.mean(below_base_point_3)
below_base_point_4_mean = np.mean(below_base_point_4)
below_base_point_5_mean = np.mean(below_base_point_5)
below_base_point_6_mean = np.mean(below_base_point_6)
below_base_point_7_mean = np.mean(below_base_point_7)
below_base_point_8_mean = np.mean(below_base_point_8)
below_base_point_9_mean = np.mean(below_base_point_9)
below_base_point_10_mean = np.mean(below_base_point_10)
below_base_point_11_mean = np.mean(below_base_point_11)
below_base_point_12_mean = np.mean(below_base_point_12)

angles_array = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
base_array = np.array([base_point_1_mean, base_point_2_mean, base_point_3_mean, base_point_4_mean, base_point_5_mean,
                       base_point_6_mean, base_point_7_mean, base_point_8_mean, base_point_9_mean, base_point_10_mean,
                       base_point_11_mean, base_point_12_mean])
above_base_array = np.array([above_base_point_1_mean, above_base_point_2_mean, above_base_point_3_mean,
                             above_base_point_4_mean, above_base_point_5_mean, above_base_point_6_mean,
                             above_base_point_7_mean, above_base_point_8_mean, above_base_point_9_mean,
                             above_base_point_10_mean, above_base_point_11_mean, above_base_point_12_mean])
below_base_array = np.array([below_base_point_1_mean, below_base_point_2_mean, below_base_point_3_mean,
                             below_base_point_4_mean, below_base_point_5_mean, below_base_point_6_mean,
                             below_base_point_7_mean, below_base_point_8_mean, below_base_point_9_mean,
                             below_base_point_10_mean, below_base_point_11_mean, below_base_point_12_mean])


def func(x, a, b, c):  # Defines Gaussian function (a is amplitude, b is mean, c is standard deviation)
    return a * np.exp(-(x - b) ** 2.0 / (2 * c ** 2))


n, bins, patches = plt.hist(extra_point_1, 7)       # Plots histogram
b_est, c_est = norm.fit(extra_point_1)              # Calculates mean & standard deviation based on entire array
bins = np.delete(bins, len(bins) - 1)
bins_diff = bins[1] - bins[0]
bins = np.linspace(bins[0] + bins_diff / 2, bins[len(bins) - 1] + bins_diff / 2, len(bins))
bins_range = np.linspace(bins[0], bins[len(bins) - 1], 10000)           # Creates array of bins
n_range = np.interp(bins_range, bins, n)                    # Interpolates & creates array of y axis values
guess = [1, float(b_est), float(c_est)]                     # Defines guess for values of a, b & c in Gaussian fit
popt, pcov = curve_fit(func, bins_range, n_range, p0=guess, maxfev=5000)    # Finds Gaussian fit
mu = float(format(popt[1], '.2e'))                          # Calculates mean
sd = np.abs(float(format(popt[2], '.2e')))              # Calculates standard deviation
plt.plot(bins_range, func(bins_range, *popt))           # Plots Gaussian fit
sum_val = 0
num = 0
for item in extra_point_1:
    sum_val += (item - mu)**2
    num += 1
sigma = np.sqrt(sum_val / num)
sigma = float(format(sigma, '.2e'))
print(sigma, sd)
plt.xlabel('Thickness (mm)')
plt.title('PMT 1 Thickness at Point 1\n mean: ' + str(mu) + ' mm' + ', SD: ' + str(sd) + ' mm' + ', sigma: ' +
          str(sigma) + ' mm')
plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/broken_pmt_point_1'), dpi=360)
plt.close()

x, = plt.plot(angles_array, base_array, 'blue')
plt.errorbar(angles_array, base_array, sigma)
y, = plt.plot(angles_array, above_base_array, 'orange')
plt.errorbar(angles_array, above_base_array, sigma)
z, = plt.plot(angles_array, below_base_array, 'green')
plt.errorbar(angles_array, below_base_array, sigma)
plt.legend((x, y, z), ('Base of Neck', '1 cm Above Base of Neck', '1 cm Below Base of Neck'))
plt.xlabel('Azimuthal Angle (degrees)')
plt.ylabel('Thickness (mm)')
plt.title('PMT 1 Thicknesses')
plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/broken_pmt_thicknesses'), dpi=360)
plt.close()
