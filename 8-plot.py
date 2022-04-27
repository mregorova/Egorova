import numpy as np
import matplotlib.pyplot as plt
with open('settings.txt', 'r') as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

x = np.linspace(0, 800, endpoint=True)
y = np.linspace(0, 250, endpoint=True)

data_array = np.loadtxt("data.txt", dtype = int)

fig, ax = plt.subplots(figsize=(16,10), dpi = 400)
ax.plot(data_array, label = "Lab work", color='m', linestyle='-', marker='*', markersize=7, markerfacecolor='c',
markeredgewidth=0.5, markevery=15)

ax.minorticks_on()

#  Определяем внешний вид линий основной сетки:
ax.grid(which='major',
        color = 'gray', 
        linewidth = 0.5)

#  Определяем внешний вид линий вспомогательной
#  сетки:
ax.grid(which='minor', 
        color = 'gray', 
        linestyle = ':',
        linewidth = 0.5)

ax.legend('V(t)', loc='upper right', shadow=True)
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Something about condensator')

ax.text(600, 155, 'Время заряда = 4.21 с',
        fontsize = 7)
ax.text(600, 105, 'Время разряда = 5.65 с',
        fontsize = 7)


fig.savefig("test.svg")
plt.show()