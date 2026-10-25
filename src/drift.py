import numpy as np
from sklearn.datasets import load_breast_cancer

def psi(expected, actual, bins=10):
    # Population Stability Index: how much a measurement's spread has shifted
    edges = np.histogram_bin_edges(expected, bins=bins)
    e = np.histogram(expected, edges)[0] / len(expected) + 1e-6
    a = np.histogram(actual, edges)[0] / len(actual) + 1e-6
    return float(np.sum((a - e) * np.log(a / e)))

X, _ = load_breast_cancer(return_X_y=True)
col = X[:, 0]                     # first measurement: mean radius

same = psi(col, col)
shifted = psi(col, col * 1.2)     # pretend a new sensor reads 20% high

for name, score in [("Unchanged data", same), ("Shifted data", shifted)]:
    status = "DRIFT" if score > 0.2 else "STABLE"
    print(f"{name}: {score:.3f} -> {status}")