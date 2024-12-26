import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time
import os


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing.... ")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("I did not understand that. Please try again.")
            return ""


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        
        if data1:  # Only proceed if there's valid speech input
            try:
                if "your name" in data1:
                    name = "My name is Boardy the bot."
                    speechtx(name)

                elif "how old are you" in data1:
                    age = "i am an ai with infinite age."
                    speechtx(age)
                    
                elif "what is your age" in data1:
                    age = "i am an ai with infinite age."
                    speechtx(age)

                elif 'time' in data1:
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    speechtx(f"The time is {current_time}")

                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif 'google' in data1:
                    webbrowser.open("https://www.google.co.in/")
                    
                    
                elif 'github' in data1:
                    webbrowser.open("https://github.com/thedrag0nspirit")
                    
                elif 'google' in data1:
                    webbrowser.open("https://www.google.co.in/")
                    
                elif 'google' in data1:
                    webbrowser.open("https://www.google.co.in/")
                    
                elif 'google' in data1:
                    webbrowser.open("https://www.google.co.in/")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en", category="neutral")
                    print(joke_1)
                    speechtx(joke_1)

                elif 'play song' in data1:
                    song_folder = r"D:\New folder\songs"  # Ensure this folder exists
                    if os.path.exists(song_folder):
                        listsong = os.listdir(song_folder)
                        if listsong:
                            print(f"Playing {listsong[0]}")
                            os.startfile(os.path.join(song_folder, listsong[0]))
                        else:
                            speechtx("No songs found in the folder.")
                    else:
                        speechtx("Song folder not found.")

                elif "exit" in data1:
                    speechtx('Thank you! Goodbye.')
                    break
                
                else:
                    speechtx("I didn't quite catch that. Please try again.")
                
            except Exception as e:
                print(f"An error occurred: {e}")
                speechtx("Something went wrong. Please try again.")
            
            time.sleep(1)  # Add delay before next command to prevent continuous looping
