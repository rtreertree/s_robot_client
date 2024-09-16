from PIL import Image
from io import BytesIO
import cv2 as cv
import numpy as np
import datetime as dt

def compress_image(img, quality=20):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    image =  Image.fromarray(img)

    # Create an in-memory buffer
    image_buffer = BytesIO()

    # Save the image to the buffer with reduced quality
    image.save(image_buffer, format='JPEG', quality=quality, optimize=True)

    # Reset buffer position
    image_buffer.seek(0)

    return image_buffer

def decompress_image(image_buffer):
    # Open the image from the buffer
    image = Image.open(image_buffer)

    # Convert the image to a numpy array
    image_array = np.array(image)

    return image_array

if __name__ == '__main__':
    date = dt.datetime.now()
    cam = cv.VideoCapture(0)


    ret, frame = cam.read()
    buff = compress_image(frame, quality=10)

    while True:
        ret, frame = cam.read()

        height, width, _ = frame.shape
        # resize the frame
        frame = cv.resize(frame, (width // 2, height // 2))

        buffer = compress_image(frame, quality=30)
        img = decompress_image(buffer)


        cv.putText(img, "FPS : " + str(1 / ((dt.datetime.now() - date).microseconds / 1000000)), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
        cv.putText(img, "Size (KB) : " + str(buffer.getbuffer().nbytes / 1000), (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

        cv.imshow('image', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        date = dt.datetime.now()
