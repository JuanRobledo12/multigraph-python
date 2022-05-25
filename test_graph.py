from cProfile import label
import matplotlib.pyplot as plt


x_1 = [1,3,5,4,3,7,9,3,7,3,5,6,9,4,3,2]
y_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

x_2 = [1,4,5,3,2,6,7,4]
y_2 = [2,4,6,8,10,12,14,16]

plt.plot(y_1, x_1, label='wololo')
plt.plot(y_2, x_2, label='oli')
plt.legend()

plt.show()