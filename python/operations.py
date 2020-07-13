def elementwise_multiplication(vec_a, vec_b):
  assert(len(vec_a) == len(vec_b))
  product = []
  for i in range(len(vec_a)):
    product.append(vec_a[i] * vec_b[i])
  return product

def elementwise_addition(vec_a, vec_b):
  assert(len(vec_a) == len(vec_b))
  product = []
  for i in range(len(vec_a)):
    product.append(vec_a[i] + vec_b[i])
  return product

def vector_sum(vec):
  sum = 0
  for i in range(len(vec)):
    sum += vec[i]
  return sum

def vector_average(vec):
  return vector_sum(vec) / len(vec)

def element_multiplication(number, vec):
  output = []
  for i in range(len(vec)):
    output.append(vec[i] * number)
  return output

print(elementwise_multiplication([1,2,3], [1,2,3]))
print(elementwise_addition([1,2,3], [1,2,3]))
print(vector_sum([1,2,3]))
print(vector_average([1,2,3]))