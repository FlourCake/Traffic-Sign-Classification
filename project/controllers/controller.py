import base64
from flask import request, redirect
from project.models.preprocessing import Preprocessing
from project.models.classification import Classification
from project.views.view import indexView, uploadView

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def index():
    return indexView()


def upload():
    if 'file' not in request.files:
        return indexView(error_msg='No File Chosen, Please upload file')
    
    file = request.files['file']
    filename = file.filename

    if not (filename.rsplit('.', 1)[1].lower() in {'txt', 'png', 'jpg', 'jpeg'}):
        return indexView(error_msg='Wrong file extention!\nAllowed Extentions: txt, png, jpg, jpeg')

    preprocessing = Preprocessing()
    classification = Classification()

    if filename.endswith('.txt'):
        file = file.read().decode('utf8')
        test_generator, nb_samples, labels = preprocessing.data_generator(file)
        cr = classification.predict_batch(test_generator, nb_samples, labels)

        return uploadView(cr)
    else:
        file = file.read()
        img = preprocessing.image_enhancement(file)
        prediction = classification.predict(img)
        prediction['image'] = base64.b64encode(file)

        return uploadView(prediction)