import pandas as pd
import csv
from sklearn.neural_network import MLPClassifier

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

    return x_training, x_test, y_training,  y_test



if __name__ == "__main__":
    file = 'preview_data.txt'
    features = readData(file)

    x_training, x_test, y_training,  y_test = hold_on(features, trainingSize=0.9)

    mlp = MLPClassifier(hidden_layer_sizes=(5, 3), max_iter=3000)

    mlp.fit(x_training, y_training)

    predictions = mlp.predict(x_test)

    predictions = list(predictions)

    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count / len(y_test)
    print("A acuracia usando metodo hold out: {:.4f}".format(accuracy))

    with open("comparação_real_vs_analise.csv", 'w') as file:
        rows = [y_test, predictions]
        writer = csv.writer(file, delimiter = ',')
        writer.writerows(rows)

    x_training, x_test, y_training, y_test = leave_one_out(features)

    count = 0
    sampleCount = 0
    for trainSet, testSet, labelTrain, labelTest in zip(x_training,x_test, y_training,y_test):
        print("Treinando amostra ... {} / {}".format(sampleCount+1, len(y_training)))
        sampleCount += 1

        mlp = MLPClassifier(hidden_layer_sizes=(5, 3), max_iter=3000)

        mlp.fit(trainSet, labelTrain)

        newList = []
        newList.append(testSet)
        predictions = mlp.predict(newList)

        if predictions == labelTest: count += 1

    accuracy = count / len(y_test)

    print("A acuracia usando metodo leave one out: {:.4f}".format(accuracy))


