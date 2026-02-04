import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_visual_prompt(sentence, style):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Convert sentence into a vivid visual scene description"},
            {"role": "user", "content": f"{style} scene: {sentence}"}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content
