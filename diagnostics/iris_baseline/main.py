from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)

plt.scatter(
    iris.frame["petal length (cm)"],
    iris.frame["petal width (cm)"],
    c = iris.target,
)

plt.xlabel("Длина лепестка, см")
plt.ylabel("Ширина лепестка, см")
plt.title("Iris: лепестки и виды")
plt.show()