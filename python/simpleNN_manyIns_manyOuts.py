import operations as ops

weights = [
  [.1, .1, -.3],
  [.1, .2, .0],
  [.0, 1.3, .1]
]

def neural_network(input, weights):
  pred = ops.vector_matrix_multiplication(input, weights)
  return pred

games = [8.5, 9.5, 9.9, 9.0]
wlrec = [.65, .8, .8, .9]
nfans = [1.2, 1.3, .5, 1.0]

input = [games[0], wlrec[0], nfans[0]]

pred = neural_network(input, weights)
print(pred)