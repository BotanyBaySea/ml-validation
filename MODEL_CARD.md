\# Model Card: Breast Cancer Classifier



\## Intended Use

Predicts malignant vs. benign tumors from 30 measurements. Portfolio demo of GxP-style ML validation. NOT for clinical use.



\## Data

scikit-learn breast cancer dataset (569 samples). 75/25 stratified train/test split, seed 42. Data hashed with SHA-256.



\## Model

Logistic regression (with StandardScaler)



\## Performance (test set)

\- Accuracy: 0.986

\- Malignant recall: 0.981



\## Limitations

\- Small public dataset, not real patient data

\- The model hasn't been checked on data from other hospitals.



\## Monitoring

PSI drift check (threshold 0.2). Stable data = 0.000, shifted data = 0.765.



\## Validation

Requirements URS-01 to URS-06 traced to pytest tests. See docs/.

