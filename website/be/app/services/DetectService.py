from app.extensions import model
from keras.models import load_model
from flask import Flask, render_template, request, jsonify, abort
from tensorflow.keras.preprocessing.image import img_to_array,load_img
import numpy as np
import json
from PIL import Image
import io
import os
import cv2
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}
def is_skin(img):
    #converting from gbr to hsv color space
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #skin color range for hsv color space 
    HSV_mask = cv2.inRange(img_HSV, (0, 5, 0), (17,170,255)) 
    HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #converting from gbr to YCbCr color space
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    #skin color range for hsv color space 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))


    #merge skin detection (YCbCr and hsv)
    global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
    global_mask=cv2.medianBlur(global_mask,3)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))
    # count the number of skin color pixels
    skin_pixels = np.sum(global_mask > 0)
    # calculate the percentage of skin color pixels in the image
    skin_percent = skin_pixels / (img.shape[0] * img.shape[1]) 
    # return True if skin percentage is above a threshold, else False
    print(skin_percent)
    return skin_percent > 0.5
class DetectService:
    def Detect(image):
        class_names = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'VASC', 'acne', 'eczema', 'not_infected']
        if not allowed_file(image.filename):
            return abort(400, 'Only image files are allowed')
        image = Image.open(image)
        if not is_skin(np.array(image)):
            return jsonify({'error': 'No skin detected'})
        # Preprocess the image
        image = image.resize((300,300))
        # convert rgb color
        image = image.convert('RGB')
        img_array = img_to_array(image)
        image = img_array / 255.0
        image = np.expand_dims(image, axis=0)
        result = model.predict(image)
        result = dict(zip(class_names, result[0].tolist()))
        return jsonify(result)