from tkinter import *
# path = r"C:\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\Emotions\Happy"
# files=os.listdir(path)
# d=random.choice(files)
tk = Tk()
canvas = Canvas(tk, width=400, height=100)
canvas.pack()
canvas.create_text(200, 50, text="ПОВТОРЯЙ ЗА ИЗОБРАЖЕНИЕМ", font="Courier 20")
tk.title('Эмпа - тренажер')
canvas.mainloop()