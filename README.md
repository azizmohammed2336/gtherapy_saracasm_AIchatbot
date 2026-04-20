# gtherapy_saracasm_AIchatbot

AI therapy chatbot project for COMP741 (Practical AI), focused on empathetic conversation and sarcasm-aware response generation.

## Owner

- Name: Aziz Mohammed
- Role: Project Owner and Developer

## Development Information

- Primary Language: Python
- Core Frameworks/Libraries: PyTorch, Hugging Face Transformers, scikit-learn, Pandas
- Development Platform: Google Colab
- Compute: Cloud GPU/T4 via Google Colab
- Project Type: NLP + Transformer fine-tuning + Text classification

## Project Overview

The system is an AI-powered mental health support assistant that analyzes user input and provides supportive, empathetic responses. It learns response patterns from therapist-style dialogue datasets and uses sarcasm detection to better interpret indirect emotional expression. The goal is not to replace licensed therapists, but to serve as a supportive conversational tool that helps users reflect on their emotions.

## AI Concepts and Techniques

1. **Natural Language Processing (NLP)**: Process and interpret user text input.
2. **Transformer-based language models**: Fine-tune pretrained models on therapist-style conversations.
3. **Text classification**: Classify whether user input contains sarcasm.
4. **Fine-tuning pretrained models**: Adapt existing models instead of training from scratch.
5. **Prompt engineering and response generation**: Produce empathetic and supportive responses.

## Datasets

- Therapeutic conversation dataset for empathetic response training
- Sarcasm detection dataset for sarcasm classification

## Risks and Ethical Considerations

1. **Safety and Security**: The system may produce misleading advice if poorly designed. To reduce risk, it will provide general emotional support only (not medical advice) and may suggest professional help for serious distress.
2. **Data Privacy and Algorithmic Bias**: No personally identifiable information (PII) will be stored during testing. Datasets will be reviewed for harmful or biased patterns.
3. **Transparency**: Users will be clearly informed they are interacting with an AI support assistant, not a human therapist.
4. **Explanation**: Documentation will explain how the model works, which datasets are used, and the system’s limitations.
