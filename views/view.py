from flask import render_template

def indexView():
    return render_template('index.html')

def uploadView(encoded_string, result, score):
    return render_template('index.html', filename=encoded_string, classname=result, score=score)