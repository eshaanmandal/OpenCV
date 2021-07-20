import cv2 as cv

video = cv.VideoCapture("Videos/BadApple.mp4")

while True:
    isframe, frame = video.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()


