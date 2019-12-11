import numpy as np
import pandas as pd
import math
import csv
import matplotlib.pyplot as plt
from matplotlib import style

def readData(file):
    return pd.read_csv(file, sep=',', header=None)

def hold_on(df, trainingSize, shuffler = True):

    if shuffler: df = df.sample(frac=1).reset_index(drop=True)

    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    x_training = data[:int(trainingSize * len(data))]
    x_test = data[int(trainingSize * len(data)):]

    y_training = [int(x[-1]) for x in x_training]
    y_test = [int(x[-1]) for x in x_test]

    x_training = [x[:-1] for x in x_training]
    x_test = [x[:-1] for x in x_test]

    return x_training, x_test, y_training, y_test


def leave_one_out(df, shuffler = True):

    if shuffler: df = df.sample(frac = 1).reset_index(drop = True)

    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    x_training = []
    x_test = []
    y_training = []
    y_test = []

    for i in range(len(data)):
        training = data.copy()
        training.remove(data[i])

        test = data[i]

        y_training.append([int(x[-1]) for x in training])
        y_test.append(int(test[-1]))

        x_training.append([x[:-1] for x in training])
        x_test.append(test[:-1])

    return   x_training, x_test, y_training,  y_test,

def euclidian_distance(x1, x2):

    distance = 0.0
    for x, y in zip(x1, x2):
        distance += pow(float(x) - float(y), 2)
        distance = math.sqrt(distance)

    return distance

class KMeans:

    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.centroids = {}

    def fit(self, data):
        # inicializa a contagem dos centroides, tirando o primeiro elemento da lista como primeiro centroide
        for i in range(self.k):
            self.centroids[i] = data[i]

        # iniciando as iterações do método de análise
        for i in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

            # encontrando a distância entre a amostra e o grupo mais proximo a esta, utilizando o centroide para
            #representar os grupos(classes)
            for features in data:
                distances = [np.linalg.norm(np.array(features) - np.array(self.centroids[centroid])) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(features)

            previous = dict(self.centroids)

            # obtem a média de dados de cada classe para recálcular os centroides
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)

            isOptimal = True

            for centroid in self.centroids:
                original_centroid = previous[centroid]

                current = self.centroids[centroid]

                if np.sum((current - original_centroid)/original_centroid * 100) > self.tolerance:
                    isOptimal = False

            # verifica se os centroides não mudaram mais além da tolerância permitida(os iniciais em relação ao novo calculo)
            if isOptimal:
                break

    def predict(self, data):
     distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
     classification = distances.index(min(distances))
     return classification


if __name__ == "__main__":
    file = 'preview_data.txt'
    features = readData(file)

    x_training, x_test, y_training, y_test = hold_on(features, trainingSize=0.8)

    km = KMeans(k = 3, max_iterations=10000)
    km.fit(x_training)

    predictions = []
    for test in x_test:
        predictions.append(km.predict(test))




    count = 0
    for x, y in zip(y_test, predictions):
        if x == y: count += 1

    accuracy = count / len(y_test)

    print("Acuracia do metodo hold out: {0:.2f}%".format(accuracy * 100))

    with open("real_e_previsão_KMeans.csv", "w") as file_knn:
        rows = [y_test, predictions]
        writer = csv.writer(file_knn, delimiter = ',')
        writer.writerows(rows)

    colors = 10 * ["r", "g", "c", "b", "k"]

    for centroid in km.centroids:
        plt.scatter(km.centroids[centroid][0], km.centroids[centroid][0], s=130, marker="x")

        for classification in km.classes:
            color = colors[classification]
            for feature in km.classes[classification]:
                plt.scatter(feature[0], feature[1], color= color, s=30)
    plt.show()

    x_training, x_test, y_training, y_test = leave_one_out(features)

    count = 0

    for training_set, test_set, training_label, test_label in zip(x_training, x_test, y_training, y_test):

        km = KMeans(k = 3, max_iterations=10000)
        km.fit(training_set)

        predictions = []

        predict = km.predict(test_set)

        if predict == test_label: count += 1

    accuracy = count / len(y_test)
    print('Accurácia obtida utilizando leave_one_out: {:.4f}'.format(accuracy))




