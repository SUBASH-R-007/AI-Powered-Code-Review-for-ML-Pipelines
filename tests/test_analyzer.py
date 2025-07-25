# tests/test_analyzer.py

import unittest
from reviewer.analyzer import MLCodeReviewer

class TestMLCodeReviewer(unittest.TestCase):

    def setUp(self):
        """Set up a reviewer instance for all tests."""
        self.reviewer = MLCodeReviewer()

    def test_data_leakage_detection(self):
        """
        Tests that the reviewer correctly identifies data leakage
        when fit_transform is used on a test set.
        """
        leaky_code = """
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target)
scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test) # This is data leakage
        """
        report = self.reviewer.generate_review_report(leaky_code)
        self.assertIn("CRITICAL", report)
        self.assertIn("fit_transform() on test data causes data leakage", report)

    def test_no_issues_found(self):
        """
        Tests that the reviewer gives a clean report for good code.
        """
        good_code = """
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42))
])
# pipe.fit(X_train, y_train)
        """
        report = self.reviewer.generate_review_report(good_code)
        self.assertIn("Excellent", report)

    def test_security_pickle_warning(self):
        """
        Tests that using pickle.load() raises a security warning.
        """
        insecure_code = "import pickle; model = pickle.load(f)"
        report = self.reviewer.generate_review_report(insecure_code)
        self.assertIn("WARNINGS", report)
        self.assertIn("Security risk: pickle.load()", report)

if __name__ == '__main__':
    unittest.main()
