import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, recall_score

def train_and_predict():
    X, y = load_breast_cancer(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    m = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42))
    m.fit(Xtr, ytr)
    return yte, m.predict(Xte)

def test_URS01_accuracy():
    y, pred = train_and_predict()
    assert accuracy_score(y, pred) >= 0.95

def test_URS02_recall():
    y, pred = train_and_predict()
    assert recall_score(y, pred, pos_label=0) >= 0.95

def test_URS03_reproducible():
    _, a = train_and_predict()
    _, b = train_and_predict()
    assert np.array_equal(a, b)
