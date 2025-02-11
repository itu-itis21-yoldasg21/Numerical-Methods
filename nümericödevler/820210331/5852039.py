#Gülce Su Yoldaş 820210331

import numpy as np
import matplotlib.pyplot as plt


xi = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10])
yi = np.array([0.72, 1.63, 1.88, 3.39, 4.02, 3.89, 4.25, 3.99, 4.68, 5.03, 5.27, 4.82, 5.67, 5.95, 5.72, 6.01, 5.5, 6.41, 5.83, 6.33])


sum_xi = np.sum(xi) #for part a
sum_yi = np.sum(yi)
sum_xi_square = np.sum(xi**2)
sum_xi_yi = np.sum(xi * yi)
b = (20 * sum_xi_yi - sum_xi * sum_yi) / (20 * sum_xi_square - sum_xi**2)
a = (sum_yi - b * sum_xi) / 20
print("b",b)
print("a",a)
sum_xi_cube = np.sum(xi**3)  #for part b
sum_xi_fourth = np.sum(xi**4)
sum_xi_square_yi = np.sum(xi**2 * yi)
sum_xi_yi = np.sum(xi * yi)
c = (20 * sum_xi_square * sum_yi - sum_xi * sum_xi_yi * sum_xi + sum_xi_cube * sum_yi - sum_xi_square * sum_xi_yi) / (20 * sum_xi_fourth - sum_xi_square**2 )
d = (20 * sum_xi_yi * sum_xi_square - sum_xi * sum_xi_square * sum_yi + sum_xi_cube * sum_yi - sum_xi_square * sum_xi_yi) / (20 * sum_xi_fourth - sum_xi_square**2)
e = ( sum_yi - c * sum_xi_square - d * sum_xi) / (20)
print("c",c)
print("d",d)
print("e",e)

sum_ln_xi = np.sum(np.log(xi))  #for part c
sum_ln_xi_yi = np.sum(np.log(xi) * yi)
sum_ln_xi_square = np.sum(np.log(xi) * np.log(xi))
k = (sum_ln_xi_square * sum_ln_xi_yi - sum_ln_xi * sum_yi) / (20 * sum_ln_xi_square - sum_ln_xi**2)
m = (20 * sum_ln_xi * sum_yi - sum_ln_xi* sum_yi) / (20 * sum_ln_xi_square - sum_ln_xi**2)
print("k",k)
print("m",m)

plt.scatter(xi, yi, label='Data Points')
x_vals = np.linspace(0.5, 5.5, 10)
plt.plot(x_vals, a + b * x_vals, label='y = {:.2f} + {:.4f}x'.format(a, b))
plt.plot(x_vals, c * x_vals**2 + d * x_vals + e, label='y = {:.4f}x**2 + {:.4f}x + {:.4f}'.format(c, d, e ))
plt.plot(x_vals, k + m * np.log(x_vals), label='y ={:.4f} + {:.4f}ln(x)'.format(k,m ) )

plt.show()
