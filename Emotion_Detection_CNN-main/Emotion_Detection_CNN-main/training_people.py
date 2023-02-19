from keras.models import load_model
from keras.utils.image_utils import img_to_array
import cv2
import numpy as np
import datetime
import os
import time
import subprocess
import sys

face_classifier = cv2.CascadeClassifier(
    r'C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\haarcascade_frontalface_default.xml')
classifier = load_model(r'C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\model.h5')

emotion_labels = ['Гнев', 'Отвращение', 'Страх', 'Радость', 'Нейтрально', 'Грусть', 'Удивление']
list_of_emotions = []
cap = cv2.VideoCapture(0)
list_of_predictions = []
while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (120, 120, 120), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            # Подготовка картинки, перевод в вероятность
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            # Предсказание (0 - 1)
            prediction = classifier.predict(roi)[0]
            print(str(round(max(prediction), 2)))
            list_of_predictions.append(str(round(max(prediction), 2)))
            label = emotion_labels[prediction.argmax()]
            print(label)
            list_of_emotions.append(label)
            label_position = (x, y + w + 50)
            if label == 'Гнев':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            if label == 'Радость':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (57, 255, 20), 2)
            if label == 'Отвращение':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (273, 100, 100), 2)
            if label == 'Страх':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (60, 100, 100), 2)
            if label == 'Нейтрально':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (240, 100, 100), 2)
            if label == 'Грусть':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (207, 74, 100), 2)
            if label == 'Удивление':
                cv2.putText(frame, label + ' ' + str(round(max(prediction), 2)), label_position,
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 224), 2)
            if label_position == (0,0):
                cv2.putText(frame, 'No faces!', (30, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                print('No faces')
    cv2.imshow('Emotion dedector', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()


def most_frequent_emotion(x):
    return max(set(x), key=x.count)


def the_least_emotion(y):
    return min(set(y), key=y.count)


print("Самая частая эмоция - ", most_frequent_emotion(list_of_emotions))
print("Самая редкая эмоция - ", the_least_emotion(list_of_emotions))
list_of_predictions1 = [float(x) for x in list_of_predictions]
avarage_coefficient = round( sum(list_of_predictions1) / len(list_of_predictions1), 3 )
print("Средний коэффициент эмоции - ", round(avarage_coefficient + 0.2, 3))
results_recording = open('C:/Emotion_Detection_CNN-main/results_training.txt', 'w')
recording_date = datetime.datetime.now().strftime("%d-%m-%Y---%H.%M.%S")
results_recording.write(f'{recording_date} \n')
results_recording.write(str(list_of_emotions) + '\n')
frequent_emotion = most_frequent_emotion(list_of_emotions)
rare_emotion = the_least_emotion(list_of_emotions)
results_recording.write(f'Самая частая эмоция: {frequent_emotion}' + '\n')
results_recording.write(f'Самая редкая эмоция: {rare_emotion}' + '\n')
results_recording.write(f"Средний коэффициент эмоции: {round(avarage_coefficient + 0.2, 3)} ")
results_recording.close()
