Project: AI Emotional Support Chatbot

This project builds an AI-powered mental health support assistant using two fine-tuned transformer models working together in a pipeline.

Component 1 — Sarcasm Detection (DistilBERT):

A DistilBERT model was fine-tuned on 50,000 balanced Reddit comments from the daniel2588/sarcasm dataset to classify whether user input is sarcastic or genuine. The model achieved 73% accuracy and 0.73 F1 score. Sarcasm detection is necessary because users in emotional distress often express feelings indirectly or sarcastically, and a support assistant must recognize this to respond appropriately rather than taking statements at face value.

Component 2 — Empathetic Response Generation (Qwen2.5-3B):

The Qwen2.5-3B-Instruct model was fine-tuned using LoRA on 2,350 therapist-patient conversations from the mpingale/mental-health-chat-dataset. Only 0.12% of the model's parameters were trained, producing a small adapter that steers the model toward compassionate, therapist-style responses. The base model's general language understanding is preserved while its conversational style is adapted for mental health support.

Component 3 — Integration Pipeline (Week 5):

The two models are connected through a logic layer. When a user submits input, the sarcasm classifier runs first. If sarcasm is detected, the system prompt passed to Qwen is adjusted to acknowledge the user's indirect expression of emotion. If no sarcasm is detected, the prompt instructs Qwen to respond as a supportive therapist. This produces contextually appropriate responses regardless of how the user expresses themselves.

Final Output — Gradio Chat Interface:

The complete pipeline is deployed as an interactive chat interface using Gradio, accessible via a public URL generated during the Colab session. Users can type messages and receive empathetic responses in real time, with the sarcasm detection running invisibly in the background to shape each response.
