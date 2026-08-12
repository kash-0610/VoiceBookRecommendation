import tkinter as tk
import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():
    result_label.config(text="Listening... Please speak.")

    try:
        with sr.Microphone(device_index=0) as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        result_label.config(text="Processing...")

        text = recognizer.recognize_google(audio)

        result_label.config(text="You said:\n" + text)

    except sr.WaitTimeoutError:
        result_label.config(text="I didn't hear you. Please try again.")

    except sr.UnknownValueError:
        result_label.config(
            text="I couldn't understand you. Please speak again."
        )

    except sr.RequestError:
        result_label.config(
            text="Speech recognition service is unavailable."
        )


window = tk.Tk()
window.title("Voice Book Recommendation")
window.geometry("500x350")

title = tk.Label(
    window,
    text="📚 Voice Book Recommendation",
    font=("Arial", 20, "bold")
)
title.pack(pady=40)

speak_button = tk.Button(
    window,
    text="🎤 Speak Here",
    font=("Arial", 16, "bold"),
    command=listen,
    bg="blue",
    fg="white",
    padx=30,
    pady=15
)
speak_button.pack()

result_label = tk.Label(
    window,
    text="Click 'Speak Here' and tell us what book you want.",
    font=("Arial", 14),
    wraplength=450
)
result_label.pack(pady=40)

window.mainloop()