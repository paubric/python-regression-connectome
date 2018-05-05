import numpy as np
from sklearn import linear_model

def mse(X, Y):
    return np.mean((X-Y)**2)

def fit_regression(X, Y):
    reg = linear_model.LinearRegression(fit_intercept=True)
    reg.fit(X.reshape(-1, 1), Y.reshape(-1, 1))
    return reg.coef_[0], reg.intercept_

def come_to_direct_node(dst):
    payloads = np.zeros((node_count, feature_column_height))
    for src in range(0, node_count):
        if (src != dst):
            payloads[src] = feature_column[src] * G[src][dst]['slope'] + G[src][dst]['intercept']
            plt.plot(payloads[src], 'y--')
        else:
            payloads[src] = feature_column[node]
            plt.plot(payloads[src], 'b-')
    return payloads

def propagate_on_edge(G, src, dst, payload):
    new_payload = payload * G[src][dst]['slope'] + G[src][dst]['intercept']
    return normalize(new_payload)

def propagate_on_chain(G, chain, payload):
    print('Chain:', chain)
    for i in range(0, len(chain)-1):
        payload = payload * G[chain[i]][chain[i+1]]['slope'] + G[chain[i]][chain[i+1]]['intercept']
    return normalize(payload)

def print_edges(G):
    for edge in G.edges:
        print(edge, G[edge[0]][edge[1]]['slope'], G[edge[0]][edge[1]]['intercept'])
    print()

def normalize(x):
    normalized = (x-np.min(x))/(np.max(x)-np.min(x))
    return normalized
