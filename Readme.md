🎹 Virtual Piano with Hand Tracking
This project implements a virtual piano that can be played using hand gestures detected via your webcam. It uses MediaPipe for real-time hand tracking and Pygame for sound playback and graphical display.
________________________________________
🔑 Features
•	🎯 Hand Tracking — Detects your hand using MediaPipe and tracks your index fingertip.
•	🎹 Virtual Piano Keys — On-screen keys for C, D, E, F, G, A, B notes.
•	🔊 Sound Playback — Plays corresponding .wav files when a key is "touched".
•	⏱️ Debouncing — Prevents repeated unintended key presses using a delay mechanism.
________________________________________
⚙️ Prerequisites
Make sure you have the following:
•	✅ Python 3.7+
•	✅ A working webcam
________________________________________
📦 Setup
Follow these steps to get started:
1. Download Project Files
Save the virtual_piano.py script in your desired folder, e.g.:
C:\Users\TAMEEZ\Desktop\VirtualPianoHand
________________________________________
2. Create the sounds Directory
Inside your project folder, create a new folder named:
sounds
________________________________________
3. Add Sound Files
Add the following .wav files into the sounds folder:
A.wav, B.wav, C.wav, D.wav, E.wav, F.wav, G.wav
(You can download free piano sounds online or record your own)
________________________________________
4. (Optional) Set Up a Virtual Environment
It's best to use a virtual environment for Python projects.
# Navigate to your project directory
cd C:\Users\TAMEEZ\Desktop\VirtualPianoHand

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate
________________________________________
5. Install Dependencies
Create a file named requirements.txt and add:
mediapipe
pygame
opencv-python
Then install them using:
pip install -r requirements.txt
________________________________________
▶️ How to Run
Make sure your virtual environment is active, then run:
python virtual_piano.py
________________________________________
🎮 Usage
•	A window with your webcam feed will appear.
•	You'll see virtual white piano keys at the bottom of the screen.
•	Move your hand in front of the webcam.
•	A red dot will follow your index fingertip.
•	"Touch" a white key with your fingertip to play a note.
•	Press q to quit.
________________________________________
🛠️ Troubleshooting
Problem	Solution
❌ "Fatal error in launcher"	Delete venv and recreate the virtual environment
📷 No webcam feed	Check camera permissions and ensure it's not used by other apps
🐢 Laggy performance	Ensure proper lighting and close unused applications
🔇 No sound	Check your system volume and confirm .wav files are correct and in the sounds folder
________________________________________
🙌 Credits
•	MediaPipe — Hand tracking technology
•	Pygame — Audio playback and graphical interface
