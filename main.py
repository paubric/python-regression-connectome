from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
import networkx as nx

def fit_regression(X, Y):
    reg = linear_model.LinearRegression(fit_intercept=True)
    reg.fit(X.reshape(-1, 1), Y.reshape(-1, 1))
    return reg.coef_[0], reg.intercept_

iris = datasets.load_iris()
X = iris.data
sample = np.asarray(X[0:50])
feature_column = np.zeros((4, 50))
for i in range(0, 4):
    feature_column[i] = [row[i] for row in sample]

G = nx.Graph()
G.add_nodes_from(range(0, 4))
G.add_edges_from([(a, b) for a in range(0, 4) for b in range(0, 4) if (a != b)])
for edge in G.edges:
    G[edge[0]][edge[1]]['slope'], G[edge[0]][edge[1]]['intercept'] = fit_regression(feature_column[edge[0]], feature_column[edge[1]])

print(G.edges(data=True))

"""
fig = plt.figure()
ax = fig.add_subplot(111)#, projection='3d')
ax.plot(feature_column[0], feature_column[1], 'bo')
ax.plot(feature_column[0], reg.coef_[0]*feature_column[0]+reg.intercept_, 'ro')
plt.show()
"""
