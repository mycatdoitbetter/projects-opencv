import csv
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


files = [str(num) + '.csv' for num in range(53, 59)]

for file in files:
    print(file, '\n\n')
    with open(file, 'r') as infile:
        read = csv.reader(infile, delimiter=',')

        data = []
        for row in read:
            data.append(row)

        true = [int(x) for x in data[0]]
        predict = [int(x) for x in data[1]]

        confusioMatrix = confusion_matrix(true, predict)

        print('Accuracia: {:.2f}'.format(accuracy_score(true, predict)*100))

        print('relatório de classificação: \n', classification_report(true, predict))

        print('\n\n###############################################')