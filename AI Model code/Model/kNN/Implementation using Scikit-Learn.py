from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# 1. Load sample dataset (Iris dataset)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create KNN classifier (choosing k=3)
knn = KNeighborsClassifier(n_neighbors=3)

# 4. Fit the model to the training data
knn.fit(X_train, y_train)

# 5. Make predictions and evaluate accuracy
y_pred = knn.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
