**April 21-28**:

This week, I have worked on the Final pipline building. This allowed for both the classifier and the model to be integrated effectively.
For this, I used Colab as the platform for the code. Moreover, I deployed the code using Gradio. This allowed for more focus on the
integration and logic rather than the user-experince. However, that is something I will be looking to do in the future, which
would to increase and better design the user-interface. 

One thing I noticed is that the user-interface could be more intuitive and provide better feedback to the user. Morever, the
model only works when I am running and connected to Colab, this is hindering the deployed of this system since I would want other users
to be able to use it whenever.

**April 14-21**:

I have worked on the project, and have replaced the model since I realized that
my computer was not able to handle it. Also, I moved my project completely to the cloud.
Seeing how colab is able to handle the model and accuratly run it is much better.

I made the sarcasmclassifier from DistillBERT which will act as the detection for seeing how to classify the sentences of sarcasm. While this dataset was 1M points long, I only used 50K with each set being from 0 to 1. 0 being non-sarcastic while 1 being sarcastic. This way, I got to work with 25k points random points from each data-subset. In an ideal world, I would have loved to use 1M datapoints, but Colab would time out, and that would take hours, if not 2-3 days just to run.

Moreover, I finetuned the Qwen model with LoRA. 
- AI Definition of what I did: LoRA (Low-Rank Adaptation) is a fine-tuning technique that freezes the original model's 3 billion parameters and injects small trainable matrices into specific layers. Instead of retraining the entire model, only 3.6 million parameters (0.12%) are trained, producing a lightweight adapter file (~100MB) that modifies the model's behavior without replacing it. When loaded alongside the base model, the adapter steers responses toward therapist-style empathetic dialogue learned from the mental health counseling dataset.

**April 7**:

- Deleted LLAMA Model - this model is a gated model which I do not have access to.
- Successfully loaded in datasets.

To-do:

- Redo justifications for the following datasets.

**March 24**:

- Initiated the Github and decided on datasets/models
- Need to start working on justifications
