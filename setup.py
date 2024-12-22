from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.0",
    author="sunny",
    author_email="itzayush21@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)