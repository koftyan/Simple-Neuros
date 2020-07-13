from operations import element_multiplication
weights = [.3, .2, .9]

def neural_network(input, weights):
  pred = element_multiplication(input, weights)
  return pred

wlrec = [.65, .8, .8, .9]
input = wlrec[0]
pred = neural_network(input, weights)

print(pred)
