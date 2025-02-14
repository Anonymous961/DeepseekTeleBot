from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_ENDPOINT = os.getenv("DEEPSEEK_API_ENDPOINT")

client = OpenAI(
    base_url=API_ENDPOINT,
    api_key=API_KEY,
)


def get_answer(question):
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

