import PIL
from django.utils import timezone

import numpy as np
import urllib
from keras.models import model_from_json
import logging
from background_task import background
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import requests
from io import BytesIO

from parking_project.camera.models import Camera

RED = (245, 10, 10)
GREEN = (0, 255, 0)
NN_INPUT_SIZE = (64, 64)


def return_frame_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def load_model():
    # load json and create model
    json_file = open('parking_project/parking_space_detector/neural_network/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    predictor = model_from_json(loaded_model_json)
    # load weights into new model
    predictor.load_weights("parking_project/parking_space_detector/neural_network/model.h5")
    return predictor


def refresh_frames():
    logging.info("Refreshing frames")
    neural_network_predictor = load_model()
    for camera in Camera.objects.all():
        image = return_frame_from_url(camera.url)
        for camera_parking_spot in camera.parking.parking_spaces.all():
            try:
                # crop the image
                rect_img = image.crop((camera_parking_spot.upper_right_x, camera_parking_spot.upper_right_y,
                                       camera_parking_spot.bottom_left_x, camera_parking_spot.bottom_left_y))

                # resize to the accepted input of the neural network NN_INPUT_SIZE
                resized_image = rect_img.resize(NN_INPUT_SIZE, PIL.Image.ANTIALIAS)

                # make prediction
                camera_parking_spot.is_occupied = neural_network_predictor.predict(np.array(resized_image).reshape(1, 64, 64, 3))[0][0] == 1
                camera_parking_spot.save()

                # add coloured rectangle
                upper_left = (camera_parking_spot.upper_right_x, camera_parking_spot.upper_right_y)
                bottom_right = (camera_parking_spot.bottom_left_x, camera_parking_spot.bottom_left_y)

                draw = ImageDraw.Draw(image)
                if camera_parking_spot.is_occupied:
                    draw.rectangle((upper_left, bottom_right), outline=RED)
                    draw.text(upper_left, camera_parking_spot.code, fill=RED)
                else:
                    draw.rectangle((upper_left, bottom_right), outline=GREEN)
                    draw.text(upper_left, camera_parking_spot.code, fill=GREEN)
            except:
                pass
        image.save('static/parking{}.png'.format(camera.parking.id))


