import imageio.v3 as iio

filenames = ['frame_00_delay-0.06s.gif', 'frame_01_delay-0.06s.gif']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)