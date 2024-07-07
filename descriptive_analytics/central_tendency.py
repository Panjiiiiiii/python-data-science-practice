import numpy as numpy
import scipy.stats as stats

#mean (rata-rata)
jumlah_kucing = numpy.array([3,2,5,6,7,8,9])
print(numpy.mean(jumlah_kucing))

#median (nilai tengah)
jumlah_kucing = numpy.array([3,2,5,6,7,8,9,10])
print(numpy.median(jumlah_kucing))

#mode (nilai yang sering muncul)
jumlah_kucing = numpy.array([1,1,2,2,4,4,4,3,3])
mode = stats.mode(jumlah_kucing)[0]
print(mode)