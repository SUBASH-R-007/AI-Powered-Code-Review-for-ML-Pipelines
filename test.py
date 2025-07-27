# Test ML Code for Analysis
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load some sample data
data = pd.read_csv('data.csv')
X = data.drop('target', axis=1)
y = data['target']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# This should trigger scaling warnings - using scale-sensitive algorithms without scaling
model1 = LogisticRegression()
model1.fit(X_train, y_train)

model2 = SVC()
model2.fit(X_train, y_train)

# Make predictions
predictions1 = model1.predict(X_test)
predictions2 = model2.predict(X_test)

# Evaluate
score1 = accuracy_score(y_test, predictions1)
score2 = accuracy_score(y_test, predictions2)

print(f"Logistic Regression Score: {score1}")
print(f"SVM Score: {score2}")

# This should trigger some other issues
# Missing random state
X_train_bad, X_test_bad, y_train_bad, y_test_bad = train_test_split(X, y, test_size=0.2)

# Using deprecated imports (if your rules check for this)
from sklearn.cross_validation import cross_val_score  # This is deprecated

# Potential data leakage - fitting on full dataset
scaler = StandardScaler()
scaler.fit(X)  # Should fit only on training data