matrizuno = [[2,3,2],
             [3,2,3]]

matrizdos = [[2,3],
             [2,3],
             [3,2]]

matriz_resultante =[]
for i in range (len(matrizuno)):
  fila = []
  for j in range(len(matrizdos[0])):
    suma = 0
    for k in range(len(matrizdos)):
      suma += matrizuno[i][k] * matrizdos[k][j]
    fila.append(suma)
  matriz_resultante.append(fila)
      
print(matriz_resultante)   