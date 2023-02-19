import subprocess
import sys
import time
repeat_for_img = subprocess.Popen([sys.executable, 'C:/Emotion_Detection_CNN-main/Emotion_Detection_CNN-main/repeat_for_img.py'])
time.sleep(2)
trainig_people = subprocess.Popen([sys.executable, 'C:/Emotion_Detection_CNN-main/Emotion_Detection_CNN-main/training_people.py'])
pictures = subprocess.Popen([sys.executable, 'C:/Emotion_Detection_CNN-main/Emotion_Detection_CNN-main/pictures_show.py'])

trainig_people.wait()
