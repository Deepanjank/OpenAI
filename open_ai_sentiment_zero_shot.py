import os
import openai

openai.api_key = "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"


# print(response)

# Chat GPT
dataset = ["I hate this", "I love this"]
for data in dataset:
    # Mention the Task
    message = "Task: Sentiment Classification, "
    # Mention the classes
    message += "Classes: positive, negative, "
    # Add context
    message += "Context: We want to classify sentiment of hotel reviews, "
    # Add the text to classfy
    message += "Text: " + data + ", "
    # Add the prompt
    message += "Prompt: Classify the given text into one of the following sentiment categories: positive, negative"
    print(message)
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}]
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")