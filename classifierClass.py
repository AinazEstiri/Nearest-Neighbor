import math

class Classifier:
    def __init__(self):
        self.trainSamples = [] # List to store the training samples
    
    def train(self, samples): 
        self.trainSamples.extend(samples) # Store the training samples for future classification
    
    def test(self, state, featureSubset, trace=False):
        minDistance = float('inf') # Initialize nearest point as None
        nearestPoint = None # Initialize minimum distance as infinity
        
        # Iterate over each training sample to find the nearest point
        for trainSample in self.trainSamples:
            distance = self.euclideanDistance(trainSample.getFeatures(featureSubset), state.getFeatures(featureSubset))
            if distance < minDistance:
                minDistance = distance
                nearestPoint = trainSample
            if trace: 
                print(str(trainSample.label) + " is class " + str(nearestPoint.label))
        # Return the predicted class label of the nearest training point
        return nearestPoint.label  # Return the class label
    
    def euclideanDistance(self, feat1, feat2):
        # Compute the Euclidean distance between two points in an n-dimensional space
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(feat1, feat2)]))
        return distance