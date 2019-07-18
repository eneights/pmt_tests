import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit


def thickness_plots(pmt_num):
    data_path = Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_measurements')

    base_array = np.empty([7, 12])
    above_array = np.empty([7, 12])
    below_array = np.empty([7, 12])
    extra_array = np.empty([20])
    mean_base_array = np.empty([2, 12])
    mean_above_array = np.empty([2, 12])
    mean_below_array = np.empty([2, 12])

    if pmt_num == 3:
        # Reads PMT Data (mm)
        myfile = open(data_path / str('pmt_' + str(pmt_num) + '_below.csv'), 'r')  # Opens file with 1 cm below data
        csv_reader = csv.reader(myfile)
        row_num = -1
        for row in csv_reader:  # Creates array with 1 cm below data
            if row_num >= 0:
                for i in range(7):
                    below_array[i, row_num] = float(row[i])
            row_num += 1
        myfile.close()
        myfile = open(data_path / str('pmt_' + str(pmt_num) + '_extra.csv'), 'r')   # Opens file with extra point 1 data
        csv_reader = csv.reader(myfile)
        row_num = -1
        for row in csv_reader:                                                  # Creates array with extra point 1 data
            if row_num >= 0:
                extra_array[row_num] = float(row[0])
            row_num += 1
        myfile.close()

        # Calculates mean value for each measurement point
        mean_below_array[0, :] = below_array[0, :]
        for i in range(12):
            mean_below_array[1, i] = np.mean(below_array[1:7, i])

    else:
        # Reads PMT Data (mm)
        myfile = open(data_path / str('pmt_' + str(pmt_num) + '_base.csv'), 'r')    # Opens file with base of neck data
        csv_reader = csv.reader(myfile)
        row_num = -1
        for row in csv_reader:                                              # Creates array with base of neck data
            if row_num >= 0:
                for i in range(7):
                    base_array[i, row_num] = float(row[i])
            row_num += 1
        myfile.close()
        myfile = open(data_path / str('pmt_' + str(pmt_num) + '_above.csv'), 'r')   # Opens file with 1 cm above data
        csv_reader = csv.reader(myfile)
        row_num = -1
        for row in csv_reader:                                                      # Creates array with 1 cm above data
            if row_num >= 0:
                for i in range(7):
                    above_array[i, row_num] = float(row[i])
            row_num += 1
        myfile.close()
        myfile = open(data_path / str('pmt_' + str(pmt_num) + '_below.csv'), 'r')   # Opens file with 1 cm below data
        csv_reader = csv.reader(myfile)
        row_num = -1
        for row in csv_reader:                                                      # Creates array with 1 cm below data
            if row_num >= 0:
                for i in range(7):
                    below_array[i, row_num] = float(row[i])
            row_num += 1
        myfile.close()
        myfile = open(data_path / str('pmt_' + str(pmt_num) + '_extra.csv'), 'r')   # Opens file with extra point 1 data
        csv_reader = csv.reader(myfile)
        row_num = -1
        for row in csv_reader:                                                  # Creates array with extra point 1 data
            if row_num >= 0:
                extra_array[row_num] = float(row[0])
            row_num += 1
        myfile.close()

        # Calculates mean value for each measurement point
        mean_base_array[0, :] = base_array[0, :]
        for i in range(12):
            mean_base_array[1, i] = np.mean(base_array[1:7, i])

        mean_above_array[0, :] = above_array[0, :]
        for i in range(12):
            mean_above_array[1, i] = np.mean(above_array[1:7, i])

        mean_below_array[0, :] = below_array[0, :]
        for i in range(12):
            mean_below_array[1, i] = np.mean(below_array[1:7, i])

    # Creates plots
    def func(m, a, b, c):  # Defines Gaussian function (a is amplitude, b is mean, c is standard deviation)
        return a * np.exp(-(m - b) ** 2.0 / (2 * c ** 2))

    n, bins, patches = plt.hist(extra_array, 7)         # Plots histogram
    b_est, c_est = norm.fit(extra_array)                # Calculates mean & standard deviation based on entire array
    bins = np.delete(bins, len(bins) - 1)
    bins_diff = bins[1] - bins[0]
    bins = np.linspace(bins[0] + bins_diff / 2, bins[len(bins) - 1] + bins_diff / 2, len(bins))
    bins_range = np.linspace(bins[0], bins[len(bins) - 1], 10000)           # Creates array of bins
    n_range = np.interp(bins_range, bins, n)                    # Interpolates & creates array of y axis values
    guess = [1, float(b_est), float(c_est)]                     # Defines guess for values of a, b & c in Gaussian fit
    popt, pcov = curve_fit(func, bins_range, n_range, p0=guess, maxfev=5000)        # Finds Gaussian fit
    mu = float(format(popt[1], '.2e'))                          # Calculates mean
    sd = np.abs(float(format(popt[2], '.2e')))                  # Calculates standard deviation
    plt.plot(bins_range, func(bins_range, *popt))               # Plots Gaussian fit
    sum_val = 0
    num = 0
    for item in extra_array:
        sum_val += (item - mu)**2
        num += 1
    sigma = np.sqrt(sum_val / num)
    sigma = float(format(sigma, '.2e'))
    plt.xlabel('Thickness (mm)')
    plt.title('PMT ' + str(pmt_num) + ' Thickness at Point 1\n mean: ' + str(mu) + ' mm' + ', SD: ' + str(sd) + ' mm' +
              ', sigma: ' + str(sigma) + ' mm')
    plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/pmt_' + str(pmt_num) +
                     '_point_1.png'), dpi=360)
    plt.close()

    if pmt_num == 3:
        plt.plot(mean_below_array[0, :], mean_below_array[1, :], 'green')
        plt.errorbar(mean_below_array[0, :], mean_below_array[1, :], sigma)
        plt.xlabel('Azimuthal Angle (degrees)')
        plt.ylabel('Thickness (mm)')
        plt.title('PMT ' + str(pmt_num) + ' Thickness (1 cm Below Base of Neck)')
        plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/pmt_' + str(pmt_num) +
                         '_thicknesses.png'), dpi=360)
        plt.close()
    else:
        x, = plt.plot(mean_base_array[0, :], mean_base_array[1, :], 'blue')
        plt.errorbar(mean_base_array[0, :], mean_base_array[1, :], sigma)
        y, = plt.plot(mean_above_array[0, :], mean_above_array[1, :], 'orange')
        plt.errorbar(mean_above_array[0, :], mean_above_array[1, :], sigma)
        z, = plt.plot(mean_below_array[0, :], mean_below_array[1, :], 'green')
        plt.errorbar(mean_below_array[0, :], mean_below_array[1, :], sigma)
        plt.legend((x, y, z), ('Base of Neck', '1 cm Above Base of Neck', '1 cm Below Base of Neck'))
        plt.xlabel('Azimuthal Angle (degrees)')
        plt.ylabel('Thickness (mm)')
        plt.title('PMT ' + str(pmt_num) + ' Thicknesses')
        plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/pmt_' + str(pmt_num) +
                         '_thicknesses.png'), dpi=360)
        plt.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="thickness_plots", description="Creates plots of PMT thickness measurements")
    parser.add_argument("--pmt_num", type=int, help='number of PMT (default=1)', default=1)
    args = parser.parse_args()

    thickness_plots(args.pmt_num)
