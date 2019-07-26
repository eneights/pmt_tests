import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit


def thickness_plots_bulb(pmt_num):
    data_path = Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_measurements')

    data_array = np.empty([5, 12])

    # Reads PMT Data (mm)
    myfile = open(data_path / str('pmt_' + str(pmt_num) + '_bulb.csv'), 'r')    # Opens file with bulb data
    csv_reader = csv.reader(myfile)
    row_num = -1
    for row in csv_reader:                                                      # Creates array with bulb data
        if row_num >= 0:
            for i in range(5):
                data_array[i, row_num] = float(row[i])
        row_num += 1
    myfile.close()

    error_1 = np.std(data_array[1, :]) / np.sqrt(len(data_array[1, :]))
    dispersion_1 = error_1 / np.mean(data_array[1, :])
    dispersion_1 = format(dispersion_1 * 100, '.2f')

    error_2 = np.std(data_array[2, :]) / np.sqrt(len(data_array[2, :]))
    dispersion_2 = error_2 / np.mean(data_array[2, :])
    dispersion_2 = format(dispersion_2 * 100, '.2f')

    error_3 = np.std(data_array[3, :]) / np.sqrt(len(data_array[3, :]))
    dispersion_3 = error_3 / np.mean(data_array[3, :])
    dispersion_3 = format(dispersion_3 * 100, '.2f')

    error_4 = np.std(data_array[4, :]) / np.sqrt(len(data_array[4, :]))
    dispersion_4 = error_4 / np.mean(data_array[4, :])
    dispersion_4 = format(dispersion_4 * 100, '.2f')

    sigma = 0.0152

    if pmt_num == 4:
        x_pt = 75
        y_pt = 3.8
    elif pmt_num == 5:
        x_pt = 100
        y_pt = 5.2
    else:
        x_pt = 200
        y_pt = 2.5

    # Makes plots
    print('Making plots...')
    a, = plt.plot(data_array[0, :], data_array[1, :], 'blue')
    plt.errorbar(data_array[0, :], data_array[1, :], sigma)
    b, = plt.plot(data_array[0, :], data_array[2, :], 'orange')
    plt.errorbar(data_array[0, :], data_array[2, :], sigma)
    c, = plt.plot(data_array[0, :], data_array[3, :], 'green')
    plt.errorbar(data_array[0, :], data_array[3, :], sigma)
    d, = plt.plot(data_array[0, :], data_array[4, :], 'red')
    plt.errorbar(data_array[0, :], data_array[4, :], sigma)
    plt.legend((a, b, c, d), ('Point 1', 'Point 2', 'Point 3', 'Point 4'))
    plt.xlabel('Azimuthal Angle (degrees)')
    plt.ylabel('Thickness (mm)')
    plt.title('PMT ' + str(pmt_num) + ' Thicknesses (Bulb)')
    plt.text(x_pt, y_pt, str('Dispersion:\nPoint 1 - ' + str(dispersion_1) + '%\nPoint 2 - ' + str(dispersion_2)
                             + '%\nPoint 3 - ' + str(dispersion_3) + '%\nPoint 4 - ' + str(dispersion_4) + '%'),
             verticalalignment='top', bbox=dict(alpha=0.5, facecolor='none'))
    plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/pmt_' + str(pmt_num) +
                     '_thicknesses_bulb.png'), dpi=360)
    plt.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="thickness_plots_bulb", description="Creates plot of PMT thickness "
                                                                              "measurements taken on bulb")
    parser.add_argument("--pmt_num", type=int, help='number of PMT (default=4)', default=4)
    args = parser.parse_args()

    thickness_plots_bulb(args.pmt_num)