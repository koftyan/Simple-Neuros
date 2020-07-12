weight = 0.1
def neural_network(input, weight):
  prediction = input * weight
  return prediction

number_of_games = [8.5, 9.5, 10]
input = number_of_games[0]
pred = neural_network(input, weight)
print(pred)