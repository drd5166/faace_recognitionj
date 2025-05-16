# faace_recognitionj
#  Real-Time Face Detection using OpenCV (Python & Android)

This project implements real-time face detection using the Haar Cascade Classifier from OpenCV. It supports both:

-  A **Python script** that performs face detection using a webcam.
-  An **Android app** that detects faces using the phone's camera with OpenCV (no internet or ML Kit required).



##  Features

✅ Real-time face detection  
✅ Uses OpenCV’s pre-trained Haar Cascade model  
✅ Works offline (no cloud or API needed)  
✅ Lightweight and fast  
✅ Cross-platform: Desktop (Python) and Mobile (Android)



##  Model Description

This project uses the **Haar Cascade Classifier**, a classical machine learning-based approach for object detection developed by **Viola and Jones**.

###  How It Works

- The algorithm uses **Haar-like features** to detect facial structures.
- It applies **integral images** to compute features rapidly.
- A **cascade of classifiers** is trained from positive (with faces) and negative (without faces) samples.
- At runtime, the model quickly eliminates non-face regions in early stages and focuses only on potential face areas.

###  Model Used

- Model file: `haarcascade_frontalface_default.xml`
- Provided by OpenCV under BSD license
- Pre-trained for detecting frontal human faces


## Android App
This Android app demonstrates real-time face detection. It uses the device camera to capture video frames and detects faces with contours, displaying bounding boxes and facial landmarks on the preview.


## Features

- Real-time face detection with camera preview
- Switch between front and back camera
- Draw face contours and bounding boxes overlay
- Camera permission handling



## Project Structure

- *MainActivity.kt*  
  Handles UI, camera permission requests, and initializes the camera manager.

- *CameraManager.kt*  
  Manages CameraX APIs, provides camera preview, and routes image frames to the face detection analyzer.
- *FaceContourDetectionProcessor.kt*  
  Implements  face detection and processes detection results to draw overlays.

- *BaseImageAnalyzer.kt*  
  Abstract class that integrates  InputImage with CameraX image analysis.

- *GraphicOverlay.kt*  
  Custom view for rendering face bounding boxes and landmarks on top of camera preview.

- *res/layout/activity_main.xml*  
  UI layout containing PreviewView and overlay views.


