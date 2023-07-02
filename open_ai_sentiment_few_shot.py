import os
import openai

openai.api_key = "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"

messages = []

labeled_dataset = [{"text" : "I do not like this", "label": "negative"}, {"text": "I like this", "label": "positive"}]
# Chat GPT labeled examples
few_shot_message = ""
# Mention the Task
few_shot_message = "Task: Sentiment Classification \n"
# Mention the classes
few_shot_message += "Classes: positive, negative \n"
# Add context
few_shot_message += "Context: We want to classify sentiment of hotel reviews \n"
#Add labeled examples
few_shot_message += "Labeled Examples: \n"
for labeled_data in labeled_dataset:
    few_shot_message += "Text: " + labeled_data["text"] + "\n Label: " + labeled_data["label"] + "\n"

few_shot_message += "Now we will ask you the sentiment classification for a  few unlabeled examples. Please use labeled examples as context."

messages.append({"role": "user", "content": few_shot_message})
chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

unlabeled_dataset = ["I hate this", "I love this"]
for data in unlabeled_dataset:
    # Add the text to classfy
    message = "Text: " + data + ", "
    # Add the prompt
    message += "Prompt: Classify the given text into one of the following sentiment categories: positive, negative"
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})