
<h1 align="center">Traffic Sign Classification with CNN</h1>

<p align="center">
  <img src=".\project\static\image\headline.png">
</p>

---

<p align="center">💡A web app that performs the classification of traffic sign images with CNN.</p>

## Table of Contents
* [General Info](#general-information)
* [Installation](#installation)
* [Contributing](#contributing)
* [Contact](#contact)

## General Info
This web app performs the classification of traffic sign images. App built using Flask framework  with mvc structure based on [Flask Simple MVC](https://github.com/indhifarhandika/flask-mvc) and some improvement. The models used are created through [Traffic Sign Classification Notebook](https://github.com/FlourCake/Traffic-Sign-Classification-Notebook). See live demo [here](http://pakhaji.pythonanywhere.com/).

## Installation
* Clone this repo
```bash
git clone https://github.com/FlourCake/Traffic-Sign-Classification.git
```
* Go to project directory
```bash
cd Traffic-Sign-Classification
```
* Install dependencies
```bash
pip i -r requirements.txt
```
* Run `server.py` with python
```bash
python server.py
```
* Copy url and open on your browser, e.g.`localhost:5000`

__Note:__
* make sure you have added the model to `data` folder.
* If you want to use your own model, you can add your trained model to `data` folder.
* Change the model path and model name in `project/models/classification.py` to match your model.
* A .txt upload is used for batch testing. With a file containing the test data path

## Room for Improvement
Room for improvement:
- Need loading bar for classification.
- Interface is too simple (No user guide).

To do for future development:
- Create trafic sign detection model to improve performance.
- Create app for real-time detection and classification

## Contributing
Pull requests are welcome! If you see something you'd like to add, please do. For drastic changes, please open an issue first.

## Contact
Created by [Nolep Dev](mailto:support@nolep.web.id) - Feel free to contact us.

Copyright 2023 - Nolep Dev