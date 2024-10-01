from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import threading

app = Flask(__name__)
recognizer = sr.Recognizer()
recognized_text = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_voice_input')
def start_voice_input():
    global recognized_text
    threading.Thread(target=take_voice_input).start()  # Run voice recognition in a separate thread
    return jsonify(recognized_text)

def take_voice_input():
    global recognized_text
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            recognized_text = recognizer.recognize_google(audio)
            print(f"You said: {recognized_text}")
    except sr.UnknownValueError:
        recognized_text = "Sorry, I did not understand the audio."
    except sr.RequestError as e:
        recognized_text = f"Could not request results; {e}"

if __name__ == '__main__':
    app.run(debug=True)
