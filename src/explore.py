# Load the built-in example dataset that comes with scikit-learn
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = data.data      # the measurements: one row per sample, 30 columns
y = data.target    # the answer for each row: 0 = malignant, 1 = benign

print("Samples:", X.shape[0])
print("Measurements per sample:", X.shape[1])
print("First 5 measurement names:", list(data.feature_names[:5]))
print("Malignant count:", (y == 0).sum())
print("Benign count:", (y == 1).sum())