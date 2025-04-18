### Cleanlab
## Quickstart & Core Concepts
A high‑level overview of how Cleanlab detects label issues in any dataset:
https://docs.cleanlab.ai/v2.3.1/

## Filter API (cleanlab.filter)
The low‑level functions for identifying mislabeled examples given your model’s predicted probabilities:

find_label_issues(labels, pred_probs, …)
find_predicted_neq_given(labels, pred_probs)
Read here: 
https://docs.cleanlab.ai/v2.0.0/cleanlab/filter.html

## Classification API (cleanlab.classification)
The CleanLearning class wraps an sklearn model to both detect label errors and train robustly under noise. See:
https://docs.cleanlab.ai/v2.5.0/cleanlab/classification.html

## DataLab Guide (cleanlab.datalab)
Beyond mislabels, Cleanlab can flag outliers, duplicates, drift, etc. The Issue Types guide describes all of them:
https://docs.cleanlab.ai/v2.3.1/tutorials/multilabel_classification.html
