from __future__ import division
from pylab import plot, show, title, xlabel, ylabel
import numpy as np

# Computer Science FB01, Lab 7, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 7")
print("Сахній Назар ФБ-01")

sunspots = np.loadtxt("sunspots.txt", float)


def first_plot():
    x = sunspots[:, 0]
    y = sunspots[:, 1]
    plot(x, y, "g.", markersize=3)
    xlabel("Порядковий номер місяця, починаючи із січня 1749", fontsize=10)
    ylabel("Кількість затемнень за місяць", fontsize=10, )
    title("Графік кількості сонячних затемнень в залежності від місяця",
          fontsize=12,
          fontweight="bold",
          color="m")
    show()


first_plot()


def second_plot():
    x = sunspots[:1001, 0]
    y = sunspots[:1001, 1]
    plot(x, y, "y.", markersize=3)
    xlabel("Порядковий номер місяця, починаючи із січня 1749", fontsize=10)
    ylabel("Кількість затемнень за місяць", fontsize=10)
    title("Кількість сонячних затемнень в залежності від місяця\n для перших 1000 місяців",
          fontsize=12,
          fontweight="bold",
          color="b")
    show()


second_plot()


def moving_ave(yk, r):
    ave_value = []
    for i in range(1001):
        if i < 5 or i > 996:
            Yk = yk[i]
            ave_value.append(Yk)
        elif 5 <= i <= 996:
            Yk = round(sum([yk[j] for j in range(i - 5, i + 5)]) / (2 * r), 1)
            ave_value.append(Yk)
    return ave_value


def third_plot():
    x = sunspots[:1001, 0]
    y = sunspots[:1001, 1]
    plot(x, y, 'k.', markersize=3)
    avarage_y = moving_ave(y, 5)
    plot(x, avarage_y, "r")
    xlabel("Порядковий номер місяця, починаючи із січня 1749", fontsize=10)
    ylabel("Кількість затемнень за місяць", fontsize=10)
    title("Кількість сонячних затемнень в залежності від місяця\n з рухомим середнім",
          fontsize=12,
          fontweight="bold",
          color="r")
    show()


third_plot()
