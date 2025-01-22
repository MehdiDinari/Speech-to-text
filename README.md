# Speech-to-Text and Text-to-Speech Application

## 🚀 Overview
This Python application provides an intuitive graphical interface for real-time speech recognition and text-to-speech conversion. It allows users to seamlessly convert spoken words into text and transform written text into spoken words. This tool is particularly beneficial for dictation, transcription, accessibility, and content creation.

## 📌 Features

### 🎙 Speech-to-Text (STT)
Convert spoken words into written text in real time. Useful for:
- Dictation and note-taking
- Automated transcription
- Accessibility for individuals with disabilities
- Voice command integration

### 📃 Text-to-Speech (TTS)
Convert written text into synthesized speech. Useful for:
- Reading documents aloud
- Assisting visually impaired users
- Creating audio versions of text-based content
- Enhancing user experience in applications

## 🛠 Technologies & Dependencies
This application utilizes state-of-the-art machine learning and signal processing techniques to enable accurate speech recognition and natural-sounding text-to-speech synthesis.

### Required Libraries
Ensure you have the following libraries installed before running the program:

```bash
pip install tensorflow SpeechRecognition sounddevice pyttsx3 librosa numpy matplotlib ipython keras pyaudio
```

| Library          | Purpose |
|-----------------|---------|
| **TensorFlow**  | Machine learning framework for advanced processing |
| **SpeechRecognition** | Recognizes and converts speech into text |
| **sounddevice** | Handles audio recording and playback |
| **pyttsx3** | Converts text into speech |
| **librosa** | Performs audio analysis |
| **numpy** | Supports numerical computations |
| **matplotlib** | Enables data visualization |
| **IPython** | Provides an interactive Python shell |
| **Keras** | Implements deep learning models |
| **pyaudio** | Provides an interface for audio input/output |

## 🎬 Installation Guide

### Prerequisites
Ensure that you have Python installed on your system. You can download it from [Python Official Website](https://www.python.org/).

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/speech-recognition-tts.git
cd speech-recognition-tts
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

## 🏗 Usage Instructions

1. Launch the application by running `python main.py`.
2. Select one of the two main functionalities:
   - **Speech-to-Text:** Click the microphone button and speak into your microphone. The application will transcribe your speech into text.
   - **Text-to-Speech:** Enter or paste text into the input field and click the play button. The application will read the text aloud.
3. Adjust any settings as needed (e.g., language, voice speed, volume).
4. Save or export transcribed text if required.

## 🎨 Graphical User Interface (GUI)
This application features a user-friendly interface that allows for easy interaction:
- **Record Button:** Start speech-to-text transcription
- **Play Button:** Read aloud entered text
- **Stop Button:** Stop ongoing audio playback
- **Save Option:** Export transcribed text to a file

## 🛠 Troubleshooting

### Common Issues & Solutions
- **Microphone not detected:** Ensure your microphone is connected and configured correctly.
- **No sound output in TTS mode:** Verify that your speakers are working and volume is not muted.
- **Library installation errors:** Run `pip install -r requirements.txt` again or manually install missing dependencies.

## 🎯 Future Improvements
- Support for multiple languages
- Enhanced voice customization options
- Integration with cloud-based AI models for improved accuracy
- Mobile and web versions

## 📜 License
This project is open-source and available under the MIT License. You are free to modify and distribute it.

## 🤝 Contributing
We welcome contributions from the community! Feel free to submit issues or pull requests.

### How to Contribute
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes and push them to your fork.
4. Submit a pull request for review.

## 📩 Contact & Support
If you have any questions or need support, feel free to reach out:
- **Email:** treshlol202@gmail.com
**LinkedIn :** [Mehdi Dinari](https://www.linkedin.com/in/mehdi-dinari-b0487a2a9/)


Happy coding! 🚀

