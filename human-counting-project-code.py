import cv2
import imutils
import numpy as np
import argparse

# Load Haar cascade once globally for efficiency
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    face_num = 1
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'Face {face_num}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        face_num += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Faces : {face_num - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    # cv2.imshow('output', frame)

    return frame

def detectByPathImage(path, output_path):
    image = cv2.imread(path)
    if image is None:
        print(f"[ERROR] Could not read image from {path}")
        return

    image = imutils.resize(image, width=min(800, image.shape[1]))
    result_image = detect(image)

    if output_path is not None:
        cv2.imwrite(output_path, result_image)

def humanDetector(args):
    image_path = args["image"]

    if image_path is not None:
        print('[INFO] Opening Image from path.')
        detectByPathImage(image_path, args['output'])
    else:
        print("[ERROR] No input source specified. Use --image, --video or --camera")

def argsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", default=None, help="path to Video File ")
    parser.add_argument("-i", "--image", default=None, help="path to Image File ")
    parser.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    parser.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    args = argsParser()
    humanDetector(args)
