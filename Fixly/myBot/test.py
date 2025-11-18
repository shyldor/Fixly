from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about programmers",
  store=True,
)

print(response.output_text);



{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {
  "model": "gpt-3.5-turbo-0125", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
