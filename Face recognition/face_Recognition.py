import face_recognition
import cv2 as cv2
import numpy as np
from datetime import datetime


video_capture = cv2.VideoCapture(0)

imgMark = face_recognition.load_image_file(r'C:\Users\Acer\Desktop\Project Sivaji\Face recognition\Database\Mark\mark.jpg')
imgMark_encoding = face_recognition.face_encodings(imgMark)[0]

imgSatiya = face_recognition.load_image_file(r'C:\Users\Acer\Desktop\Project Sivaji\Face recognition\Database\Satiyaganes\iMSatiya.jpg')
imgSatiya_encoding = face_recognition.face_encodings(imgSatiya)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [imgMark_encoding, imgSatiya_encoding,]
known_face_names = ["Mark","Satiya"]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

i=0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_list = []
        face_names = []
        
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                face_names.append(name)
    
    i+=1
    if i==5:
        curr_name = name
        print(curr_name)
        speak(curr_name)

    if len(face_names)==0:
        i=0
            
    process_this_frame = not process_this_frame




    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255),1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()