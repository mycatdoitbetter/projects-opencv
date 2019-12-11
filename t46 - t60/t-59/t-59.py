import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels


def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.get_cmap('Reds')):

    if not title:
        if normalize: title = 'matriz de confusão normalizada'
        else: title = 'matriz de confusão não normalizada'


    confusionMatrix = confusion_matrix(y_true, y_pred)

    classes = unique_labels(y_true, y_pred)
    if normalize:
        confusionMatrix = confusionMatrix.astype('float') / confusionMatrix.sum(axis=1)[:, np.newaxis]
        print("matriz de confusão normalizada")
    else:
        print('matriz de confusão não normalizada')

    print(confusionMatrix)

    fig, ax = plt.subplots()
    im = ax.imshow(confusionMatrix, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)

    ax.set(xticks=np.arange(confusionMatrix.shape[1]),
           yticks=np.arange(confusionMatrix.shape[0]),

           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='rotulo verdadeiro',
           xlabel='rótulo dado')


    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    fmt = '.2f' if normalize else 'd'
    thresh = confusionMatrix.max() / 2.
    for i in range(confusionMatrix.shape[0]):
        for j in range(confusionMatrix.shape[1]):
            ax.text(j, i, format(confusionMatrix[i, j], fmt),
                    ha="center", va="center",
                    color="white" if confusionMatrix[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


files = [str(num) + '.csv' for num in range(53, 59)]

for file in files:
    print(file)
    with open(file, 'r') as infile:
        read = csv.reader(infile, delimiter=',')

        data = []
        for row in read:
            data.append(row)

        class_names = ['0', '1', '2']

        true = [int(x) for x in data[0]]
        pred = [int(x) for x in data[1]]

        plot_confusion_matrix(true, pred, classes=class_names,
                              title='não normalizada')
        plt.show()