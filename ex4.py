from matplotlib import pyplot as plt
from collections import Counter 

# 4 Construa um histograma envolvendo dados de pagantes e não pagantes.
experiencia_tipo_conta = [
    (0.7, 'paga'),
    (1.9,'não_paga'),
    (2.5,'paga'),
    (4.2,'não_paga'),
    (6,'não_paga'),
    (6.5,'não_paga'),
    (7.5,'não_paga'),
    (8.1,'não_paga'),
    (8.7,'paga'),
    (10,'paga')
]
l1 = [i[0] for i in experiencia_tipo_conta if (i[1] == "paga")]
quartil = lambda grade: grade // 2.5001
histograma = Counter(quartil (grade) for grade in l1 )
plt.bar (
    [
        x for x in histograma.keys()
    ],
    histograma.values(),
    .7
)
plt.title ("Usuário Pagantes")
plt.xlabel ("Quartil")
plt.axis ([-1, 5, 0, 4])
plt.xticks ([i for i in range (5)])
plt.ylabel ("Número de Pagantes")
plt.show()
