import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit


def thickness_plots_bulb(pmt_num):
    data_path = Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_measurements')

    data_array = np.empty([9, 12])
    mean_data_array = np.empty([5, 12])

    # Reads PMT Data (mm)
    myfile = open(data_path / str('pmt_' + str(pmt_num) + '_bulb.csv'), 'r')    # Opens file with bulb data
    csv_reader = csv.reader(myfile)
    row_num = -1
    for row in csv_reader:              # Creates array with base of neck data
        if row_num >= 0:
            for i in range(9):
                data_array[i, row_num] = float(row[i])
        row_num += 1
    myfile.close()

    # Calculates mean value for each measurement point
    mean_data_array[0, :] = data_array[0, :]
    for i in range(12):
        mean_data_array[1, i] = np.mean(data_array[1:3, i])
        mean_data_array[2, i] = np.mean(data_array[3:5, i])
        mean_data_array[3, i] = np.mean(data_array[5:7, i])
        mean_data_array[4, i] = np.mean(data_array[7:9, i])

    # Makes plots
    print('Making plots...')
    a, = plt.plot(mean_data_array[0, :], mean_data_array[1, :], 'blue')
    b, = plt.plot(mean_data_array[0, :], mean_data_array[2, :], 'orange')
    c, = plt.plot(mean_data_array[0, :], mean_data_array[3, :], 'green')
    d, = plt.plot(mean_data_array[0, :], mean_data_array[4, :], 'red')
    plt.legend((a, b, c, d), ('Point 1', 'Point 2', 'Point 3', 'Point 4'))
    plt.xlabel('Azimuthal Angle (degrees)')
    plt.ylabel('Thickness (mm)')
    plt.title('PMT ' + str(pmt_num) + ' Thicknesses (Bulb)')
    plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/pmt_' + str(pmt_num) +
                     '_thicknesses_bulb.png'), dpi=360)
    plt.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="thickness_plots_bulb", description="Creates plot of PMT thickness "
                                                                              "measurements taken on bulb")
    parser.add_argument("--pmt_num", type=int, help='number of PMT (default=1)', default=1)
    args = parser.parse_args()

    thickness_plots_bulb(args.pmt_num)
