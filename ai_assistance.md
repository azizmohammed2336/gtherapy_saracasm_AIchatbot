In this section, I will note how I used Claude to for assitance and debuggin my project.

Here's a full summary of everything we've covered:

---

## March 23 — Model Setup & Environment

**What you asked:** How to run Qwen2.5-7B from a local Mac path on Colab hardware.

**What we did:**

- Diagnosed that your local Mac path (`/Users/kingabdulaziz/...`) doesn't exist on Colab — it's a cloud VM
- Discussed options: upload to Drive, download from HuggingFace, or use HF repo ID directly
- Decided to use Google Drive as persistent storage

**What we debugged:**

- `HFValidationError` — path had too many slashes, HuggingFace treated it as a repo ID
- Colab running on CPU instead of GPU — walked through Runtime → Change runtime type → T4 GPU
- `torch.cuda.is_available()` returning False — runtime wasn't actually switched

---

## April 7 to 14 — Model Selection & Local Setup

**What you asked:** Whether 7B was too big for Colab and whether to use Ollama.

**What we did:**

- Switched from 7B to 3B model — better fit for free Colab T4
- Explained LoRA and why it makes fine-tuning feasible
- Explained Ollama can't fine-tune, only inference
- Decided to run locally on M2 Mac using MPS

**What we debugged:**

- `SystemError: bad call flags` — package version conflict, fixed with clean reinstall
- M2 running out of RAM (15GB used of 16GB) — model too large for Mac with other apps open
- VS Code kernel not switching properly when changing Colab runtime
- Decided to move fully to Colab browser tab instead of VS Code

---

## CONTINUED: Environment Cleanup & Project Structure

**What you asked:** How to properly structure the project, hide file paths, and organize notebooks.

**What we did:**

- Set up `keys.env` to hide local file paths from GitHub
- Used `python-dotenv` to load paths from env file
- Created 4 notebooks: local setup, local every session, Colab setup, Colab every session
- Decided to remove local notebooks and work fully in Colab
- Explained git submodule issue with `qwenModel` folder
- Added `qwenModel/` and `keys.env` to `.gitignore`

**What we debugged:**

- `HFValidationError` on `./qwenModel` path — fixed using `os.path.expanduser()`
- `TypeError: expected str not NoneType` — `keys.env` not loading correctly, fixed with absolute path
- Git submodule warning — fixed with `git rm --cached qwenModel`
- Missing `model-00001-of-00002.safetensors` — partial download, fixed with `hf_hub_download` for just the missing file

---

## April 14 - 21: Sarcasm Classifier

**What you asked:** How to build the sarcasm detection model for Week 3 of your project.

**What we did:**

- Loaded `daniel2588/sarcasm` dataset (1,010,826 rows)
- Discovered dataset was ordered — all 0s first, then all 1s
- Fixed class imbalance by sampling 25k from each label (50k balanced total)
- Fine-tuned DistilBERT for binary classification
- Evaluated with accuracy and F1 score
- Saved classifier to Google Drive

**What we debugged:**

- `evaluation_strategy` renamed to `eval_strategy` in newer transformers version
- `NameError: train_dataset not defined` — cells ran out of order, combined into one cell
- `TypeError: TextEncodeInput must be Union` — None values in comments, fixed with string conversion and `.filter()`
- Classifier not appearing in Drive UI — Drive sync delay, confirmed files existed via `os.listdir()`

**Results:** 73% accuracy, 0.73 F1 — solid result explained by label noise in dataset

---

## CONTINUED: Therapist Fine-tuning

**What you asked:** How to fine-tune Qwen on the mental health dataset.

**What we did:**

- Loaded `mpingale/mental-health-chat-dataset` (2,775 rows)
- Formatted conversations using Qwen chat template with system prompt
- Set up LoRA config (r=16, targeting q_proj and v_proj)
- Confirmed 0.12% trainable parameters (3.6M of 3B)
- Fine-tuned Qwen with therapist conversation data

**What we debugged:**

- Training taking 2 hours — reduced `max_length` from 512 to 256, increased batch size
- Wrong tokenizer loaded (`Qwen1.5-7B`) — fixed to use already loaded tokenizer
- `NameError: tokenizer not defined` — Drive not mounted, model not loaded this session
- Still at 50 minutes — confirmed this is acceptable, let it run

---

## Where You Are Now

```
Week 3 ✅ — Sarcasm classifier trained and saved to Drive
Week 4 ✅ — Qwen fine-tuned with LoRA, adapter saved
Week 5 ✅ — About to build integration pipeline + Gradio UI
Week 6 ✅ — Gradio UI (already scaffolded in every_session notebook)
Week 7 ✅ — Testing and evaluation
Week 8 ✅ — Documentation and presentation
```

---

## Key Decisions Made

- **3B not 7B** — fits comfortably on free Colab T4
- **Colab only** — dropped local Mac setup due to RAM limitations
- **LoRA not full fine-tuning** — 0.12% parameters, ~100MB adapter vs 6GB full model
- **DistilBERT not Qwen for classification** — right tool for the job
- **50k balanced not 500k or 1M** — faster training, same quality result
