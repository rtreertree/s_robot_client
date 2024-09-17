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
sleep(2)
last = dt.datetime.now()
_, frame = cam.read()
imgBuffer = compress.compress_image(frame, quality=70)
image = imgBuffer.read()
res = send_image(image)

# cam = cv.VideoCapture(0)

# last = dt.datetime.now()
# while True:
#     ret, frame = cam.read()

#     if not ret:
#         continue
    
#     frame = cv.resize(frame, (640, 480))
#     if fd.isContainFace(frame) and (dt.datetime.now() - last).seconds > 1 / 20:
#         frame = fd.detectFace(frame)
#     else:
#         continue

#     imgBuffer = compress.compress_image(frame)
#     image = imgBuffer.read()
#     res = send_image(image)
#     last = dt.datetime.now()
#     sleep(1/20)
