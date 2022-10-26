import openai
from flask import Flask, redirect, render_template, request, url_for
from os import getenv

app = Flask(__name__)
openai.organization = getenv("OPENAI_ORG")
openai.api_key = getenv("OPENAI_KEY")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        prompt = request.form.get("prompt")
        
        if prompt.strip() == "":
            return redirect(url_for("index"))
        
        loc = len([i for i in prompt if i == '\n']) + 1     # calculate Lines of Code
        description_factor = 35     # calculated from average LoC:Result ratio
        
        mtr = loc * description_factor
        
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=f"#Python 3\n{prompt}\n# Explanation of what the code does",
            temperature=0,
            max_tokens=mtr,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        answer = response["choices"][0]["text"].split("#Python 2")[0]
        print(answer)
        
        return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)