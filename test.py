import cv2

# Load the trained cascade
cascade = cv2.CascadeClassifier('DIP/classifier/cascade.xml')

# Read an image to test the cascade on
image = cv2.imread("C:/Users/Sarvar/Desktop/Saved Pictures/_OSO0021.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the cascade to detect objects
objects = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,     # Start with 1.1 and adjust slightly up/down if needed
    minNeighbors=7,      # Experiment between 3–6
    minSize=(400, 400)     # Adjust based on expected face size   
)

# Draw bounding boxes around detected objects
for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the result
cv2.imshow('Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
