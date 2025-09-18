import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cap = cv2.CascadeClassifier("C:/Users/shrey/myprojects/.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
 
# To capture video from webcam (0)
video_cap = cv2.VideoCapture(0)

# Start video capture
while True:
    ret , video_data = video_cap.read()
    if not ret:     
        print("Failed to capture video. Exiting...")
        break

    # convert to grey scale 
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),    
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangle around the faces 
    for(x,y,h,w) in faces :
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)     # make square brackets

    # display the resulting frame
    cv2.imshow("video_live",video_data)

    # Press "a" on keyboard to exit the video
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()

# Destroy all the windows
cv2.destroyAllWindows()