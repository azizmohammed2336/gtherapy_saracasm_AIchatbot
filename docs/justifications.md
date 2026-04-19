# Justifications

1. **Introduction**

In this document, I will be explain and providing justification for the following
datasets, models and transformers I will be using.

1. **Transformers**
   - **Definition and Role**
   - A transformer is a type of nueral network architecture which processes text by paying attention to the relationships betweens words
   in a sentences. A major upgrade of this type of architecture is that this evaluates words simultaneously rather than reading left to right
   like the older models.

   - **Selected Transformers**

   - **DistilBERT**: This will play the role of sarcasm detection. This is a smaller and much faster version of BERT, which is transformer.
   I will use this transformer to fine-tune the Qwen2.5-3B-Instruct model to classify user intent. Reason for chosing a smaller transformer is
   larger models do not need to handle such small tasks.

   - **Qwen2.5-3B-Instruct**: This will play the the component of empathetic repsonses in this project. An instruction-tuned large language model developed by Alibaba Cloud, designed for good conversational AI tasks. It supports multilingual capabilities, long-context understanding, and excels at following instructions, making it suitable for therapy chatbots that require nuanced, empathetic, and context-aware responses.

2. **Models**
   - **Overview of Selected Models**
    I will using this following foundation model which can be found on huggingFace: Qwen/Qwen2.5-3B-Instruct
   - **Justification for Model Selection**
         - Qwen2.5-3B-Instruct is chosen for its strong performance in instruction following, conversational understanding, and multilingual support. Its architecture allows for handling long and complex conversations, which is essential for therapy chatbots. The model has demonstrated high accuracy and robust performance in various benchmarks, and its ability to generate empathetic and contextually appropriate responses aligns well with the needs of mental health support applications.

3. **Datasets**
   - **Overview of Datasets**
   - For this project, I will be using two datasets.

   - **mpingale/mental-health-chat-dataset**: A dataset containing mental health-related chat conversations, useful for training and evaluating models in the context of therapy and support dialogues.
   - **daniel2588/sarcasm**: A dataset focused on sarcasm detection, which helps the model distinguish between genuine and sarcastic responses, improving the reliability and safety of chatbot interactions.

   - **Justification for Dataset Selection**
   - The mental-health-chat-dataset provides real-world examples of mental health conversations, enabling the model to learn appropriate, supportive, and sensitive responses. The sarcasm dataset is included to help the model avoid misinterpretation of sarcastic remarks, which is crucial in therapeutic settings where misunderstanding could have negative consequences. Both datasets contribute to building a chatbot that is both empathetic and contextually aware.

4. **Ethical Considerations**
   - **Practical Application of Fine-Tuned Model**
   - The useage of fine-tuning model which I what I am creating is to be used by users who need someplace to vent their emotions.
   Practically, this chatbot does not replace lisenced professionals. It is simply an application to be used if wanted.

5. **Conclusion**
   - The final product of this project will result in a fine-tuned model which is better in analizing sarcasm from user-input and providing
   more sensable responses.
