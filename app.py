import openai
import time
from flask import Flask, request, render_template

app = Flask(__name__)
openai.api_key = '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'


@app.route('/',methods=['GET','POST'])
def ai():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        question = request.form['question']
        T1 = time.time()
         
        text = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{question}"}
            ]
        )
         
        T2 = time.time()
        t = (T2 - T1) * 1000
        return render_template('reply.html',reply=text['choices'][0]['message']['content'], t=t)

if __name__ == '__main__':
    app.run()
