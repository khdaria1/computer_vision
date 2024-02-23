import cv2

# read webcam
print("read webcam...")
webcam = cv2.VideoCapture(0)    # device(0) : webcam

# visualize webcam
print("visualize webcam...")

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # if you want exit, press a 'q' key
        break

webcam.release()
cv2.destroyAllWindows()
