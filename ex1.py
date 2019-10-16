from matplotlib import pyplot as plt

#1. Construa um gráfico de linha que mostra o número de amigos por usuário.
num_amigos_por_id = [(0, 2), (1, 3), (2, 3), (3, 3), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 1)]
l1 = [ i[0] for i in num_amigos_por_id] 
l2 = [ i[1] for i in num_amigos_por_id] 
plt.plot (l1, l2, color='green', marker='o', linestyle='solid') 
plt.title ("Id Usuário X Num Amigos")   
plt.xlabel ("Id do Usuário")
plt.xticks ([i for i in range (11)])
plt.ylabel ("Qtde Amigos")
plt.yticks ([i for i in range (5)])
plt.show()