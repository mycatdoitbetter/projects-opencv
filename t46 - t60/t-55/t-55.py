import numpy as np
import pandas as pd
import math
import operator
import csv
import cv2

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

def knn_classifier(x_training, x_test, y_training, k_neigbours = 3):
    assert (k_neigbours % 2), "Número de vizinhos desconhecidos."

    preview = []

    for x1 in x_test:
        class_prediction = np.zeros(max(y_training) + 1)
        distance = []

        for x2, label2 in zip(x_training, y_training):
            euclidian_dis = euclidian_distance(x1, x2)
            distance.append((label2, euclidian_dis))
            distance.sort(key = operator.itemgetter(1))
            smallest_dist = distance[:k_neigbours]

            for label, dist in smallest_dist: class_prediction[int(label)] += 1

        preview.append(max(range(len(class_prediction)), key = class_prediction.__getitem__))

    return preview


if __name__ == "__main__":
    file = 'preview_data.txt'
    features = readData(file)

    x_training, x_test, y_training, y_test = hold_on(features, trainingSize=0.8)

    y_training = np.reshape(y_training, (-1, 1))

    knn= cv2.ml.KNearest_create()

    knn.train(np.asarray(x_training, np.float32), cv2.ml.ROW_SAMPLE, y_training)

    ret, results, neighbors, dist = knn.findNearest(np.asarray(x_test, np.float32), k=3)

    predictions = [int(x) for x in results]


    count = 0
    for x, y in zip(y_test, predictions):
        if x == y: count += 1

    accuracy = count / len(y_test)

    print("Acuracia do metodo hold out: {0:.2f}%".format(accuracy * 100))

    with open("real_e_previsão_KNN.csv", "w") as file_knn:
        rows = [y_test, predictions]
        writer = csv.writer(file_knn, delimiter = ',')
        writer.writerows(rows)

    x_training, x_test, y_training, y_test = leave_one_out(features)

    predictions = np.zeros(int(max(y_training[0])) + 1)
    count = 0

    for training_set, test_set, training_label, test_label in zip(x_training, x_test, y_training, y_test):

        training_label = np.reshape(training_label, (-1, 1))

        knn = cv2.ml.KNearest_create()

        knn.train(np.asarray(training_set, np.float32),cv2.ml.ROW_SAMPLE, training_label )

        test_list = []
        test_list.append(test_set)
        ret, results, neighbors, dist = knn.findNearest(np.asarray(test_list, np.float32), k=3)

        if results[0] == test_label: count == 1
    accuracy= count / len(y_test)

    print('acuracia do metodo leave one out: {:.4f}'.format(accuracy))


