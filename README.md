# Face Detection Project

This is a simple Python project that detects faces in images using OpenCV's Haar Cascade classifier. The program reads an input image, detects faces, draws bounding boxes around detected faces, and saves the resulting image with annotations.

---

## Features

- Detects faces in a static image
- Draws rectangles and labels on detected faces
- Outputs the annotated image to a specified file path
- Easy to run from the command line

---

## Requirements

- Python 3.6+
- OpenCV (`opencv-python`)
- imutils
- numpy

Install dependencies with:

```bash
pip install opencv-python imutils numpy
```
---
## Usage
Run the script from the command line with the following arguments:
```bash
python human-counting-project-code.py --image <input_image_path> --output <output_image_path>
```
Example
```bash
python human-counting-project-code.py --image C:/Users/Admin/Desktop/image.jpg --output C:/Users/Admin/Desktop/output.jpg
```
