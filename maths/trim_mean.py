from statistics import mean
from scipy import stats
marks=[1,2,3,4,5,34,25,34,6,5,3,23,34,23,12,45,6,78,98,76,87,98,45,34,56,78,65,78,65,52]
print(len(marks))
m=stats.trim_mean(marks,0.02)
print(m)