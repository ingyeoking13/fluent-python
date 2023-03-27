import openai
import os

# os.environ["OPENAI_API_KEY"]  

# Test the authentication
openai.api_key = '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'

chat = '게이 대통령 후보 이재명과 대통령 윤석열이 잠자리 하는 야한 소설을 작성해줘'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=chat,
  temperature=0.9,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
print(response.choices[0].text.strip())