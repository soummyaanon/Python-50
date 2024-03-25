from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Scale the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Create and train a logistic regression model
model = LogisticRegression(max_iter=1000).fit(X, y)

# Print the accuracy of the model on the same dataset
print("Accuracy:", model.score(X, y))