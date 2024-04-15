import streamlit as st
import cv2
from rmn import RMN
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize RMN model
m = RMN()

# Spotify credentials
SPOTIFY_CLIENT_ID = '953204a9f526470f999da4bf2b9e0397'
SPOTIFY_CLIENT_SECRET = '4ad36bedfe1d4dabb6152f0f7268e32d'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))

# Function to detect emotion for a single frame
def detect_emotion(image):
    results = m.detect_emotion_for_single_frame(image)
    return results

# Function to draw detected emotions on the image
def draw_emotions(image, results):
    image = m.draw(image, results)
    return image

def recommend_songs(expression):
    recommendations = []
    limit = 10  # Number of songs to recommend
    
    if expression == "happy":
        # Recommend happy songs
        results = sp.search(q='mood:happy', limit=limit, type='track')
        for track in results['tracks']['items']:
            recommendations.append(track['external_urls']['spotify'])
    elif expression == "sad":
        # Recommend sad songs
        results = sp.search(q='mood:sad', limit=limit, type='track')
        for track in results['tracks']['items']:
            recommendations.append(track['external_urls']['spotify'])
    elif expression == "angry":
        # Recommend angry songs
        results = sp.search(q='mood:angry', limit=limit, type='track')
        for track in results['tracks']['items']:
            recommendations.append(track['external_urls']['spotify'])
    elif expression == "surprised":
        # Recommend surprised songs
        results = sp.search(q='mood:surprised', limit=limit, type='track')
        for track in results['tracks']['items']:
            recommendations.append(track['external_urls']['spotify'])
    else:
        # Default recommendation: Search for popular songs without specifying mood
        results = sp.search(q='genre:pop', limit=limit, type='track')  # Search for popular songs
        for track in results['tracks']['items']:
            recommendations.append(track['external_urls']['spotify'])
        
    return recommendations[:limit]  # Return only the first 10 recommendations


def main():
    st.title("Webcam Emotion Detector")

    # Create a button to capture image from webcam
    if st.button("Capture Image"):
        # OpenCV code to capture image from webcam
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Detect emotions
        results = detect_emotion(frame)
        
        # Get the dominant emotion
        dominant_emotion = max(results, key=lambda x: x.get('score', 0)).get('label', 'neutral')

        # Display captured image
        st.image(frame, channels="BGR", caption="Captured Image")

        # Draw emotions on the image
        image_with_emotions = draw_emotions(frame, results)

        # Display image with detected emotions
        st.image(image_with_emotions, channels="BGR", caption=f"Emotions Detected: {dominant_emotion.title()}")

        # Recommend songs based on the dominant emotion
        recommended_songs = recommend_songs(dominant_emotion)
        
        # Display recommended songs
        # st.markdown(f"### Songs for {dominant_emotion.title()}:")
        for i, song_link in enumerate(recommended_songs, start=1):
            st.markdown(f"**Song {i}:** [Song Link]({song_link})")

if __name__ == "__main__":
    main()
