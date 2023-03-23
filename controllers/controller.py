from flask import request
from models.preprocessing import toBase64, preprocessing
from models.classification import predict
from views.view import indexView, uploadView

def index():
    return indexView()


def upload():
    file = request.files['file'].read()
    encoded_string = toBase64(file)
    img_array = preprocessing(file)
    classname, score = predict(img_array)
    
    return uploadView(encoded_string, classname, score)