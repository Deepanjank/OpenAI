import os
import openai

openai.api_key = "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"

# GPT-3
# response = openai.Completion.create(
#     model = "text-davinci-003",
#     prompt="Write an essay:\n\n Hindi is an important language.",
#     temperature=0,
#     max_tokens=1000,
#     top_p=1.0,
#     frequency_penalty=0.0,
#     presence_penalty=0.0
# )

# print(response)

# Chat GPT
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})