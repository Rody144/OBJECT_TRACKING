import streamlit as st
import cv2
import numpy as np
import tempfile
import time


def ConvertColor(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


# App title and description
st.set_page_config(page_title="Object Tracking App", layout="wide",page_icon="🎥",initial_sidebar_state="expanded")
st.title("🎥Video Object Tracking Application")
st.markdown("## Upload a video file to track objects in it.")
uploaded_file = st.file_uploader("Please upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    tfile.close()

    capturtes = cv2.VideoCapture(tfile.name)

    if not capturtes.isOpened():
        st.error("Video file cannot be opened")
    else:
        stframe = st.empty()  # Placeholder for video
        back_sub = cv2.createBackgroundSubtractorMOG2()  # Background subtractor

        while capturtes.isOpened():
            ret, frame = capturtes.read()
            if not ret:
                break

            fg_mask = back_sub.apply(frame)  # Apply background subtraction
            contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours

            for i in contours:
                if cv2.contourArea(i) > 500:  # Filter out small contours
                    x, y, w, h = cv2.boundingRect(i)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw bounding box

            stframe.image(ConvertColor(frame), channels="RGB")
            time.sleep(0.003)  # Add delay to control the frame rate
                
        capturtes.release()  # Release video capture object        
                        
            

    
         
            
            
   
    
    
























