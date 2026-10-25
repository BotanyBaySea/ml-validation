\# Validation Summary Report: Pass/Fail ML Model



Date: 2026-10-18    Performed by: Travis Marks



| ID     | Test / Evidence                  | Result            | Status |

|--------|----------------------------------|-------------------|--------|

| URS-01 | test\_URS01\_accuracy              | Accuracy 0.986    | PASS   |

| URS-02 | test\_URS02\_recall                | Recall 0.981      | PASS   |

| URS-03 | test\_URS03\_reproducible          | Identical runs    | PASS   |

| URS-04 | SHA-256 data hash in audit log   | Hash recorded     | PASS   |

| URS-05 | audit\_log.jsonl entry            | Entry complete    | PASS   |

| URS-06 | drift.py PSI check               | 0.000 / 0.765     | PASS   |



Conclusion: All acceptance criteria met. Model is fit for its intended

use as a demonstration of GxP-style ML validation.

