import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit


def thickness_plots(pmt_num):
    data_path = Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_measurements')

    base_array = np.empty([2, 12])
    above_array = np.empty([2, 12])
    below_array = np.empty([2, 12])

    sigma = 0.0152

    # Reads PMT Data (mm)
    myfile = open(data_path / str('pmt_' + str(pmt_num) + '.csv'), 'r')     # Opens file with neck data
    csv_reader = csv.reader(myfile)
    row_num = -1
    for row in csv_reader:                                                  # Creates arrays with neck data
        if row_num >= 0:
            base_array[0, row_num] = float(row[0])
            base_array[1, row_num] = float(row[1])
            above_array[0, row_num] = float(row[0])
            above_array[1, row_num] = float(row[2])
            below_array[0, row_num] = float(row[0])
            below_array[1, row_num] = float(row[3])
        row_num += 1
    myfile.close()

    error_base = np.std(base_array[1, :]) / np.sqrt(len(base_array[1, :]))
    dispersion_base = error_base / np.mean(base_array[1, :])
    dispersion_base = format(dispersion_base * 100, '.2f')

    error_above = np.std(above_array[1, :]) / np.sqrt(len(above_array[1, :]))
    dispersion_above = error_above / np.mean(above_array[1, :])
    dispersion_above = format(dispersion_above * 100, '.2f')

    error_below = np.std(below_array[1, :]) / np.sqrt(len(below_array[1, :]))
    dispersion_below = error_below / np.mean(below_array[1, :])
    dispersion_below = format(dispersion_below * 100, '.2f')

    # Creates plots
    x, = plt.plot(base_array[0, :], base_array[1, :], 'blue')
    plt.errorbar(base_array[0, :], base_array[1, :], sigma)
    y, = plt.plot(above_array[0, :], above_array[1, :], 'orange')
    plt.errorbar(above_array[0, :], above_array[1, :], sigma)
    z, = plt.plot(below_array[0, :], below_array[1, :], 'green')
    plt.errorbar(below_array[0, :], below_array[1, :], sigma)
    plt.legend((x, y, z), ('Base of Neck', '1 cm Above Base of Neck', '1 cm Below Base of Neck'))
    plt.xlabel('Azimuthal Angle (degrees)')
    plt.ylabel('Thickness (mm)')
    plt.title('PMT ' + str(pmt_num) + ' Thicknesses')
    plt.text(0.05, 0.95, str('Dispersion\nBase: ' + str(dispersion_base) + '%\n1 cm Above: ' + str(dispersion_above)
                             + '%\n1 cm Below: ' + str(dispersion_below) + '%'), transform=ax.transAxes,
             verticalalignment='top', bbox=dict(alpha=0.5))
    plt.savefig(Path(r'/Users/Eliza/Documents/WATCHMAN/PMT Testing/thickness_plots/pmt_' + str(pmt_num) +
                     '_thicknesses.png'), dpi=360)
    plt.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="thickness_plots", description="Creates plots of PMT thickness measurements")
    parser.add_argument("--pmt_num", type=int, help='number of PMT (default=4)', default=4)
    args = parser.parse_args()

    thickness_plots(args.pmt_num)