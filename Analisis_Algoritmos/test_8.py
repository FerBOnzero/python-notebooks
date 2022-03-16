def max_subsecuencia(arr):
    n = len(arr)
    global maximum

    if n == 1 :
        return 1

    maximo = 1

    for i in range(1, n):
        res = max_subsecuencia(arr[:i])
        if arr[i-1] < arr[n-1] and res+1 > maximo:
            maximo = res + 1

    maximum = max(maximum , maximo)
  
    return maximo

def subsecuencia(arr):

  global maximum
  maximum = 1
  max_subsecuencia(arr)

  return maximum

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
n = len(arr)
print ("La longitud de la subsecuencia máxima usando recursividad de [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] es:")
print (subsecuencia(arr))
print('La longitud de la subsecuencia máxima usando recursividad de [4, 2, -1, 3, 2, 3] es:')
print(subsecuencia([4, 2, -1, 3, 2, 3]))
print('La longitud de la subsecuencia máxima usando recursividad de [4, 11, 6, 7, 5] es:')
print(subsecuencia([4, 11, 6, 7, 5]))


def max_subsecuencia_iterativa(arr):
  n = len(arr)

  lis = [1]*n

  for i in range (1 , n):
    for j in range(0 , i):
      if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
        lis[i] = lis[j]+1

  maximum = 0

  for i in range(n):
    maximum = max(maximum , lis[i])

  return maximum

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("La longitud de la subsecuencia más larga usando iteración de [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] es:")
print(max_subsecuencia_iterativa(arr))
print('La longitud de la subsecuencia máxima usando iteración de [4, 2, -1, 3, 2, 3] es:')
print(max_subsecuencia_iterativa([4, 2, -1, 3, 2, 3]))
print('La longitud de la subsecuencia máxima usando iteración de [4, 11, 6, 7, 5] es:')
print(max_subsecuencia_iterativa([4, 11, 6, 7, 5]))
print(max_subsecuencia_iterativa([1]))