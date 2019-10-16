from matplotlib import pyplot as plt

# 2 Construa um gráfico de linha que mostra o número médio de amigos por usuário.
#def media_usuario(l2):
  soma=0
  for i in l2:
    print("soma: ",soma,",i: ",i)
    soma += i
  return soma/len(num_amigos_por_id)
plt.plot (l1, media_usuario(l2), color='green', marker='o', linestyle='solid') 
plt.title ("# medio de amigos / Usuario")   
plt.xlabel ("Usuário")
plt.xticks ([i for i in range (11)])
plt.ylabel ("Med de Amigos")
plt.yticks ([i for i in range (5)])
plt.show()