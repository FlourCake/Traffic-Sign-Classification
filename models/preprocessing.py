import io
import base64
import numpy as np
from PIL import Image
from PIL import ImageFilter

def preprocessing(file):
    image = Image.open(io.BytesIO(file))
    resize_image = image.resize((75, 75))
    enchanced_image = resize_image.filter(ImageFilter.SHARPEN).filter(ImageFilter.EDGE_ENHANCE)
    # enchanced_image = enchanced_image.convert('L').convert('RGB')
    img_array = np.array(enchanced_image)/255
    img_array = np.expand_dims(img_array, 0)

    return img_array

def toBase64(file):
    encoded_string = base64.b64encode(file)
    return encoded_string