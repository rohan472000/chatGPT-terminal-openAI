# 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

import openai

openai.api_key = "OpenAI-API-key"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


while True:
    prompt = input("You: ")
    response = generate_response(prompt)
    print("Terminal_bot: ", response)
