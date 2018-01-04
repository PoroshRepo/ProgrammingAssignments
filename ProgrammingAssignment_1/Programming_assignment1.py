import numpy as np


feature = ["a", "c", "d", "b", "a", "d", "c", "a", "b", "b", "d", "a", "c", "d", "c"]
target = ["yes", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "no","yes", "no", "yes", "yes"]

def printProbabilities(t, f, probability):
    
    print("P(target= "+t+"| feature= "+f+") = "+str(probability))

def calculateProbability():
    hit = 0
    probability = 0
    
    for t, t_f in zip(targets, target_freq):
        
        for f, f_f in zip(features, features_freq):
            
            hit = 0
            
            for t_all, f_all in zip(target, feature):
                
                if t_all == t and f_all == f:
                    
                    hit += 1
            
            probability = ( (hit/t_f) * (t_f/len(target)) )/ (f_f/len(feature))
            
            printProbabilities(t, f, probability)


targets, target_freq = np.unique(target, return_counts= True)
features, features_freq = np.unique(feature, return_counts= True)

calculateProbability()



