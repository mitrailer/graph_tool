import matplotlib.pyplot as plt
import matplotlib
import numpy as np


matplotlib.rcParams['text.usetex'] = True

# 100 linearly spaced numbers
theta = np.linspace(0, 2.5, 100)
ro = 1
tau = 1
beta = 0.1
delta = 1.4
delta_sup = 2.5
font_size = 15
# the function, which is y = x^2 here
y_1 = tau + ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0 * tau * np.exp(4 * (theta - delta)))
y_2 = tau + ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0.25 * tau * np.exp(4 * (theta - delta)))
y_3 = tau + ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0.5 * tau * np.exp(4 * (theta - delta)))
y_4 = tau + ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0.75 * tau * np.exp(4 * (theta - delta)))
y_5 = tau + ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (1 * tau * np.exp(4 * (theta - delta)))



# setting the axes at the centre
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('center')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

# plot the function
plt.axvline(x=delta, ls='dashed', color='black')
plt.text(delta, 88, r'$\underline{\delta}$', fontsize=font_size)
plt.axvline(x=delta_sup, ls='dashed', color='black')
plt.text(delta_sup, 88, r'$\bar{\delta}$', fontsize=font_size)

plt.plot(theta, y_1, 'm', label='beta = 0')
plt.plot(theta, y_2, 'r', label='beta = .25')
plt.plot(theta, y_3, 'c', label='beta = .5')
plt.plot(theta, y_4, 'g', label='beta = .75')
plt.plot(theta, y_5, 'b', label='beta = 1')
plt.legend(loc='upper left')

plt.xlabel(r'\emph{Load factor }$\theta_{i}^{l}$', fontsize=font_size)
plt.ylabel(r'\emph{crowding penalty }$cp_{i}^{l}$', fontsize=font_size)

# show the plot
plt.grid()
plt.show()

