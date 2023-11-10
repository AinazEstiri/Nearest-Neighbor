from InterfaceMainMenu import *
from classifierClass import Classifier
from validatorClass import Validator
#This is a testing file to see if some of the functions will work.


#print(inputdata('very-small-test-dataset.txt')) #Testing to see if inputdata() works


classifier = Classifier()

# classifier.train(inputdata("small-test-dataset.txt"))

# # Test a new instance
# test_instance = (2.0, [3.9575864, 2.9025602, 0.33396418, 1.9807348, 2.325866, 2.3749735, 1.8660643, 1.6101164, 2.6151125, 2.8727727])
# predicted_label = classifier.test(test_instance)
#print(predicted_label)  # Output should be the dataset trace, and then an output of 2 as its identified class

#print(featuresonly(inputdata("very-small-test-dataset.txt")))

dataset = inputdata('large-test-dataset.txt')
validator = Validator()
#print(validator.evaluate({0, 1, 2}, dataset))
forward_selection(40, validator, dataset, True)
#backward_elimination(10, validator, dataset, True)