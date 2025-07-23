import cv2
import mediapipe as mp
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Define piano key mapping (x1, x2 pixel regions on screen)
key_map = {
    'C': (50, 150),
    'D': (160, 260),
    'E': (270, 370),
    'F': (380, 480),
    'G': (490, 590),
    'A': (600, 700),
    'B': (710, 810),
}

# Load sound files once
sounds = {key: pygame.mixer.Sound(f"sounds/{key}.wav") for key in key_map.keys()}

# Track last played time to avoid rapid repeats
last_played = {}
delay = 0.5  # seconds

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Mirror the image
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Draw piano keys
    for key, (x1, x2) in key_map.items():
        cv2.rectangle(img, (x1, 400), (x2, 600), (255, 255, 255), -1)
        cv2.putText(img, key, (x1 + 30, 580), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

    # Hand detection and fingertip tracking
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8:  # Index fingertip
                    cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

                    for key, (x1, x2) in key_map.items():
                        if x1 < cx < x2 and 400 < cy < 600:
                            now = time.time()
                            if key not in last_played or now - last_played[key] > delay:
                                sounds[key].play()
                                last_played[key] = now

    cv2.imshow("Virtual Piano", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
