import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pandas

#data distribution
jumlah_kucing = numpy.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jumlah_kucing, bins=4)
plt.show()

#skewness
jumlah_kucing = numpy.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pandas.Series(jumlah_kucing)
jumlah_kucing_series.skew()