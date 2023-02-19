import os
import random
import time
import subprocess

path1 = r"C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\Emotions\Happy\Smiling-Man.jpg"
# Open file with desired program
prog = r'C:/Program Files/IrfanView/i_view64.exe'
OpenIt = subprocess.Popen([prog, path1])

# keep it open for 30 seconds
time.sleep(18)

OpenIt.terminate()
path2 = r"C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\Emotions\Angry\1653584343_7-kartinkin-net-p-zloi-chelovek-kartinki-8.jpg"
# Open file with desired program
OpenIt = subprocess.Popen([prog, path2])

# keep it open for 30 seconds
time.sleep(10)

OpenIt.terminate()
path3 = r"C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\Emotions\Neutral\ilya-shatilin.jpg"
# Open file with desired program
OpenIt = subprocess.Popen([prog, path3])

# keep it open for 30 seconds
time.sleep(10)

OpenIt.terminate()
path4 = r"C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\Emotions\Sad\shutterstock_126009806.jpg"
# Open file with desired program
OpenIt = subprocess.Popen([prog, path4])

# keep it open for 30 seconds
time.sleep(10)

OpenIt.terminate()
path5 = r"C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\Emotions\Surprised\0848551965a0d4488585c4fd41f82815.jpg"
# Open file with desired program
OpenIt = subprocess.Popen([prog, path5])

# keep it open for 30 seconds
time.sleep(10)

OpenIt.terminate()