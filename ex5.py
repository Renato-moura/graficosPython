from matplotlib import pyplot as plt
from collections import Counter

#  5 Construa um histograma de palavras em interesses. Por exemplo, a palavra 
# learning pode aparecer em machine learning e em deep learning. Quebre cada 
# interesse em palavras para fazer a contagem e montar o histograma.
interesses = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"), 
(2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodel"), (2, "pandas"), 
(3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"), 
(5, "Python"), (5, "R"),(5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"), 
(6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),(7, "neural networks"), 
(8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]
frequencia_palavras = Counter (
    palavra
    for usuario, assunto in interesses
    for palavra in assunto.lower().split()
)

d1 = [ e for e in frequencia_palavras.items() if e[1] > 1 ]

plt.bar (
    [
        palavra[0] for palavra in d1
    ],
    [
        palavra[1] for palavra in d1
    ],
    .8
)
plt.title ("Tecnologias com mais citações")
plt.axis ([-0.5, 13.5, 1, 4])
plt.xticks ([i for i in range(14)])
plt.xlabel ("Tecnologia")
plt.yticks ([i for i in range(4)])
plt.ylabel ("Número de citações")
plt.show()