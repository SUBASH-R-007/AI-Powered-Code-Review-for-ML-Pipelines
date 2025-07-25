# main.py

from reviewer.analyzer import MLCodeReviewer

def main():
    """Main function demonstrating the enhanced code reviewer"""

    print("🚀 Enhanced ML Code Reviewer - Core Logic")
    print("=" * 50)

    reviewer = MLCodeReviewer()

    test_cases = [
        {
            "name": "Data Leakage + Multiple Issues",
            "code": """
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Simulated data
data = np.random.rand(100, 10)
target = np.random.randint(0, 2, 100)

X_train, X_test, y_train, y_test = train_test_split(data, target)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)  # Data leakage!
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
accuracy = model.score(X_test_scaled, y_test)
"""
        },
        {
            "name": "Perfect ML Pipeline",
            "code": """
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Excellent ML practices
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42, n_estimators=100))
])

param_grid = {'classifier__max_depth': [10, 20, None]}
# Note: X and y are assumed to be defined elsewhere for this snippet
# grid_search = GridSearchCV(pipeline, param_grid, cv=StratifiedKFold(5), scoring='f1')
# cv_scores = cross_val_score(grid_search, X, y, cv=5)
"""
        },
        {
            "name": "Security & Performance Issues",
            "code": """
import pickle
from sklearn.svm import SVC
import pandas as pd

# Multiple security and performance issues
model = pickle.load(open('model.pkl', 'rb'))  # Security risk
data = pd.read_csv('huge_file.csv')  # No nrows limit
svm_model = SVC()  # No scaling, no n_jobs
# svm_model.fit(X, y) # Assumes X, y are defined
eval("print('dangerous')")  # Security risk
"""
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*15} TEST {i}: {test_case['name']} {'='*15}")
        print("\n**CODE:**")
        print("```python")
        print(test_case['code'].strip())
        print("```")
        print("\n**COMPREHENSIVE REVIEW:**")
        review = reviewer.generate_review_report(test_case['code'])
        print(review)
        print("\n" + "-"*70)

    print(f"\n🎉 **Code Review Complete!**")

if __name__ == "__main__":
    main()
