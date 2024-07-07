import numpy as numpy
import pandas as pandas

#range
jumlah_kucing = numpy.array([1,1,2,2,4,4,4,3,3])
range = jumlah_kucing.max() - jumlah_kucing.min()
print (range)

#interquartille range
jumlah_kucing = numpy.array([1,1,2,2,4,4,4,3,3])
iqr = numpy.percentile(jumlah_kucing,75) - numpy.percentile(jumlah_kucing, 25)
print(iqr)

#variance 
jumlah_kucing = numpy.array([1,1,2,2,4,4,4,3,3])
jumlah_kucing_series = pandas.Series(jumlah_kucing)
print(jumlah_kucing_series.var())

#standard deviation
jumlah_kucing = numpy.array([1,1,2,2,4,4,4,3,3])
jumlah_kucing_series = pandas.Series(jumlah_kucing)
print(jumlah_kucing_series.std())