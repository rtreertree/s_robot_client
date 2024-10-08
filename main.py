import cv2 as cv
import datetime as dt
import compress
import facedetection as fd
from time import sleep
import requests

url = 'http://rtreertree.com:3000/image'

def send_image(image: bytes):
    response = requests.post(url, files={'image': image}, data={'name': 'image'})
    return response.text

cam = cv.VideoCapture(0)

last = dt.datetime.now()
while True:
    ret, frame = cam.read()

    if not ret:
        continue
    
    frame = cv.resize(frame, (640, 480))
    if fd.isContainFace(frame) and (dt.datetime.now() - last).seconds > 5:
        frame = fd.detectFace(frame)
    else:
        continue

    imgBuffer = compress.compress_image(frame, quality=60)
    image = imgBuffer.read()
    res = send_image(image)
    last = dt.datetime.now()
    sleep(1/20)
