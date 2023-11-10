class Instance:
    def __init__(self, label: float, features: list):
        self.label = label
        self.features = features

    #takes set of feature indexes, returns list of feature values
    def getFeatures(self, featureSet: set):
        result = []
        for feature in featureSet:
            result.append(self.features[feature])
        return result
    
#[Insance1, Instance2]
#Instance1.label = 1.000000
#Instance1.getFeatures({1,2,3}) = [1234.0, 352.0, 123.0]