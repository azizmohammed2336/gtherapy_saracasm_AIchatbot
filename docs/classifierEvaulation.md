# DistilBERT Sarcasm Classifier Evaluation

## Model

- **Architecture:** DistilBERT (`distilbert-base-uncased`)
- **Task:** Binary text classification (sarcastic vs non-sarcastic)

## Dataset

- **Source:** `daniel2588/sarcasm`
- **Total rows in source dataset:** 1,010,826
- **Sample used for training/evaluation:** 50,000

## Sampling Strategy

- 25,000 sarcastic examples (`label=1`)
- 25,000 non-sarcastic examples (`label=0`)
- Balanced class distribution for training

## Data Split

- **Train:** 40,000
- **Test:** 10,000
- **Split ratio:** 80/20

## Training Configuration

- **Runtime:** ~ 1:30 minutes
- **Hardware:** Google Colab T4 GPU

## Training Results

| Epoch | Training Loss | Validation Loss | Accuracy | F1 Score |
|------:|--------------:|----------------:|---------:|---------:|
| 1     | 0.5416        | 0.5405          | 73.08%   | 0.7301   |
| 2     | 0.4313        | 0.5731          | 72.68%   | 0.7246   |
| 3     | 0.2441        | 0.7428          | 72.23%   | 0.7222   |

## Analysis

The model reached its best performance at **Epoch 1** with **73.08% accuracy** and **0.7301 F1**.  
Although training loss decreased steadily (0.54 → 0.43 → 0.24), validation loss increased after Epoch 1 (0.54 → 0.57 → 0.74), indicating mild overfitting beginning at Epoch 2.

The best checkpoint (Epoch 1) was selected automatically using `load_best_model_at_end=True`.  
An accuracy near **73%** is clearly above the **50% random baseline** for binary classification, showing the model learned meaningful sarcasm-related patterns.

## Why ~73% Is a Realistic Ceiling

Sarcasm detection from text alone is inherently difficult, even for humans.  
Without tone, facial cues, or dialogue context, many sarcastic statements remain ambiguous.  
Manual inspection also suggests some label noise (possible mislabels), which lowers the achievable ceiling regardless of model size or longer training. A larger, cleaner dataset with richer context would likely improve performance.

## Note on Load Report Warnings

- **MISSING keys** (e.g., `classifier.weight`, `pre_classifier.weight`) are expected when the classification head is newly initialized before fine-tuning.
- **UNEXPECTED keys** correspond to DistilBERT’s masked language modeling head, which is not used for sequence classification.

These warnings are non-critical and do not affect final evaluation quality.
