from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
import networkx as nx

node_count = 4
feature_column_height = 150

def fit_regression(X, Y):
    reg = linear_model.LinearRegression(fit_intercept=True)
    reg.fit(X.reshape(-1, 1), Y.reshape(-1, 1))
    return reg.coef_[0], reg.intercept_

def come_to_direct_node(target):
    ghosts = np.zeros((node_count, feature_column_height))
    for node in range(0, node_count):
        if (node != target):
            ghosts[node] = feature_column[node] * G[node][target]['slope'] + G[node][target]['intercept']
            plt.plot(ghosts[node], 'y--')
        else:
            ghosts[node] = feature_column[node]
            plt.plot(ghosts[node], 'b-')
    return ghosts

def print_edges():
    for edge in G.edges:
        print(edge, G[edge[0]][edge[1]]['slope'], G[edge[0]][edge[1]]['intercept'])
    print()

def normalize(x):
    normalized = (x-np.min(x))/(np.max(x)-np.min(x))
    return normalized

iris = datasets.load_iris()
X = iris.data
sample = np.asarray(X[0:feature_column_height])
feature_column = np.zeros((node_count, feature_column_height))
for i in range(0, node_count):
    feature_column[i] = [row[i] for row in sample]
feature_column = normalize(feature_column)

G = nx.DiGraph()
G.add_nodes_from(range(0, node_count))
G.add_edges_from([(a, b) for a in range(0, node_count) for b in range(0, node_count) if (a != b)])

for edge in G.edges:
    G[edge[0]][edge[1]]['slope'], G[edge[0]][edge[1]]['intercept'] = fit_regression(feature_column[edge[0]], feature_column[edge[1]])

print_edges()
plt.subplot(211)

for node in range(0, node_count):
    ghosts = come_to_direct_node(node)
    slopes = []

    for i in range(0, node_count):
        if i != node:
            slopes = np.append(slopes, G[i][node]['slope'])
        print('Cost: ', np.sum(ghosts[i]-feature_column[node])**2)

    ghosts = np.delete(ghosts, node, 0)

    final_ghost = np.mean(ghosts, axis=0)
    print('Special cost: ', np.sum(final_ghost-feature_column[node])**2, '\n')

    plt.plot(final_ghost, 'r-')

plt.subplot(212)
nx.draw(G)
plt.show()

"""
fig = plt.figure()
ax = fig.add_subplot(111)#, projection='3d')
ax.plot(feature_column[0], feature_column[1], 'bo')
ax.plot(feature_column[0], reg.coef_[0]*feature_column[0]+reg.intercept_, 'ro')
plt.show()
"""
