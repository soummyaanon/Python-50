import numpy 
marks = numpy.array([45, 67, 81, 55, 92, 78, 88, 61, 77, 79])
newmarks = numpy.array_split(marks, 5)
print(newmarks)
