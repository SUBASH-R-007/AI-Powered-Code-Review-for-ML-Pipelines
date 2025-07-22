import sys
import os
# Add the parent directory (backend) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.analysis.extractor import analyze_code
import json
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import precision_score, recall_score, f1_score
import logging

logger = logging.getLogger(__name__)

def train_model(data_path: str, model_path: str):
    # Load data
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Prepare features and labels
    X = []
    y = []
    
    for item in data:
        issues = analyze_code(item["code"])
        X.append(
            {
                "code_length": len(item["code"]),
                "num_issues": len(issues)
            }
                )
        y.append(1 if issues else 0)
    
    # Vectorize features
    vectorizer = DictVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_vectorized, y)
    
    # Evaluate
    y_pred = model.predict(X_vectorized)
    print(f"Precision: {precision_score(y, y_pred):.3f}")
    print(f"Recall: {recall_score(y, y_pred):.3f}")
    print(f"F1-score: {f1_score(y, y_pred):.3f}")
    
    # Save model and vectorizer
    joblib.dump(model, f"{model_path}/code_review_model.joblib")
    joblib.dump(vectorizer, f"{model_path}/code_vectorizer.joblib")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    train_model("./data/code_data.json", "./models")
