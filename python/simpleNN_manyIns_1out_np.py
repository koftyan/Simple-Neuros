import numpy as np
weights = np.array([.1, .2, 0])
def neural_network(input, weights):
  pred = input.dot(weights)
  return pred

games = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([.65, .8, .8, .9])
nfans = np.array([1.2, 1.3, .5, 1.0])

input = np.array([games[0], wlrec[0], nfans[0]])
pred = neural_network(input, weights)
print(pred)