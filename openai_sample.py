import os
import openai

def view_env():
    print(os.getenv('OPENAI_API_KEY'))

def call_api():
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role":"system", "context": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role":"user", "context": "hello! i am atsushi."}
        ]
    )

if __name__ == '__main__':
    # view_env()
    call_api()