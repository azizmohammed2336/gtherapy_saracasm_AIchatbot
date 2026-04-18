# Justifications

1. **Introduction**

In this document, I will be explain and providing justification for the following
datasets, models and transformers I will be using.

2. **Transformers**
   - **Definition and Role**

   - **Selected Transformers**

   - **Qwen2.5-7B-Instruct**: An instruction-tuned large language model developed by Alibaba Cloud, designed for advanced conversational AI tasks. It supports multilingual capabilities, long-context understanding, and excels at following instructions, making it suitable for therapy chatbots that require nuanced, empathetic, and context-aware responses.

3. **Models**
   - **Overview of Selected Models**
    I will using this following foundation model which can be found on huggingFace: Qwen/Qwen2.5-7B-Instruct
   - **Justification for Model Selection**
         - Qwen2.5-7B-Instruct is chosen for its strong performance in instruction following, conversational understanding, and multilingual support. Its architecture allows for handling long and complex conversations, which is essential for therapy chatbots. The model has demonstrated high accuracy and robust performance in various benchmarks, and its ability to generate empathetic and contextually appropriate responses aligns well with the needs of mental health support applications.

4. **Datasets**
   - **Overview of Datasets**

   - **mpingale/mental-health-chat-dataset**: A dataset containing mental health-related chat conversations, useful for training and evaluating models in the context of therapy and support dialogues.
   - **daniel2588/sarcasm**: A dataset focused on sarcasm detection, which helps the model distinguish between genuine and sarcastic responses, improving the reliability and safety of chatbot interactions.

   - **Justification for Dataset Selection**
   - The mental-health-chat-dataset provides real-world examples of mental health conversations, enabling the model to learn appropriate, supportive, and sensitive responses. The sarcasm dataset is included to help the model avoid misinterpretation of sarcastic remarks, which is crucial in therapeutic settings where misunderstanding could have negative consequences. Both datasets contribute to building a chatbot that is both empathetic and contextually aware.

5. **Ethical Considerations**
   - 

6. **Conclusion**
   - 