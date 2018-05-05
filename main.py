from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import networkx as nx
import itertools
from sklearn import linear_model
from RegressionConnectome import *

node_count = 4
feature_column_height = 50

iris = datasets.load_iris()
X = iris.data
sample = np.asarray(X[0:feature_column_height])
feature_column = np.zeros((node_count, feature_column_height))
for i in range(0, node_count):
    feature_column[i] = [row[i] for row in sample]
    feature_column[i] = normalize(feature_column[i])

G = nx.DiGraph()
G.add_nodes_from(range(0, node_count))
G.add_edges_from([(a, b) for a in range(0, node_count) for b in range(0, node_count) if (a != b)])

for edge in G.edges:
    G[edge[0]][edge[1]]['slope'], G[edge[0]][edge[1]]['intercept'] = fit_regression(feature_column[edge[0]], feature_column[edge[1]])

print_edges(G)
plt.subplot(211)

plt.plot(feature_column[1], 'b')
payload01 = propagate_on_edge(G, 0, 1, feature_column[0])
#plt.plot(payload01, 'y')
print('01', mse(payload01, feature_column[1]))

i = 0
payload = np.zeros((6, feature_column_height))
for list in list(itertools.permutations([0, 2, 3])):
    payload[i] = propagate_on_chain(G, np.append(list, 1), feature_column[list[0]])
    #plt.plot(payload[i], 'r')
    print(list, mse(payload[i], feature_column[1]))
    i += 1
plt.plot(normalize(np.mean(payload, axis=0)), 'r')
print('Mean:', mse(np.mean(payload, axis=0), feature_column[1]))

trireg = [[feature_column[0].reshape(-1,1)[i][0], feature_column[2].reshape(-1,1)[i][0], feature_column[3].reshape(-1,1)[i][0]] for i in range(0, 50)]
reg = linear_model.LinearRegression(fit_intercept=True)
reg.fit(trireg, feature_column[1].reshape(-1, 1))
result = np.zeros((feature_column_height))
for i in range(0, feature_column_height):
    for j in range(0, node_count-1):
        result[i] += trireg[i][j] * reg.coef_[0][j]
result = normalize(result + reg.intercept_[0])

print('Trireg: ', mse(result, feature_column[1]))
plt.plot(result, 'y')
plt.subplot(212)
nx.draw(G)
plt.show()

"""
for node in range(0, node_count):
    payloads = come_to_direct_node(node)
    slopes = []

    for i in range(0, node_count):
        if i != node:
            slopes = np.append(slopes, G[i][node]['slope'])
        print('Cost: ', np.sum(payloads[i]-feature_column[node])**2)

    payloads = np.delete(payloads, node, 0)

    final_payloads = np.mean(payloads, axis=0)
    print('Special cost: ', np.sum(final_payloads-feature_column[node])**2, '\n')

    plt.plot(final_payloads, 'r-')
"""

"""
fig = plt.figure()
ax = fig.add_subplot(111)#, projection='3d')
ax.plot(feature_column[0], feature_column[1], 'bo')
ax.plot(feature_column[0], reg.coef_[0]*feature_column[0]+reg.intercept_, 'ro')
plt.show()
"""
