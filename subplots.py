import matplotlib.pyplot as plt

Y = [5.3, 5, 6.8, 4.9 - 0.7, -0.2, 0.2, 0.2, 5, 4, 6, 8.2, 7, 5.3, 8.2, 8.9, 13.1, 10.7, 6.2, 12.3, 11.3, 9.1,
     11, 7.9, 4, 2.3, 2, 4, 4]
X = range(len(Y))

plt.bar(X, Y, edgecolor="black")
plt.plot(X, Y)
plt.scatter(X, Y, c='red')
plt.tight_layout()
plt.show()

plt.subplot(1, 2, 1)
plt.plot(X, Y)
plt.subplot(2, 2, 2)
plt.bar(X, Y, edgecolor="black")
plt.subplot(2, 2, 4)
plt.scatter(X, Y, c='red')

plt.tight_layout()
plt.show()
