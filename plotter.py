from InterfaceMainMenu import *
import matplotlib.pyplot as plt

def plotFeatures(feature1 : int, feature2: int, dataset):
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for instance in dataset:
        features = instance.getFeatures({feature1, feature2})
        if instance.label == 1.0:
            x1.append(features[0])
            y1.append(features[1])
        elif instance.label == 2.0:
            x2.append(features[0])
            y2.append(features[1])
        else:
            print("BAD")
            
    # print("x1", x1)
    # print("y1", y1)
    # print("x2", x2)
    # print("y2", y2)
    
    plt.title(file + ' features ' + str(feature1) + ' and ' + str(feature2))
    plt.xlabel("Feature " + str(feature1))
    plt.ylabel("Feature " + str(feature2))
    plt.scatter(x1, y1)
    plt.scatter(x2, y2)
    plt.show()
    # for row in range(len(dataset)):
    #     currRow = dataset[row]
    #     # if currRow[0] == 1.0: 
    #     print(currRow)

file = "large-test-dataset.txt"           
plotFeatures(1,2, inputdata(file))