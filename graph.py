import matplotlib.pyplot as plt
import matplotlib
import numpy as np


matplotlib.rcParams['text.usetex'] = True
font_size = 30
tnr_font = {'fontname': 'Times New Roman'}
font = {'family': 'Times New Roman',
        'size': 30}
matplotlib.rc('font', **font)

# 100 linearly spaced numbers
theta = np.linspace(0, 2.5, 100)
ro = 1
tau = 1
beta = 0.1
delta = 1.4
delta_sup = 2.5

# the function, which is y = x^2 here
y_1 = ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0 * tau * np.exp(4 * (theta - delta)))
y_2 = ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0.25 * tau * np.exp(4 * (theta - delta)))
y_3 = ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0.5 * tau * np.exp(4 * (theta - delta)))
y_4 = ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (0.75 * tau * np.exp(4 * (theta - delta)))
y_5 = ((ro * tau)/(1 + np.exp(1000 * (1 - theta)))) + (1 * tau * np.exp(4 * (theta - delta)))

# theta_1 = 1.95
# y = ((ro * tau)/(1 + np.exp(1000 * (1 - theta_1)))) + (0.5 * tau * np.exp(4 * (theta_1 - delta)))
# print(y)



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

plt.plot(theta, y_1, 'm', label=r'$\beta$ = 0')
plt.plot(theta, y_2, 'r', label=r'$\beta$ = .25')
plt.plot(theta, y_3, 'c', label=r'$\beta$ = .5')
plt.plot(theta, y_4, 'g', label=r'$\beta$ = .75')
plt.plot(theta, y_5, 'b', label=r'$\beta$ = 1')
plt.legend(loc='upper left')

plt.xlabel(r'\emph{Load factor }$\theta_{i}^{l}$', fontsize=font_size, **tnr_font)
plt.ylabel(r'\emph{crowding penalty }$cp_{i}^{l}$', fontsize=font_size, **tnr_font)


# show the plot
plt.grid()
plt.show()

