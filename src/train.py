from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, recall_score
import joblib

SEED = 42  # fixed seed so every run gives the same result (URS-03)

X, y = load_breast_cancer(return_X_y=True)

# Hold back 25% of samples as a blind test the model never sees while learning
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=SEED, stratify=y)

# Put all measurements on the same scale, then learn the pass/fail rule
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=SEED))
model.fit(X_train, y_train)   # this line is the actual "learning"

# Blind test: predict the held-back samples and compare with the real answers
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred), 3))                 # URS-01
print("Recall (malignant):", round(recall_score(y_test, pred, pos_label=0), 3))  # URS-02

joblib.dump(model, "model.joblib")  # save the trained model to a file
print("Model saved.")

from audit import log_run
log_run({"accuracy": round(accuracy_score(y_test, pred), 3)})