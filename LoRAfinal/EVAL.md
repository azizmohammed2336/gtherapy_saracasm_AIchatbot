# Week 4 — Therapeutic Response Model Evaluation

## Model
**Qwen2.5-3B-Instruct** fine-tuned with **LoRA**

## Dataset
- **Source:** `mpingale/mental-health-chat-dataset`
- **Total examples:** 2,775
- **Split (reported):** 2,350 train / 262 test (90/10 reported)

## Training Configuration
- **Training time:** ~55 minutes (Google Colab T4 GPU)
- **Trainable parameters:** 3,686,400 / 3,089,625,088 (**0.12%**, LoRA)

## Training Results

| Step | Training Loss | Validation Loss |
|------|----------------|-----------------|
| 50   | 2.1740         | 2.1589          |
| 100  | 2.1221         | 2.1023          |
| 150  | 2.0957         | 2.0881          |
| 200  | 2.0858         | 2.0808          |

## Analysis
The model improved consistently across all 3 epochs, with both training and validation loss decreasing steadily (from ~2.17 to ~2.08).  
The small and stable gap between training and validation loss suggests good generalization to unseen examples, with no clear signs of overfitting.

For a causal language model fine-tuned on a relatively small, domain-specific dataset, a final loss near **2.08** is reasonable. This indicates the model learned therapist-style tone, structure, and response patterns rather than memorizing exact outputs.

## Limitations
- The dataset (2,775 examples) is small for adapting a 3B-parameter model.
- A larger therapeutic conversation dataset would likely improve stability and response quality.
- Loss alone is not sufficient for quality assessment; human evaluation is needed for:
  - empathy
  - coherence
  - appropriateness

## Note on Warnings
PyTorch `use_reentrant` warnings are non-critical and related to gradient checkpointing behavior in PyTorch 2.9+.  
They do not affect the reported training outcomes and can be addressed in future runs by setting `use_reentrant=False` in checkpoint configuration.