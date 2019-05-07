import sys

import cv2

try:
    image_path = sys.argv[1]
    casc_path = sys.argv[2]
except IndexError as e:
    image_path = "/Users/owenbrown/cockpit.jpg"
    casc_path = None

# Creat teh haar cascade
face_cascade = cv2.CascadeClassifier(image_path)

# Read the image
image = cv2.imread(image_path)
gray = cv2.cvtColor(cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("Faces found", image)
cv2.waitKey(0)