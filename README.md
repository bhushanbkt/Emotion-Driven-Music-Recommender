# Webcam-Emotion-Detector-with-Spotify-Recommendations

This is a Streamlit web application that captures images from the webcam, detects emotions in the captured images, and recommends songs based on the detected emotions using the Spotify API.

![Screenshot (291)](https://github.com/bhushanbkt/Webcam-Emotion-Detector-with-Spotify-Recommendations/assets/91175596/202cfaa5-23b1-4161-b27c-2e2317824953)

## Installation

1. Clone the repository: https://github.com/bhushanbkt/Webcam-Emotion-Detector-with-Spotify-Recommendations
2. Navigate to the project directory:
3. 
4. 3. Install the dependencies: requirements.txt
  
  ![Screenshot (292)](https://github.com/bhushanbkt/Webcam-Emotion-Detector-with-Spotify-Recommendations/assets/91175596/ef7487d0-d041-4445-9fc2-ae5adfa7260d)

## Usage

1. Fill in the Spotify credentials:

Before running the application, make sure to fill in your Spotify API credentials in the code:

```python
# Spotify credentials
SPOTIFY_CLIENT_ID = 'your_client_id'
SPOTIFY_CLIENT_SECRET = 'your_client_secret'

#Run the Streamlit application:
streamlit run main.py
```

This application uses the following libraries:

Streamlit
OpenCV
NumPy
RMN
Spotipy
