import cv2

camera_url = "http://192.168.0.104:8080/video"
cap = cv2.VideoCapture(camera_url)

while True:
    ret, frame = cap.read()
    print(frame)
    cv2.imshow('IP Camera Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
