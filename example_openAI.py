import openai

client = openai.OpenAI(
  api_key="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"
)

prompt = "What is the capital of India?"

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
