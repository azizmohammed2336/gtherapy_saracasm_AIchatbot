## Empath-AI

# Authorship

- Name: Aziz Mohammed  
- Date: 2026-04-28  
- GitHub: <https://github.com/azizmohammed2336/gtherapy_saracasm_AIchatbot>

# Brief summary

This project implements an AI emotional-support chatbot composed of two models in a pipeline: a DistilBERT sarcasm classifier (detects sarcastic vs. genuine user input) and a LoRA-fine-tuned Qwen2.5-3B Instruct model (generates empathetic, therapist-style responses). The pipeline adapts Qwen’s prompt based on the sarcasm classifier output and exposes a Gradio chat interface. Models and artifacts are stored on Google Drive and the project runs end-to-end on Google Colab (T4 GPU).

# Folder and file structure

```
├── ai_assistance.md
├── docs
│   ├── classifierEvaulation.md
│   ├── justifications.md
│   ├── loRAevaluation.md
│   ├── results.md
│   └── WORK_NOTES.md
├── finalClassifier
│   ├── config.json
│   ├── model.safetensors
│   ├── requirement.txt
│   ├── tokenizer_config.json
│   ├── tokenizer.json
│   └── training_args.bin
├── LoRAfinal
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   ├── chat_template.jinja
│   ├── tokenizer_config.json
│   └── tokenizer.json
├── README.md
├── sprints
│   ├── projectS1.md
│   ├── projectS1.pdf
│   ├── projectS2.md
│   ├── projectS2.pdf
│   └── projectS3.md
└── src
    ├── FinalPipelineBuilding.ipynb
    ├── LoRAtraining.ipynb
    ├── SarcasmClassifyer.ipynb
    └── SetUp.ipynb
```

# Installation (prerequisites and setup)

Prerequisites

- macOS or Linux, Python 3.9+ (Colab uses system Python)
- Git, git-lfs (for large model files)
- Google account with Google Drive for model storage
- Hugging Face account and token (HF_TOKEN)

Local setup (optional)

1. Clone repo:
   git clone <https://github.com/azizmohammed2336/gtherapy_saracasm_AIchatbot.git>
2. Install and enable Git LFS:
   brew install git-lfs
   git lfs install

Colab (recommended)

- Open the provided Colab notebooks (or run the project scripts) and enable a GPU (T4).

# Datasets

- mpingale/mental-health-chat-dataset  
  - Purpose: fine-tune Qwen2.5-3B with therapist-patient dialogs (LoRA).  
  - Size: used 2,775 examples for LoRA experiments (adapter saved separately).  
  - Source: Hugging Face dataset (not stored in repo due to size).

- daniel2588/sarcasm  
  - Purpose: train DistilBERT sarcasm classifier.  
  - Source size: ~1,010,826 rows; project samples 50,000 (25k sarcastic / 25k non-sarcastic).  
  - Storage: dataset is pulled dynamically from Hugging Face; not included in repo.

# Configuration (keys.env)

Create a keys.env file at project root (do NOT commit it). Example:
HF_TOKEN=hf_xxxYOUR_HF_TOKENxxx
DRIVE_MOUNT_PATH=/content/drive/MyDrive/gtherapy_models
OPTIONAL_API_KEY=...

Usage


- Colab: set environment variables with os.environ or use Colab secrets + mount Drive

# Deployment (Google Colab with GPU)

1. Open the project Colab notebook.
2. Runtime → Change runtime type → GPU (T4 recommended).
3. Mount Google Drive:
   from google.colab import drive
   drive.mount('/content/drive')
4. Ensure keys.env variables are set in the runtime environment (or export HF_TOKEN).
5. Install requirements in the Colab cell:
   !pip install -r /content/path/to/requirements.txt
6. Run training / inference cells. Trained artifacts should be saved to the Drive mount path.

Notes

- Large model files (>100MB) must be stored in Drive or tracked via Git LFS. For sharing, push LFS pointers and run `git lfs push --all <remote>`.

# How to run and what to expect

Quick run (Colab recommended)

1. Mount Drive and set HF_TOKEN.
2. Run the sarcasm classifier notebook or:
   python src/sarcasm_classifier.py
   - This script loads the `daniel2588/sarcasm` dataset (sampled), trains DistilBERT, evaluates, and saves the classifier to Drive.
3. Load the LoRA adapter for Qwen2.5-3B in Colab (see LoRAfinal instructions) and point the Gradio interface to the saved models.
4. Launch Gradio in Colab to obtain a public shareable URL.

Expectations

- DistilBERT classifier: ~73% accuracy (project results).
- Qwen2.5-3B with LoRA: small adapter (0.12% parameters trained) to steer responses toward therapeutic style.
- Gradio chat UI: real-time responses, sarcasm-aware prompts.

# License

This project is provided under the MIT License.
