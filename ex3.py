from matplotlib import pyplot as plt

# 3 Construa um gráfico de dispersão envolvendo salário e tempo de experiência.
salarios_experiencia = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]
l1 = [ i[0]/1000 for i in salarios_experiencia]
l2 = [ i[1] for i in salarios_experiencia]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
plt.scatter (l1, l2)
for label, l1_count, l2_count in zip(labels, l1, l2):
    plt.annotate(
        label,
        xy = (l1_count,l2_count),
        xytext = (-5, 5),
        textcoords = 'offset points'
    )
plt.title ("Salário X Tempo de Experiência")
plt.xlabel ("Salário em R$ mil")
plt.ylabel ("Tempo de Experiência")
plt.show()