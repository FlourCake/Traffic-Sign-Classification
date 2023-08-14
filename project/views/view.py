from flask import render_template
import os

datadir = os.path.join(os.path.dirname(__file__), '../data')

def getModelList():
    modelList = []
    for model in os.listdir(os.path.join(datadir, 'model')):
        if model.endswith('.h5'):
            modelList.append(model.split('.')[0])

    return modelList

def indexView(error_msg=False):
    return render_template('index.html', error=error_msg)

def uploadView(data):
    batch = True

    if 'classname' in data:
        batch = False
        
    return render_template('index.html', batch=batch, data=data)