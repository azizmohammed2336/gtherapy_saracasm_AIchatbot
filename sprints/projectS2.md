## Sprint April 21, 2026 - Update

What project work have you achieved since last class last week?

- This week was my strongest week in the project. I was able to finetune the sarcasm classifier and get it to run with an accuracy of 73% and an F1 score of 0.73. Moreover, I was able to finetune the Qwen2.5-3B model using LoRA on the mental health counseling dataset, which produced a small adapter that steers the model toward compassionate, therapist-style responses.

What challenges, setbacks, "blockers" have you encountered?

- The main challenge was the training time for both models. The sarcasm classifier took a long time to train (30 minutes), and I had to reduce the dataset size to make it feasible. For the Qwen model, the training was also  verytime-consuming, and I had to adjust the `max_length` and batch size to speed it up (1 hour). The Qwen model took the most amount of time since I was fine-tuning a much larger model, even with LoRA, at it's peak, the esimtated time to run the model was 3 hours which is not feasible for me, so I had to make adjustments to make it run in a reasonable time frame.

What is your actionable and feasible plan for this week sprint?

- This week, I plan to build the integration pipeline that connects the sarcasm classifier and the fine-tuned Qwen model. I will also start working on the Gradio UI to deploy the complete pipeline as an interactive chat interface.

How much time are you allocated for this sprint? When? What's a concrete schedule?

- For this sprint, I allocated 5 hours. I plan to spend the first 3 hours building the integration pipeline and the next 2 hours working on the Gradio UI.

What specific activities/tasks you'll do in the allocated time?

- Build the integration pipeline to connect the sarcasm classifier and the fine-tuned Qwen model.

What tangible work products in your project folder will evidence your work?

- The integration pipeline code and the Gradio UI code will be added to the project folder, along with any necessary documentation. Then, when I deploy the Gradio interface, I will also include a link to the live demo in the project folder.

How much are done?

- I think I am about 70% done with the project.
