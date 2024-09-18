import cv2 as cv

SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 5

def isContainFace(image):
    face_cascade = cv.CascadeClassifier('face_cascade.xml')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, SCALE_FACTOR, MIN_NEIGHBORS)
    return len(faces) > 0

def detectFace(image):
    face_cascade = cv.CascadeClassifier('face_cascade.xml')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, SCALE_FACTOR, MIN_NEIGHBORS)
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

if __name__ == '__main__':
    cam = cv.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if isContainFace(frame):
            frame = detectFace(frame)
        cv.imshow('image', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv.destroyAllWindows()