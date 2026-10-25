\# User Requirements Specification: Pass/Fail ML Model



Intended use: Classify a sample as malignant or benign from 30 lab measurements,

as a demo of validating an ML model under GxP practices. Not for clinical use.



| ID     | Requirement                                         | Acceptance criteria |

|--------|-----------------------------------------------------|---------------------|

| URS-01 | The model shall correctly classify test samples     | Accuracy >= 0.95 on held-out test data |

| URS-02 | The model shall catch true malignant cases          | Recall >= 0.95 for malignant |

| URS-03 | Retraining with the same data gives the same result | Two runs with seed 42 give identical predictions |

| URS-04 | Any change to the input data shall be detectable    | SHA-256 hash of data changes if any value changes |

| URS-05 | Every training run shall be recorded                | Audit log entry with time, user, hashes, metrics |

| URS-06 | The model shall flag when new data drifts           | Drift score > 0.2 flags DRIFT; unchanged data = STABLE |

