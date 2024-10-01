import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Create the Notepad GUI
def create_notepad():
    window = tk.Tk()
    window.title("Voice-Enabled Notepad")
    window.geometry("600x500")  # Set a fixed window size
    window.configure(bg="#f0f0f0")  # Set background color

    # Create a scrollable text area
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=25, bg="#ffffff", fg="#000000", font=("Arial", 12))
    text_area.grid(column=0, row=0, padx=20, pady=20)

    # Function to convert voice to text and insert into notepad
    def take_voice_input():
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                text_area.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I did not understand the audio")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")

    # Function to clear the text area
    def clear_text():
        text_area.delete('1.0', tk.END)

    # Function to save the notepad content
    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_area.get('1.0', tk.END))
            messagebox.showinfo("Success", "File saved successfully!")

    # Add a button to start voice input
    record_button = tk.Button(window, text="Start Voice Input", command=take_voice_input, bg="#4CAF50", fg="white", font=("Arial", 12))
    record_button.grid(column=0, row=1, padx=10, pady=10)

    # Add a button to clear text
    clear_button = tk.Button(window, text="Clear Text", command=clear_text, bg="#FF5722", fg="white", font=("Arial", 12))
    clear_button.grid(column=0, row=2, padx=10, pady=10)

    # Add a button to save text
    save_button = tk.Button(window, text="Save Text", command=save_file, bg="#2196F3", fg="white", font=("Arial", 12))
    save_button.grid(column=0, row=3, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_notepad()
