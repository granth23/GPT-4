from flask import Flask, render_template, request
import openai

app = Flask(__name__)

def gen_response(prompt):
    "DocString"

    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {'role': 'system', 'content': "You are an AI used by a university to generate questions for their exams. You strictly follow the prompts and do the tasks"},
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