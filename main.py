import os
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def generate_text(user_input: str) -> Markdown:
    response = model.generate_content(user_input)
    return to_markdown(response.text).data


def print_sample(user_input: str):
    result = generate_text(user_input)
    print(result)


if __name__ == '__main__':
    print_sample('Hello, how are you?')
