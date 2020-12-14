from flask import Flask, request, render_template
import NaiveBayes

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if 'text' in request.form:
        text = request.form['text']
        rating = NaiveBayes.predict(text)

        if len(rating) == 0:
            noval = "OOPS!!! no results found for your search query"
            return noval

    return render_template('result.html', name=rating)



if __name__ == '__main__': 
   app.run(host='0.0.0.0',port='80')