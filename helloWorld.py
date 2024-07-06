# set OPENAI_API_KEY=sk-proj-xxxxxxlLz4
# export OPENAI_API_KEY=sk-proj-xxxxxlLz4
# get your key from https://platform.openai.com/api-keys


import os
import asyncio
from  openai import OpenAI


client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user",
               "content": "give 10 examples of fruit. short answer only"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")