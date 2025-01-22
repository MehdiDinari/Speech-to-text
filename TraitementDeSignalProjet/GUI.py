import tkinter as tk
import tkinter.font as tkFont
import pyttsx3
import speech_recognition as sr
from test import Test
from record import Record

class TTSWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech")
        width = 400
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.frame = tk.Frame(root, bg="#264653")
        self.frame.place(x=0, y=0, width=width, height=height)

        self.label = tk.Label(self.frame, text="Enter Text:", bg="#264653", fg="#ffffff")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(self.frame, width=50)
        self.text_entry.pack(pady=10)

        self.speak_button = tk.Button(self.frame, text="Speak", command=self.speak_text, bg="#2a9d8f", fg="#ffffff")
        self.speak_button.pack(pady=10)

    def speak_text(self):
        text = self.text_entry.get()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

class App:
    def __init__(self, root):
        # Setting title
        root.title("Speech Application")
        # Setting window size
        width = 800
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        frame = tk.Frame(root, bg="#264653")
        frame.place(x=0, y=0, width=width, height=height)

        GButton_558 = tk.Button(frame)
        GButton_558["bg"] = "#2a9d8f"
        GButton_558["activebackground"] = "#2980b9"
        GButton_558["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Helvetica', size=12, weight="bold")
        GButton_558["font"] = ft
        GButton_558["fg"] = "#ffffff"
        GButton_558["justify"] = "center"
        GButton_558["text"] = "Dire un mot"
        GButton_558["relief"] = "raised"
        GButton_558.place(x=100, y=50, width=130, height=54)
        GButton_558["command"] = Record

        GButton_284 = tk.Button(frame)
        GButton_284["bg"] = "#2a9d8f"
        GButton_284["activebackground"] = "#2980b9"
        ft = tkFont.Font(family='Helvetica', size=16, weight="bold")
        GButton_284["font"] = ft
        GButton_284["fg"] = "#ffffff"
        GButton_284["justify"] = "center"
        GButton_284["text"] = "Vérifier"
        GButton_284.place(x=270, y=50, width=130, height=54)
        GButton_284["command"] = self.check_command

        GLabel_179 = tk.Label(frame)
        GLabel_179["bg"] = "#CFDBD5"
        ft = tkFont.Font(family='Helvetica', size=25)
        GLabel_179["font"] = ft
        GLabel_179["fg"] = "#2c3e50"
        GLabel_179["justify"] = "center"
        GLabel_179["text"] = ""
        GLabel_179["relief"] = "solid"
        GLabel_179.place(x=440, y=50, width=264, height=54)
        self.GLabel_179 = GLabel_179

        text_label = tk.Label(frame, text="Taper le texte :", bg="#264653", fg="#ffffff", font=('Helvetica', 14))
        text_label.place(x=50, y=150, width=200, height=30)

        self.text_box = tk.Text(frame, wrap=tk.WORD, font=('Helvetica', 14))
        self.text_box.place(x=50, y=190, width=700, height=300)

        GButton_TTS = tk.Button(frame)
        GButton_TTS["bg"] = "#2a9d8f"
        GButton_TTS["activebackground"] = "#2980b9"
        ft = tkFont.Font(family='Helvetica', size=14, weight="bold")
        GButton_TTS["font"] = ft
        GButton_TTS["fg"] = "#ffffff"
        GButton_TTS["justify"] = "center"
        GButton_TTS["text"] = "Transformer"
        GButton_TTS.place(x=335, y=510, width=130, height=54)
        GButton_TTS["command"] = self.speak_text

        GButton_STT = tk.Button(frame)
        GButton_STT["bg"] = "#2a9d8f"
        GButton_STT["activebackground"] = "#2980b9"
        ft = tkFont.Font(family='Helvetica', size=14, weight="bold")
        GButton_STT["font"] = ft
        GButton_STT["fg"] = "#ffffff"
        GButton_STT["justify"] = "center"
        GButton_STT["text"] = "Dire une phrase"
        GButton_STT.place(x=500, y=510, width=170, height=54)
        GButton_STT["command"] = self.record_speech

    def check_command(self):
        result = Test()
        self.GLabel_179["text"] = result

    def speak_text(self):
        text = self.text_box.get("1.0", tk.END).strip()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def record_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.GLabel_179["text"] = "Listening..."
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            self.text_box.insert(tk.END, text)
            self.GLabel_179["text"] = "Done"
        except sr.UnknownValueError:
            self.GLabel_179["text"] = "Could not understand audio"
        except sr.RequestError as e:
            self.GLabel_179["text"] = f"Could not request results; {e}"

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
