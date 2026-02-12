📸 Face Detection Auto Photo Capture using OpenCV

This project uses OpenCV and Haar Cascade Classifier to detect human faces through a webcam. When a real face is detected, it automatically captures and saves a full photo.

The system captures only one image per detection session and displays it briefly on the screen.

🚀 Features

Real-time face detection using webcam

Automatic photo capture when a face is detected

Saves images in a local folder

Shows detected face with bounding box

Displays captured image for 2 seconds

Press q to quit anytime

🛠️ Requirements

Make sure you have the following installed:

Python 3.x

OpenCV

OS module (built-in)

Install OpenCV using:

pip install opencv-python

📁 Project Structure
Face_Detection_Project/
│
├── Face_detection.py      # Main Python file
├── dataset/             # Folder where images are saved
└── README.md            # Project documentation


The dataset folder is created automatically.

▶️ How to Run

Open your terminal or command prompt.

Navigate to the project folder.

Run the script:

python Face_detection.py 


Allow camera access if prompted.

🎯 How It Works

The webcam starts automatically.

The system converts frames to grayscale.

Histogram equalization improves brightness.

Haar Cascade detects faces.

When a face is detected:

A photo is saved in dataset/

The image is displayed for 2 seconds

Only one photo is captured per run.

Press q to exit.

💾 Output

Images are saved as:

dataset/photo_0.jpg
dataset/photo_1.jpg
...


Example console output:

Saved full photo: dataset/photo_0.jpg
Face detected and photo captured successfully!

⚙️ Important Parameters
scaleFactor = 1.1     # Detection accuracy
minNeighbors = 7      # Reduces false positives
minSize = (100,100)   # Ignores small objects


You can adjust these values to improve detection.

❗ Notes

Works best in good lighting conditions.

Face should be clearly visible.

Avoid backlight and dark environments.

Use a good quality webcam for better results.

📌 Future Improvements

Multiple face tracking

Continuous capture mode

Face recognition

Liveness detection

Database integration

👨‍💻 Author

Dinesh C
Student | Developer
Project developed using Python and OpenCV for academic and learning purposes.