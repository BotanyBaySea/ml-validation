import hashlib, json, getpass, datetime
from sklearn.datasets import load_breast_cancer

def sha256_of(data_bytes):
    # A fingerprint: changing even one value gives a completely different hash
    return hashlib.sha256(data_bytes).hexdigest()

def log_run(metrics, model_file="model.joblib", log_file="audit_log.jsonl"):
    X, _ = load_breast_cancer(return_X_y=True)
    entry = {
        "time": datetime.datetime.now().isoformat(),
        "user": getpass.getuser(),
        "data_hash": sha256_of(X.tobytes()),
        "model_hash": sha256_of(open(model_file, "rb").read()),
        "metrics": metrics,
    }
    with open(log_file, "a") as f:   # "a" = append only, never overwrite
        f.write(json.dumps(entry) + "\n")
    print("Audit entry recorded.")