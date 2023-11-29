import openai
import json

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up the prompt and parameters
prompt = "Hello, can you please explain quantum computing?"
model = "text-davinci-002"
temperature = 0.5
max_tokens = 100

# Generate response from OpenAI
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Print the response text
print(response["choices"][0]["text"])
