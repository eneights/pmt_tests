import numpy as np

one_point_array = np.array([0.166, 0.164, 0.168, 0.168, 0.169, 0.167, 0.167, 0.168, 0.170, 0.169])
around_neck_array = np.array([0.169, 0.170, 0.187, 0.177, 0.196, 0.191, 0.197, 0.176])

error_mean_one_point = np.std(one_point_array) / np.sqrt(len(one_point_array))
error_mean_around_neck = np.std(around_neck_array) / np.sqrt(len(around_neck_array))

error_relative_one_point = error_mean_one_point / np.mean(one_point_array)
error_relative_around_neck = error_mean_around_neck / np.mean(around_neck_array)

error_one_pt = format(error_relative_one_point * 100, '.2f')
error_many_pts = format(error_relative_around_neck * 100, '.2f')

print('error at point = ' + error_one_pt + '%')
print('error in variation = ' + error_many_pts + '%')
