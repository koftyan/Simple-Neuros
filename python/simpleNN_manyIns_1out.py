def w_sum(a, b):
  assert(len(a) == len(b))
  output = 0
  for i in range(len(a)):
    output += (a[i] * b[i])
  return output

def neural_network(input, weights):
  pred = w_sum(input, weights)
  return pred

weights = [.1, .2, 0]

games = [8.5, 9.5, 9.9, 9.0]
wlrec = [.65, .8, .8, .9]
nfans = [1.2, 1.3, .5, 1.0]

input = [games[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)
print(pred)
