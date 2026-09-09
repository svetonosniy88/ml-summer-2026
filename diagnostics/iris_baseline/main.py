from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)

print(iris.frame.head(10))

