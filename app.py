from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

def gen_response(prompt):
    "DocString"

    openai.api_key = os.environ.get('OPENAI_API_KEY')

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {'role': 'system', 'content': "You are an AI assistant that helps people with their work."},
            {'role': 'user', 'content': prompt}
        ]
    )
    response=completion["choices"][0]['message']["content"]

    return response


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        content = request.form.get('content')

        content = gen_response(content)

        return render_template('home.html', result = content)
    return render_template('home.html', result = "")

if __name__ == '__main__':
    app.run(debug=True)