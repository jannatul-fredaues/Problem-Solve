import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        # 1. Compute distances between x and all points in training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        
        # 2. Get the indices of the k-nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        
        # 3. Extract the labels of these k neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # 4. Return the most common class label (majority vote)
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
