import cv2

def main():
    # Create video capture object
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera 

    # Create background subtractor
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        
        # Apply background subtraction
        fg_mask = bg_subtractor.apply(frame)

        # Find contours of moving objects
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # Draw rectangles around moving objects
        for contour in contours: 
            # check if the area of contour is greater than 400
            if cv2.contourArea(contour) > 400: 
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0))

        # Display the frame with moving object detection
        cv2.imshow("Abhinandan Singh | Moving Object Detector", frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()

    # Mac Kernal Crash Problem Resolved
    cv2.waitKey(1) # only for mac

if __name__ == "__main__":
    main()
