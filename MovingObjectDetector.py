import cv2

# Create video capture object
video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera 

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow("Video", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()

# Mac Kernal Crash Problem Resolved
cv2.waitKey(1) # only for mac
